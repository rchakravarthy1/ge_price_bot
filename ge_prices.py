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

def query_item(item):
    try:
        item_id = map_item_id(item)
        if item_id == None:
            return f"Item not found: **{item}**"
        price = int(find_price(item_id))
        return f'The average price of **{item}** is: **{price:,} gp**'
    except Exception as e:
        return e 

def get_response(user_input:str) ->str:
    lowered: str = user_input.lower()
    return(query_item(lowered))

# print(query_item("abyssal whip"))
# print(query_item("abyssal whp"))
