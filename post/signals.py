from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------------------------\n user login signal")
    print('sender ', sender)
    print('request ', request)
    print('user ', user)


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("----------------------------\n user logout signal")
    print('sender ', sender)
    print('request ', request)
    print('user ', user)

@receiver(user_login_failed)
def login_failed(sender, request, **kwargs):
    print("----------------------------\n user login failed signal")
    print('sender ', sender)
    print('request ', request)