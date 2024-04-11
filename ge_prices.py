from urllib.request import Request, urlopen
import json

req = Request(
    url='https://prices.runescape.wiki/api/v1/osrs/latest', 
    headers={'User-Agent': 'Price Checker - @chikaflask on discord'}

)

webpage = urlopen(req).read()
price_data = json.loads(webpage)
prices = price_data["data"]

req = Request(
    url='https://prices.runescape.wiki/api/v1/osrs/mapping', 
    headers={'User-Agent': 'Price Checker - @chikaflask on discord'}
)

webpage = urlopen(req).read()
mapping_data = json.loads(webpage)
item_info = mapping_data

def find_price(id):
    high = prices[str(id)]["high"]
    low = prices[str(id)]["low"]
    avg = (high + low)/2
    return avg

def map_item_id(name):
    for item in item_info:
        if item["name"] == str(name.capitalize()):
            return item["id"]

def query_item(name):
    item_id = map_item_id(name)
    price = find_price(item_id)
    return price


print(query_item("BLood moon tassets"))