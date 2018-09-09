import json
from urllib import request
from collections import Counter

from django.db import models

from .managers import AuctionQuerySet
from items.models import Item
from realms.models import Realm


class Auction(models.Model):
    auc = models.PositiveIntegerField(primary_key=True)

    item = models.ForeignKey(
        'items.Item',
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

    def build_auctions(self):
        # the following is modeled from https://stackoverflow.com/questions/16381241/
        if self.lastchecksuccess:
            success_result = json.loads(self.lastchecksuccessresult)
            url = success_result['files'][0]['url']
            self.file_url = url
            self.save()

            # filename = parse.urlparse(url).path.split('/')[2]  # get unique blizz uuid from url string
            # print(filename)

            json_file = json.load(request.urlopen(url))
            added = 0
            skipped = Counter()
            for row in json_file['auctions']:
                added += 1
                try:
                    item = Item.objects.get(blizzard_id=row['item'])
                except Item.DoesNotExist:
                    print('{} not found'.format(row['item']))
                    skipped[row['item']] += 1
                    continue

                prepared_data = {
                    'auc': row['auc'],
                    'item': item,
                    'owner': row['owner'],
                    'ownerRealm': Realm.objects.get(name=row['ownerRealm'], house=self.house),
                    'bid': row['bid'],
                    'buyout': row['buyout'],
                    'quantity': row['quantity'],
                    'timeLeft': row['timeLeft'],
                }

                auction = Auction(**prepared_data)
                auction.save()

            print('{} auctions added'.format(added))

            for item_id, skips in skipped.items():
                print('ID {} skipped {} times'.format(item_id, skips))



# class AuctionHouse(models.Model):
#     realm = models.ForeignKey()
#
#     # @property
#     # def latest(self):
