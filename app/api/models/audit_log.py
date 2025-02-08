import logging
from datetime import datetime

# Настроим логгер
logging.basicConfig(filename='audit_log.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_action(action: str):
    """Функция для записи действия в журнал"""
    logging.info(action)

def log_balance_change(address: str, old_balance: str, new_balance: str):
    """Логирование изменений баланса"""
    action = f"Баланс адреса {address} изменился с {old_balance} на {new_balance}"
    log_action(action)

def log_transaction(address: str, amount: str, tx_hash: str):
    """Логирование транзакции"""
    action = f"Транзакция от {address} на сумму {amount}. Хэш транзакции: {tx_hash}"
    log_action(action)
