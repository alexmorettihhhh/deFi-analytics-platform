# Документация API для платформы DeFi Analytics

## Обзор

**DeFi Analytics Platform** предоставляет API для анализа данных DeFi и отправки торговых сигналов в реальном времени. Он поддерживает несколько блокчейнов (Ethereum, Polygon, BSC, Solana и другие), позволяя пользователям отслеживать и взаимодействовать с транзакциями в децентрализованных финансовых системах и смарт-контрактами.

---

## **Base URL**

- Базовый URL для API:

```https://api.defi-analytics-platform.com/v1```

## **Аутентификация**

- Для работы с API необходимо использовать **API-ключ**. Для аутентификации запросов нужно передавать ваш API-ключ в заголовке `Authorization` header.

- Пример: `Authorization: Bearer YOUR_API_KEY`


---

## Доступные Эндпоинты

---

- ### 1. **Получить Торговый Сигнал**

- #### Эндпоинт: `/signal`

- **Метод**: `GET`

- **Описание**: Этот эндпоинт позволяет пользователям получить последние торговые сигналы на основе рыночных данных.

- **Параметры запроса**:
- `pair` (string) — Торговая пара, по которой запрашивается сигнал (например, `ETH-USDT`).
- `threshold` (float) — Порог изменения цены для генерации торгового сигнала. По умолчанию `5.0` (5%).

**Ответ**:
```json
{
  "signal": "Buy ETH",
  "pair": "ETH-USDT",
  "threshold": 5.0,
  "timestamp": "2025-02-09T14:23:00Z"
}
```

### 2. Получить Баланс

- Эндпоинт: `/balance`
- Метод: `GET`
- Описание: Этот эндпоинт возвращает текущий баланс указанного адреса на выбранном блокчейне.
- Параметры запроса:
`address` (string) — Адрес кошелька (например, `0x1234567890abcdef...`).
`blockchain` (string) — Блокчейн-сеть (например, `ethereum`, `polygon`, `bsc`).

#### Ответ:
```json
{
  "address": "0x1234567890abcdef...",
  "balance": "12345.6789",
  "currency": "USDT"
}
```
### 3. Получить Данные Блокчейна

Эндпоинт: `/blockchain-data`
Метод: `GET`

- Описание: Этот эндпоинт возвращает аналитические данные для выбранного блокчейна, включая объем транзакций и тренды.

#### Параметры запроса:

`blockchain` (string) — Блокчейн для анализа (например, `ethereum`, `polygon`).

#### Ответ:
```json
{
  "blockchain": "ethereum",
  "data": {
    "total_transactions": 1234567,
    "total_volume": "5000000",
    "active_addresses": 12000
  }
}
```
### 4. Получить События Из Смарт-Контракта

- Эндпоинт: `/events`
- Метод: `GET`

- Описание: Этот эндпоинт извлекает события (логи) из указанного смарт-контракта на выбранном блокчейне.

- Параметры запроса:

`contract_address` (string) — Адрес смарт-контракта.
`blockchain` (string) — Блокчейн (например, `ethereum`, `polygon`, `bsc`).
`from_block` (number) — Начальный блок для извлечения событий (необязательный).
`to_block` (number) — Конечный блок для извлечения событий (необязательный).
#### Ответ:
```json
{
  "events": [
    {
      "event_type": "Transfer",
      "data": "0xabcdef123456...",
      "block_number": 1234567
    },
    {
      "event_type": "Approval",
      "data": "0xabcdef987654...",
      "block_number": 1234568
    }
  ]
}
```
### 5. Отправить Транзакцию

- Эндпоинт: `/transaction`
- Метод: `POST`

- Описание: Этот эндпоинт позволяет отправить транзакцию в смарт-контракт (например, вызвать функцию контракта для взаимодействия).

- Параметры тела:
-  `from_address` (string) — Адрес отправителя транзакции.
- `to_address` (string) — Адрес смарт-контракта.
- `private_key` (string) — Приватный ключ отправителя для подписания транзакции.
- `amount` (number) — Сумма токенов для отправки.
- `function` (string) — Название функции контракта (например,`transfer`, `approve`).
#### Ответ:

```json
{
  "transaction_hash": "0xabcdef123456...",
  "status": "success",
  "message": "Transaction sent successfully"
}
```

### 6. Подписка на События

- Эндпоинт: `/subscribe`
- Метод: `POST`

- Описание: Этот эндпоинт позволяет пользователям подписываться на события в реальном времени для определенного смарт-контракта.

- Параметры тела:

- `contract_address` (string) — Адрес смарт-контракта.
- `event_type` (string) — Тип события, на который нужно подписаться (например, `Transfer`, `Approval`).
 #### Ответ:
```json
{
  "status": "subscribed",
  "message": "Subscribed to events successfully"
}
```
### Ошибки

- Если произошла ошибка, API вернет стандартный ответ об ошибке.

Пример:
```json
{
  "error": {
    "code": 400,
    "message": "Invalid address format"
  }
}
```
### Использование WebSocket API

WebSocket API используется для получения данных о торговых парах в реальном времени. Это позволяет пользователю отслеживать изменения цен, объемы торгов и другие данные без необходимости выполнять регулярные запросы.

#### Эндпоинт: `/ws/{pair}`
**Метод**: `GET`

- **Описание**: Соединение с WebSocket для получения данных в реальном времени для торговой пары (например, `ETH-USDT`).

**Пример запроса**:
```bash
wss://api.defi-analytics-platform.com/ws/ETH-USDT
```
#### Ответ:
```json
{
  "pair": "ETH-USDT",
  "price": "4000.50",
  "volume": "12345.67",
  "timestamp": "2025-02-09T14:30:00Z"
}
```
### 4. **Инструкции по настройке WebSocket сервера**
Дополнительно можно предоставить информацию о том, как пользователи могут настроить WebSocket-соединение для получения данных о торговых сигналах, например, через Python или JavaScript.

#### Пример (для Python):

```markdown
### Пример использования WebSocket с Python:

```python
import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    print(f"New data: {data}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("WebSocket opened")
    
ws = websocket.WebSocketApp("wss://api.defi-analytics-platform.com/ws/ETH-USDT",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open
ws.run_forever()
```
### Пример использования API

- 1. **Получение торгового сигнала**:
   ```bash
   curl -X GET "https://api.defi-analytics-platform.com/v1/signal?pair=ETH-USDT&threshold=5.0" \
        -H "Authorization: Bearer YOUR_API_KEY"
    ```
- 2. Получение баланса:
```bash
curl -X GET "https://api.defi-analytics-platform.com/v1/balance?address=0x1234567890abcdef&blockchain=ethereum" \
     -H "Authorization: Bearer YOUR_API_KEY"
```
- 2. Получение баланса:
```bash
curl -X POST "https://api.defi-analytics-platform.com/v1/transaction" \
     -H "Content-Type: application/json" \
     -d '{
       "from_address": "0x1234567890abcdef",
       "to_address": "0xabcdef1234567890",
       "private_key": "YOUR_PRIVATE_KEY",
       "amount": 10.0,
       "function": "transfer"
     }'
```
  
### Установка и запуск бота:

1. Установите все зависимости:
```bash
pip install -r requirements.txt
```

### Валидация и формат данных

- Параметры запроса и тела должны быть переданы в формате JSON.
- Для числовых значений, таких как `threshold`, `amount`, допустимы только положительные числа.
- Адреса блокчейнов (например, `address`, `contract_address`) должны быть в формате строк, соответствующем стандартам адресов для соответствующих блокчейнов (например, для Ethereum — строка длиной 42 символа, начинающаяся с `0x`).

#### Пример ошибки:

```json
{
  "error": {
    "code": 422,
    "message": "Invalid address format. Expected format: 0x... for Ethereum addresses."
  }
}
```


### Лимитирование Запросов
- API использует лимитирование для предотвращения злоупотреблений. Каждый пользователь может сделать до 1000 запросов в час. Если лимит превышен, будет возвращен ответ `429 Too Many Requests.`

#### Пример:

```json
{
  "error": {
    "code": 429,
    "message": "Rate limit exceeded"
  }
}
```

### Ошибки

#### 400 Bad Request
- Произошла ошибка в запросе. Обычно это связано с отсутствием обязательных параметров или неверным их форматом.

#### 401 Unauthorized
- Ошибка авторизации. Убедитесь, что вы передаете правильный API-ключ в заголовке `Authorization`.

#### 422 Unprocessable Entity
- Ошибка валидации данных. Например, если передан неправильный формат адреса.

#### 429 Too Many Requests
- Превышен лимит запросов (1000 запросов в час).

#### 500 Internal Server Error
- Ошибка на сервере. Если ошибка продолжает возникать, обратитесь в службу поддержки.


### Заключение
- Это API позволяет вам интегрироваться с DeFi Analytics Platform, анализировать данные блокчейнов, получать торговые сигналы, отслеживать смарт-контракты и взаимодействовать с децентрализованными финансовыми платформами. Вы можете легко расширять возможности платформы, - используя предоставленные эндпоинты для получения и отправки данных в реальном времени.


