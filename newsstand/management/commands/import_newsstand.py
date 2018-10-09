import json
import time

from django.core.management.base import BaseCommand
from django.db import connections

from newsstand.models import Tbldbcitem, Tblrealm, Tblhousecheck, Tbldbcspell, Tbldbcspellcrafts
from auctionhouses.models import AuctionData
from items.models import Item
from realms.models import Realm
from recipes.models import Recipe, Ingredient


def fetchsome(cursor, array_size=1000):
    """ A generator that simplifies the use of fetchmany """
    while True:
        results = cursor.fetchmany(array_size)
        if not results:
            break
        for result in results:
            yield result


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
        parser.add_argument(
            '--auctions-only',
            action='store_true',
            dest='auctions-only',
            help="Only save auctions from newsstand DB",
        )

    def handle(self, *args, **options):
        # TODO: Handle option to force update existing items as well
        dry_run = options.get('dry-run')
        auctions_only = options.get('auctions-only')

        if not auctions_only:
            self.stdout.write("Copying Items...")
            self.get_items(dry_run)

            self.stdout.write("Copying Realms...")
            self.get_realms(dry_run)

            self.stdout.write("Copying Recipes...")
            self.get_recipes(dry_run)

            self.stdout.write("Copying Ingredients...")
            self.get_ingredients(dry_run)
        else:
            self.stdout.write("Copying Auction House Checks...")
            self.get_auctionhouse_checks(dry_run)

    def get_realms(self, dry_run=True):
        supported_regions = ['US', 'EU']
        # local_data = list(
        #     Realm.objects.filter(
        #         region__in=supported_regions
        #     ).values_list(
        #         'slug',
        #         flat=True
        #     )
        # )
        newsstand_data = Tblrealm.objects.filter(region__in=supported_regions)#.exclude(slug__in=local_data)

        if not dry_run:
            for realm in newsstand_data:
                new_realm, _ = Realm.objects.update_or_create(
                    slug=realm.slug,
                    region=realm.region,
                    defaults={
                        'slug': realm.slug,
                        'name': realm.name,
                        'region': realm.region,
                        'house': realm.house,
                        'population': realm.population
                    }
                )
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

    def get_recipes(self, dry_run=True):
        local_spells = list(Recipe.objects.exclude(
            blizzard_id__isnull=True
        ).values_list(
            'blizzard_id',
            flat=True
        ))

        spells = Tbldbcspell.objects.filter(skillline__isnull=False).exclude(pk__in=local_spells)

        if not dry_run:
            for spell in spells:
                new_spell, created = Recipe.objects.update_or_create(
                    blizzard_id=spell.id,
                    defaults={
                        "blizzard_id": spell.id,
                        "name": spell.name,
                        "description": spell.description,
                        "cooldown": spell.cooldown,
                        "skillline": spell.skillline,
                        "qtymade": spell.qtymade,
                        "expansion": spell.expansion,
                    }
                )
                try:
                    crafted_id = Tbldbcspellcrafts.objects.get(spell=spell.pk)
                    crafted_item = Item.objects.get(blizzard_id=crafted_id.item)
                    new_spell.crafteditem = crafted_item
                except Tbldbcspellcrafts.DoesNotExist:
                    self.stdout.write('Crafted Item with spell {} not found'.format(spell.pk))
                    continue
                except Item.DoesNotExist:
                    self.stdout.write('Item {} not found'.format(crafted_id.item))
                    continue

                new_spell.save()
        else:
            self.stdout.write("Number of spells: {}".format(spells.count()))

    def get_ingredients(self, dry_run=True):
        with connections['newsstand'].cursor() as cursor:
            if not dry_run:
                cursor.execute('SELECT item, skillline, reagent, quantity, spell FROM newsstand.tblDBCItemReagents')
                columns = [col[0] for col in cursor.description]

                for row in fetchsome(cursor):
                    ingredient = dict(zip(columns, row))

                    try:
                        crafted_item = Item.objects.get(blizzard_id=ingredient['item'])
                        recipe_spell = Recipe.objects.get(blizzard_id=ingredient['spell'])
                    except Item.DoesNotExist:
                        self.stdout.write('Item {} not found'.format(ingredient['spell']))
                        continue
                    except Recipe.DoesNotExist:
                        self.stdout.write('Recipe {} not found'.format(ingredient['spell']))
                        continue

                    try:
                        ingredient_reagent = Item.objects.get(blizzard_id=ingredient['reagent'])
                    except Item.DoesNotExist:
                        self.stdout.write('Reagent {} not found'.format(ingredient['spell']))
                        continue

                    if Ingredient.objects.filter(reagent=ingredient_reagent, spell=recipe_spell).exists():
                        continue
                    else:
                        new_ingredient = Ingredient()
                        new_ingredient.item = crafted_item
                        new_ingredient.skillline = ingredient['skillline']
                        new_ingredient.reagent = ingredient_reagent
                        new_ingredient.quantity = ingredient['quantity']
                        new_ingredient.spell = recipe_spell

                        new_ingredient.save()
            else:
                self.stdout.write("Skipping Ingredients")

    def get_auctionhouse_checks(self, dry_run=True):
        house_checks = Tblhousecheck.objects.all()
        count = house_checks.count()

        if not dry_run:
            start = time.clock()
            house = 0
            for row in house_checks[94:95]:
                house = row.house
                new_data, created = AuctionData.objects.update_or_create(house=row.house, defaults={
                    'house': row.house,
                    'nextcheck': row.nextcheck,
                    'lastdaily': row.lastdaily,
                    'lastcheck': row.lastcheck,
                    'lastcheckresult': row.lastcheckresult,
                    'lastchecksuccess': row.lastchecksuccess,
                    'lastchecksuccessresult': row.lastchecksuccessresult,
                })
                success_result = json.loads(new_data.lastchecksuccessresult)
                region = 'US' if 'auction-api-us' in success_result['files'][0]['url'] else 'EU'
                new_data.save()
                new_data.build_auctions(region)
            self.stdout.write("House {} auctions saved in {} seconds".format(house, time.clock()-start))
        else:
            self.stdout.write("Number of new auctionhouse checks: {}".format(count))


