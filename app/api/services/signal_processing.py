from typing import List
import logging

def process_trading_signals(data: List[dict]):
    signals = []
    for item in data:
        if item["price_change"] > 5:  # Порог для сигналов
            signals.append(item)
    return signals

def send_signal_notification(signal):
    logging.info(f"Sending signal notification: {signal}")
