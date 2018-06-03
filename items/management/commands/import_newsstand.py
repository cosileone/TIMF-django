from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from items.models import Item
from newsstand.models import Tbldbcitem


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

        local_items = list(
            Item.objects.exclude(
                blizzard_id__isnull=True
            ).values_list(
                'blizzard_id',
                flat=True
            ).using('default'))

        if local_items:
            new_items = Tbldbcitem.objects.exclude(pk__in=local_items).using('newsstand')
            count = new_items.count()

            with transaction.atomic():
                if count > 0 and not dry_run:
                    for item in new_items:
                        new_item = Item()
                        new_item.blizzard_id = item.id
                        new_item.name = item.name
                        new_item.quality = item.quality
                        new_item.level = item.level
                        new_item.item_class = item.class_field
                        new_item.subclass = item.subclass
                        new_item.icon = item.icon
                        new_item.stacksize = item.stacksize
                        new_item.buyfromvendor = item.buyfromvendor
                        new_item.selltovendor = item.selltovendor
                        new_item.auctionable = item.auctionable
                        new_item.type = item.type
                        new_item.requiredlevel = item.requiredlevel
                        new_item.requiredskill = item.requiredskill
                        new_item.save()
                else:
                    self.stdout.write("Number of new items: {}".format(count))
