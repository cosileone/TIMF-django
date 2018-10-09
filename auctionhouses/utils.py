import wowapi
import urllib
import json
import time
from datetime import datetime
import os
import glob

from instance.config import blizz_key


blizzapi = wowapi.API(blizz_key)


class AuctionHouse(object):
    def __init__(self, region='US', server='malganis', download_data=False):
        self.region = region
        self.server = server
        self.data = self.get_data(download_data)
        blizzapi.region = region

    def get_data(self, save_file=False):
        # average update interval in minutes - https://theunderminejournal.com/dataintervals.php
        interval = 21 if self.region == 'EU' else 119

        latest_file = self.get_latest_file()

        if latest_file and self.is_fresh_data(latest_file, interval):
            auction_data = self.read_json_from_disk(latest_file)
            print(latest_file)
        else:
            auction_file = blizzapi.auction_status(self.server)
            data_url = auction_file['files'][0]['url']
            response = urllib.urlopen(data_url)
            auction_data = json.load(response)

            if save_file:
                self.save_json_to_disk(auction_data)
            print(data_url)

        return auction_data

    def is_fresh_data(self, filepath, threshold):
        # TODO: check Blizz AH URL instead of filename for freshness
        now = datetime.now()

        dirname = "./timf/auctions/data/{0}-{1}/".format(self.server, self.region)
        filename = filepath.replace(dirname, "")
        timestr = filename.replace(".json", "")
        filedate = datetime.strptime(timestr, "%Y.%m.%d-%H%M%S")

        time_diff = now - filedate
        fresh = (time_diff.seconds / 60) <= threshold

        return fresh

    def get_latest_file(self):
        # TODO: Make this directory a config constant?
        dirname = "./timf/auctions/data/{0}-{1}/".format(self.server, self.region)
        file_list = glob.glob(dirname + "*.json")
        if file_list:
            latest = max(file_list, key=os.path.getctime)
            return latest
        else:
            return None

    def read_json_from_disk(self, filepath):
        with open(filepath) as json_file:
            auction_data = json.load(json_file)

        return auction_data

    def save_json_to_disk(self, json_data):
        timestr = time.strftime("%Y.%m.%d-%H%M%S")
        dirname = "./timf/auctions/data/{0}-{1}/".format(self.server, self.region)
        filename = dirname + ("{}.json".format(timestr))

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(filename, 'w') as outfile:
            json.dump(json_data, outfile, sort_keys=True, indent=4)

        return timestr

    def filter_by_item_ids(self, item_ids):
        results = []
        for auction in self.data['auctions']:
            if auction['item'] in item_ids:
                results.append(auction)

        return results

    def calcStats(self, item_ids):
        total_quantity = 0
        total_volume = 0
        mean_buyout = 0
        min_buyout = 0

        filtered_ah = self.filter_by_item_ids(item_ids)
        num_listings = len(filtered_ah)

        if num_listings > 0:
            min_bid = filtered_ah[0]['bid']

            for auction in filtered_ah:
                bid = auction['bid']
                quantity = auction['quantity']
                buyout = auction['buyout']
                if min_buyout == 0 and not buyout == 0:
                    min_buyout = buyout

                min_buyout = min(min_buyout, (buyout / quantity))
                min_bid = min(min_bid, (bid / quantity))

                total_quantity += quantity
                total_volume += buyout

            mean_buyout = total_volume / total_quantity
        else:
            min_bid = 0

        results = {
            'auctions': num_listings,
            'total_quantity': total_quantity,
            'total_volume': float("{0:.4f}".format(total_volume/10000)),
            'mean_buyout': float("{0:.4f}".format(mean_buyout/10000)),
            'cheapest_buyout': float("{0:.4f}".format(min_buyout/10000)),
            'cheapest_bid': float("{0:.4f}".format(min_bid/10000))
        }

        return results

def median_value(queryset, term):
    count = queryset.count()
    values = queryset.values_list(term, flat=True).order_by(term)
    if count % 2 == 1:
        return values[int(round(count / 2))]
    else:
        return sum(values[count // 2 - 1:count // 2 + 1]) / 2  # Python 3 does floating-point division
