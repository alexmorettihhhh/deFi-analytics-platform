from prometheus_client import Counter, Histogram, Gauge
from prometheus_client.exposition import generate_latest
from fastapi import Request
import time
from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

ACTIVE_REQUESTS = Gauge(
    'http_requests_active',
    'Number of active HTTP requests'
)

DB_QUERY_LATENCY = Histogram(
    'db_query_duration_seconds',
    'Database query latency',
    ['query_type']
)

CACHE_HITS = Counter(
    'cache_hits_total',
    'Total number of cache hits'
)

CACHE_MISSES = Counter(
    'cache_misses_total',
    'Total number of cache misses'
)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        # Increment active requests
        ACTIVE_REQUESTS.inc()
        
        # Start timer
        start_time = time.time()
        
        method = request.method
        path = request.url.path
        
        try:
            # Process request
            response = await call_next(request)
            
            # Record metrics
            REQUEST_COUNT.labels(
                method=method,
                endpoint=path,
                status=response.status_code
            ).inc()
            
            REQUEST_LATENCY.labels(
                method=method,
                endpoint=path
            ).observe(time.time() - start_time)
            
            return response
            
        except Exception as e:
            # Record failed requests
            REQUEST_COUNT.labels(
                method=method,
                endpoint=path,
                status=500
            ).inc()
            raise
            
        finally:
            # Decrement active requests
            ACTIVE_REQUESTS.dec()

def record_db_query_latency(query_type: str, duration: float):
    """Record database query latency"""
    DB_QUERY_LATENCY.labels(query_type=query_type).observe(duration)

def record_cache_hit():
    """Record cache hit"""
    CACHE_HITS.inc()

def record_cache_miss():
    """Record cache miss"""
    CACHE_MISSES.inc()

async def metrics_endpoint():
    """Endpoint to expose metrics to Prometheus"""
    return generate_latest() 