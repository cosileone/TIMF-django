from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from newsstand.models import Tbldbcitem, Tblrealm
from items.models import Item
from realms.models import Realm


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
        # TODO: Handle option to force update existing items as well
        dry_run = options.get('dry-run')

        self.stdout.write("Copying Items...")
        self.get_items(dry_run)

        self.stdout.write("Copying Realms...")
        self.get_realms(dry_run)

    def get_realms(self, dry_run):
        supported_regions = ['US', 'EU']
        local_data = list(
            Realm.objects.filter(
                region__in=supported_regions
            ).values_list(
                'slug',
                flat=True
            )
        )
        newsstand_data = Tblrealm.objects.filter(region__in=supported_regions).exclude(slug__in=local_data)

        if newsstand_data != local_data and not dry_run:
            with transaction.atomic():
                for realm in newsstand_data:
                    new_realm = Realm()
                    new_realm.name = realm.name
                    new_realm.region = realm.region
                    new_realm.slug = realm.slug
                    new_realm.house = realm.house
                    new_realm.population = realm.population
                    new_realm.save()
        else:
            self.stdout.write("Number of new items: {}".format(newsstand_data.count()))

    def get_items(self, dry_run):
        local_items = list(
            Item.objects.exclude(
                blizzard_id__isnull=True
            ).values_list(
                'blizzard_id',
                flat=True
            ).using('default'))

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
