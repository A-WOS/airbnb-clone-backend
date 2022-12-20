from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'direct_messages'
    # admin 패널에서 보여지는 verbose_name 을 커스텀
    verbose_name = "Direct Messages"
