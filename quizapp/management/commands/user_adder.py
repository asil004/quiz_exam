from django.core.management import BaseCommand
from pathlib import Path
from django.contrib.auth import get_user_model

User = get_user_model()
BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent) + '/import_files/'


class Command(BaseCommand):
    help = "Add users"

    def add_arguments(self, parser):
        parser.add_argument('user', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(BASE_DIR + 'users.txt') as file:
            content = file.readlines()
            for i in content:
                line = i.strip().split(' ')
                name = line[0]
                last_name = line[1]
                full_name = line[2]
                user_gmail = line[3]
                username = line[4]
                User.objects.create(first_name=name, last_name=last_name, email=user_gmail,
                                    username=username)

        self.stdout.write(self.style.SUCCESS('Successfully added'))
