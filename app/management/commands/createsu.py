from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="",
                password="admin"
            )
            self.stdout.write("Superuser created: admin / admin")
        else:
            self.stdout.write("Superuser 'admin' already exists")
