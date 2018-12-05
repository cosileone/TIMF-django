from django.shortcuts import render

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
    silvermoon = Realm.objects.filter(house=98)[1]
    random_auction = silvermoon.auctions.first()
    auction_item = random_auction.item
    recipes = auction_item.recipes.all()
    random_recipe = recipes[1]
    price = random_recipe.market_price_buyout(silvermoon)['market_cost_buyout']

    return render(request, "test.html", {
        'recipe': random_recipe,
        'price': price
    })
