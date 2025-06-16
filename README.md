# Django Internship Assignment

This project demonstrates a Django application with Django REST Framework, authentication, Celery, and Telegram bot integration.

## Features

- User registration and authentication using Token Authentication
- Protected and public API endpoints
- Celery integration with Redis for background tasks
- Telegram bot integration for user registration
- Email notifications using Celery tasks

## Prerequisites

- Python 3.8+
- Redis server
- Telegram Bot Token (from BotFather)

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
REDIS_URL=redis://localhost:6379/0
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start Redis server:
```bash
redis-server
```

2. Start Celery worker:
```bash
celery -A backend worker -l info
```

3. Start the Django development server:
```bash
python manage.py runserver
```

4. Start the Telegram bot:
```bash
python manage.py runbot
```

## API Endpoints

### Public Endpoints
- `POST /api/register/` - Register a new user
  - Required fields: username, password, password2, email

### Protected Endpoints
- `GET/PUT /api/profile/` - Get or update user profile
  - Requires authentication token

## Telegram Bot Commands

- `/start` - Start the bot and register a new user

## Testing

Run the test suite:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 