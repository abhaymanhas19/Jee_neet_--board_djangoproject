from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def send_passwod(email, password):
    try:
        subject = "Your account login Password"
        message = f"your Otp is {password}"
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
        print("Done")
    except Exception as e:
        print(e)
