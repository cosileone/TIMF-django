import json
import requests
import time
from collections import Counter

from django.db import models, transaction

from .managers import AuctionQuerySet
from items.models import Item
from realms.models import Realm


class Auction(models.Model):
    auc = models.PositiveIntegerField(primary_key=True)

    item = models.ForeignKey(
        'items.Item',
        related_name='auctions',
        on_delete=models.PROTECT,
        help_text='The Item being sold'
    )

    owner = models.CharField(
        max_length=32,
        help_text='The Character that listed this Auction'
    )

    ownerRealm = models.ForeignKey(
        'realms.Realm',
        related_name='auctions',
        on_delete=models.PROTECT,
        help_text='The Realm on which this Auction is listed on.'
    )

    bid = models.PositiveIntegerField()
    buyout = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()

    TIMELEFT_CHOICES = [
        ('Very Long', 'VERY_LONG'),
        ('Long', 'LONG'),
        ('Short', 'SHORT')
    ]

    timeLeft = models.CharField(
        max_length=16,
        choices=TIMELEFT_CHOICES
    )

    objects = AuctionQuerySet.as_manager()

    def __str__(self):
        return '{}x[{}] {}/{}'.format(self.quantity, self.item, self.bid, self.buyout)


class AuctionData(models.Model):
    house = models.PositiveSmallIntegerField(primary_key=True)
    nextcheck = models.DateTimeField(blank=True, null=True)
    lastdaily = models.DateField(blank=True, null=True)
    lastcheck = models.DateTimeField(blank=True, null=True)
    lastcheckresult = models.TextField(blank=True, null=True)
    lastchecksuccess = models.DateTimeField(blank=True, null=True)
    lastchecksuccessresult = models.TextField(blank=True, null=True)

    file_url = models.URLField(null=True, blank=True)

    @transaction.atomic
    def build_auctions(self, region):
        # the following is modeled from https://stackoverflow.com/questions/16381241/
        if self.lastchecksuccess:
            success_result = json.loads(self.lastchecksuccessresult)
            url = success_result['files'][0]['url']

            if self.file_url != url:
                self.file_url = url
                self.save()

                # filename = parse.urlparse(url).path.split('/')[2]  # get unique blizz uuid from url string
                # print(filename)

                download_start = time.clock()
                json_file = requests.get(url).json()
                print("Downloaded in {} seconds".format(time.clock()-download_start))

                added = 0
                skipped = Counter()
                auctions = []
                collection_start = time.clock()
                for row in json_file['auctions']:
                    added += 1
                    try:
                        item = Item.objects.get(blizzard_id=row['item'])
                    except Item.DoesNotExist:
                        print('Item {} not found'.format(row['item']))
                        skipped[row['item']] += 1
                        continue

                    if not Auction.objects.filter(auc=row['auc']).exists():
                        auctions.append(self._import_auction(row, item, region))

                print("Collection finished in {} seconds".format(time.clock() - collection_start))

                bulk_insertion_start = time.clock()
                Auction.objects.bulk_create(auctions, batch_size=500)  # SQLite max insertion is 999?
                print("Insertion finished in {} seconds".format(time.clock() - bulk_insertion_start))

                for item_id, skips in skipped.items():
                    print('ID {} skipped {} times'.format(item_id, skips))

                print('{} auctions added'.format(added))

    def _import_auction(self, auction_data, blizz_item, region):
        auction = Auction(
            auc=auction_data['auc'],
            item=blizz_item,
            owner=auction_data['owner'],
            ownerRealm=Realm.objects.get(name=auction_data['ownerRealm'], region=region),
            bid=auction_data['bid'],
            buyout=auction_data['buyout'],
            quantity=auction_data['quantity'],
            timeLeft=auction_data['timeLeft'],
        )
        return auction

# class AuctionHouse(models.Model):
#     realm = models.ForeignKey()
#
#     # @property
#     # def latest(self):
