from django.dispatch import Signal

saved = Signal(providing_args=["user", "table", "name", "header"])


