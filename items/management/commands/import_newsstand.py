from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from items.models import Item


class Command(BaseCommand):
    help = 'Saves any new items found in Newsstand DB to local DB'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--dry-run',
            action='store_true',
            dest='dry-run',
            help="Don't save any new items found from newsstand DB",
        )

    def handle(self, *args, **options):
        dry_run = options.get('dry-run')

        local_items = Item.objects.filter(blizzard_id__isnull=False)
        new_items = Item.objects.exclude(pk__in=local_items).using('newsstand')
        count = new_items.count()

        self.stdout.write(count)
        with transaction.atomic():
            if count > 0 and not dry_run:
                for item in new_items:
                    new_item = item
                    new_item.pk = None
                    new_item.save(using='default')

