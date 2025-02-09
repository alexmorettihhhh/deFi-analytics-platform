# DeFi Analytics Platform

**DeFi Analytics Platform** - это система для мониторинга и анализа данных с децентрализованных бирж (DEX), предназначенная для трейдеров и аналитиков в области DeFi. Платформа предоставляет API для получения транзакций и ценовых данных с блокчейн-платформ и отображает их на панели мониторинга, с возможностью получения уведомлений о торговых сигналах. Проект использует лучшие практики безопасности и оптимизации для работы с большими объемами данных.

## Настройка новых функций бота:

1. **Автоматические уведомления**:
   - Бот настроен на отправку торговых сигналов каждые 10 минут. Вы можете изменить частоту уведомлений, настроив параметр в `apscheduler`.

2. **Работа с кнопками**:
   - Используйте команду `/buttons`, чтобы увидеть доступные кнопки для выбора действий в боте. Эти кнопки позволяют пользователям легко получать торговые сигналы или информацию о статусе торгов.

3. **Обработка сообщений**:
   - Бот также может отвечать на любые текстовые сообщения от пользователей, чтобы предоставить им нужную информацию или дополнительные сигналы.


## Основные особенности:
- **Аутентификация с JWT** для безопасной авторизации и аутентификации пользователей.
- **Интеграция с DeFi сервисами**: Подключение к Uniswap, Sushiswap, PancakeSwap и другим для получения данных о торговых парах.
- **Аналитика и отчеты**: Генерация отчетов с торговыми данными, включая объемы и тренды.
- **WebSocket API**: Получение данных в реальном времени.
- **Обработка торговых сигналов** через Telegram или Email.
- **Использование Celery** для асинхронной обработки больших объемов данных.
- **Защита от избыточных запросов (Rate Limiting)** для предотвращения DDoS-атак.
- **SSL для защиты данных** через HTTPS.
- 
## Стек технологий:
- **Python 3.6+**
- **FastAPI**: Для создания RESTful API.
- **JWT**: Для аутентификации и авторизации.
- **SQLAlchemy**: Для работы с базой данных.
- **Redis**: Для кэширования данных.
- **Celery**: Для обработки асинхронных задач.
- **Web3.py**: Для работы с блокчейн-API.
- **PostgreSQL**: Для хранения данных о транзакциях.
- **Clickhouse**: Для аналитики и обработки больших объемов данных.
- **Docker**: Для контейнеризации и деплоя.
- **WSL2**: Для работы с Linux-дистрибуциями на Windows.

## Установка и запуск

1. Клонируйте репозиторий:
 ```
git clone https://github.com/yourusername/deFi-analytics-platform.git
 ```

**Перейдите в директорию проекта:**
 ```bash
cd deFi-analytics-platform
 ```

**Создайте файл .env в корневой папке проекта и добавьте в него ваши секретные ключи и данные для подключения к базе данных:**
```bash
SECRET_KEY=your-generated-secret-key
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_DB=defi
 ```

**Установите все зависимости:**
 ```bash
pip install -r requirements.txt
 ```
**Для запуска Docker-контейнеров используйте:**
 ```bash
docker-compose up --build
 ```
**После этого приложение будет доступно по адресу:**
 ```bash
http://localhost:8000
 ```

##  API
- **1. POST /register - Регистрация нового пользователя.
- **2. POST /login - Логин пользователя и получение JWT токена.
- **3. GET /reports/{pair} - Генерация отчетов для указанного торгового Pair (например, ETH-USDT).
- **4. WebSocket /ws/{pair} - Получение данных о торговом Pair в реальном времени.
- **5. POST /signals - Отправка торговых сигналов на Email или Telegram.

## API Documentation
Подробную документацию по API можно найти в файле [API_DOC.md](./API_DOC.md).


## Примечания
- Для получения данных о транзакциях используется интеграция с внешними блокчейн-сервисами (например, Uniswap).
- Уведомления о торговых сигналах могут быть настроены через Telegram или Email API.
- Проект контейнеризован с помощью Docker для удобства деплоя и управления зависимостями.


### Дополнительные рекомендации:
- Убедитесь, что вы обновили все ключевые данные, такие как `SECRET_KEY`, учетные данные для базы данных и прочее, в `.env` файле перед запуском.

## Лицензия
Этот проект использует лицензию MIT. Подробности см. в файле LICENSE.

