from django.core.management.base import BaseCommand
from django.db import transaction

from newsstand.models import Tbldbcitem, Tblrealm, Tblhousecheck
from auctionhouses.models import AuctionData
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

        self.stdout.write("Copying Auction House Checks...")
        self.get_auctionhouse_checks(dry_run)

    def get_realms(self, dry_run=True):
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

        if not dry_run:
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

    def get_items(self, dry_run=True):
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
                    new_item, created = Item.objects.update_or_create(
                        blizzard_id=item.pk,
                        defaults={
                            "blizzard_id": item.id,
                            "name": item.name,
                            "quality": item.quality,
                            "level": item.level,
                            "item_class": item.class_field,
                            "subclass": item.subclass,
                            "icon": item.icon,
                            "stacksize": item.stacksize,
                            "buyfromvendor": item.buyfromvendor,
                            "selltovendor": item.selltovendor,
                            "auctionable": item.auctionable,
                            "type": item.type,
                            "requiredlevel": item.requiredlevel,
                            "requiredskill": item.requiredskill
                        }
                    )
                    new_item.save()
            else:
                self.stdout.write("Number of new items: {}".format(count))

    def get_auctionhouse_checks(self, dry_run=True):
        house_checks = Tblhousecheck.objects.all()
        count = house_checks.count()

        with transaction.atomic():
            if not dry_run:
                for row in house_checks:
                    new_data, created = AuctionData.objects.update_or_create(house=row.house, defaults={
                        'house': row.house,
                        'nextcheck': row.nextcheck,
                        'lastdaily': row.lastdaily,
                        'lastcheck': row.lastcheck,
                        'lastcheckresult': row.lastcheckresult,
                        'lastchecksuccess': row.lastchecksuccess,
                        'lastchecksuccessresult': row.lastchecksuccessresult,
                    })
            else:
                self.stdout.write("Number of new auctionhouse checks: {}".format(count))


