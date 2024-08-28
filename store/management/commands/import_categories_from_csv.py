import csv

from django.core.management.base import BaseCommand, CommandError
from store.models import Category
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    help = 'Storing objects from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument("CSV_path", nargs="+", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Importing categories")

        csv_path = options['CSV_path'][0]

        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)

                for row in reader:
                    if not row:
                        continue

                    level1_title = row[0].strip()
                    level2_title = row[1].strip()
                    level3_title = row[2].strip()
                    level4_title = row[3].strip()

                    level1_category, created = Category.objects.get_or_create(
                        title=level1_title,
                        parent=None
                    )

                    level2_category, created = Category.objects.get_or_create(
                        title=level2_title,
                        parent=level1_category
                    )

                    level3_category, created = Category.objects.get_or_create(
                        title=level3_title,
                        parent=level2_category
                    )
                    if level4_title:
                        level4_category, created = Category.objects.get_or_create(
                            title=level4_title,
                            parent=level3_category
                        )

                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully processed categories: "{level1_title}" -> "{level2_title}" -> "{level3_title}" -> "{level4_title}"'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(
                f'File "{csv_path}" does not exist.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
