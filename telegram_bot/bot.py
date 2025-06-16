import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from django.conf import settings
from .models import TelegramUser
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    chat_id = str(update.effective_chat.id)
    username = update.effective_user.username
    
    # Check if user already exists
    telegram_user = TelegramUser.objects.filter(chat_id=chat_id).first()
    
    if telegram_user:
        await update.message.reply_text(
            f"Welcome back, {username}! You're already registered."
        )
        return
    
    # Create new Telegram user
    try:
        user = User.objects.create_user(
            username=f"telegram_{username}",
            password=User.objects.make_random_password(),
            telegram_username=username
        )
        
        TelegramUser.objects.create(
            user=user,
            chat_id=chat_id,
            username=username
        )
        
        await update.message.reply_text(
            f"Welcome {username}! Your account has been created successfully."
        )
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        await update.message.reply_text(
            "Sorry, there was an error creating your account. Please try again later."
        )

def setup_bot():
    """Setup the bot with command handlers."""
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    
    return application 