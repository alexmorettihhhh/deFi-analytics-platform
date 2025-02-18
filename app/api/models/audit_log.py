import logging
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

# Настроим логгер
logging.basicConfig(filename='audit_log.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

Base = declarative_base()

class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    event_type = Column(String)  # e.g., 'login', 'api_call', 'data_modification'
    user_id = Column(String, nullable=True)
    ip_address = Column(String)
    endpoint = Column(String)
    method = Column(String)
    request_data = Column(JSON, nullable=True)
    response_status = Column(Integer)
    execution_time = Column(Integer)  # in milliseconds
    additional_data = Column(JSON, nullable=True)

    def __repr__(self):
        return f"<AuditLog(id={self.id}, event_type={self.event_type}, user_id={self.user_id})>"

def log_action(action: str):
    """Функция для записи действия в журнал"""
    try:
        logging.info(action)
    except Exception as e:
        logging.error(f"Ошибка при записи лога: {e}")

def log_balance_change(address: str, old_balance: str, new_balance: str):
    """Логирование изменений баланса"""
    action = f"Баланс адреса {address} изменился с {old_balance} на {new_balance}"
    log_action(action)

def log_transaction(address: str, amount: str, tx_hash: str):
    """Логирование транзакции"""
    action = f"Транзакция от {address} на сумму {amount}. Хэш транзакции: {tx_hash}"
    log_action(action)
