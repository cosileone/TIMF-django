from django.db import models

from .managers import AuctionQuerySet


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

    rand = models.IntegerField()
    seed = models.IntegerField()
    context = models.IntegerField()

    bonusLists = models.CharField(
        max_length=256
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


# class AuctionHouse(models.Model):
#     realm = models.ForeignKey()
#
#     # @property
#     # def latest(self):
