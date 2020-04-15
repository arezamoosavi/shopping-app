from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'number of products and orders on how many users.'


    def handle(self, *args, **options):
        print("HIIIIII and Welcome")