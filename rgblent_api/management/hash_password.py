from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'hashes plaintext password(s)'

    def add_arguments(self, parser):
        parser.add_argument('plaintext', nargs='+', type=str)

    def handle(self, *args, **options):
        for plaintext in 
