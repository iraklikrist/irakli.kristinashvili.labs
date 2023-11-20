from scrapy.http import TextResponse
import requests
import pprint
import re

url = requests.get(
    "https://place.ge/en/ads/page:1?object_type=flat&order_by=date&currency_id=1&city_id=1&mode=list&limit=200")
res = TextResponse(url.url, body=url.text, encoding='utf-8')
all = res.css(".infoFilter")

data = []
filter_data = ["", "urgently", "FOR RENT", "FOR SALE", "Like", "Estimate", "Price: ", "on credit:", " – ", " ",
               "SHORT TERM RENT"]
counter = 1
real_data = []

for e in all:
    data.append(e.css(":not(a)::text").getall())

for e in data:
    dt = []
    for each in e:
        each = re.sub(r'[\n\t]', '', each)
        if "tel" in each:
            each = ""
        if "month" in each:
            each = ""
        if each not in filter_data:
            each = each.replace(",", "")
            each = each.replace("tel: ", "")
            dt.append(each)
    print(dt)

    real_data.append(dt)
    dt.clear()
