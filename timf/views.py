from django.shortcuts import render
from django.db.models import Min

from realms.models import Realm


def index(request):
    """
    Homepage
    """
    return render(request, "index.html")


def test(request):
    """
    Test page for testing querysets
    """
    realm = Realm.objects.filter(house=92)[0]
    shuffled_auctions = realm.auctions.all().order_by('?')
    for auction in shuffled_auctions:
        recipes = auction.item.recipes.all()
        if recipes:
            random_recipe = recipes[0]
            break
    # random_auction = realm.auctions.all().order_by('?')[counter]

    market_stats = random_recipe.market_stats(realm)
    min_auction = market_stats.order_by('buyout_min')[0]
    min_buyout = min_auction.buyout_min / min_auction.quantity
    avg_price = random_recipe.market_avg_buyout(realm)['market_avg_buyout']

    return render(request, "test.html", {
        'recipe': random_recipe,
        'min_buyout': min_buyout,
        'average': avg_price
    })
