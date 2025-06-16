from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to Our Platform!'
    message = '''
    Thank you for registering with our platform!
    
    We're excited to have you on board. You can now:
    - Access your profile
    - Connect your Telegram account
    - Use our API endpoints
    
    If you have any questions, feel free to reach out to our support team.
    
    Best regards,
    The Team
    '''
    
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    ) 