from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.api.models.audit_log import AuditLog
from sqlalchemy.orm import Session
import time
import json
from typing import Callable
import logging

logger = logging.getLogger(__name__)

class AuditMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, db: Session):
        super().__init__(app)
        self.db = db

    async def dispatch(self, request: Request, call_next: Callable):
        # Start timer for request
        start_time = time.time()
        
        # Get request details
        path = request.url.path
        method = request.method
        ip_address = request.client.host
        
        try:
            # Get user from request state if authenticated
            user_id = getattr(request.state, 'user_id', None)
            
            # Get request body
            body = None
            if method in ['POST', 'PUT', 'PATCH']:
                try:
                    body = await request.json()
                except:
                    body = None
            
            # Process the request
            response = await call_next(request)
            
            # Calculate execution time
            execution_time = int((time.time() - start_time) * 1000)
            
            # Create audit log entry
            audit_log = AuditLog(
                event_type='api_call',
                user_id=user_id,
                ip_address=ip_address,
                endpoint=path,
                method=method,
                request_data=body,
                response_status=response.status_code,
                execution_time=execution_time
            )
            
            # Save to database
            self.db.add(audit_log)
            await self.db.commit()
            
            # Log slow requests
            if execution_time > 1000:  # More than 1 second
                logger.warning(f"Slow request: {method} {path} took {execution_time}ms")
            
            return response
            
        except Exception as e:
            logger.error(f"Error in audit middleware: {str(e)}")
            # If there's an error, we still want to return the response if possible
            if 'response' in locals():
                return response
            raise 