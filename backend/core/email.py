from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


User = get_user_model()


def send_contact_email_message(subject, name, email, content, ip, user_id):
    """
    Function to send contact form email
    """
    user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string('core/includes/feedback_email_send.html', {
        'email': email,
        'name': name,
        'content': content,
        'ip': ip,
        'user': user,
    })
    email = EmailMessage(
        subject, message, settings.EMAIL_SERVER, [settings.EMAIL_ADMIN]
    )
    email.send(fail_silently=False)
    