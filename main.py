import requests
from bs4 import BeautifulSoup
import re
import json

respons = requests.get("https://www.ceneo.pl/91715703#tab=reviews")

page_dom = BeautifulSoup(respons.text, 'html.parser')


opinions = page_dom.select("div.js_product-review").pop(0)

all_opinions = []

for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
    try:
        recommendation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
        recommendation = True if recommendation=="Polecam" else False
    except IndexError:
        recommendation = None
    stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
    stars = float(stars.split("/")[0].replace(",","."))
    content = opinion.select("div.user-post__text").pop(0).get_text().strip()
    content = content.replace("\n"," ").replace("\r"," ")
    content = re.sub("\\s"," ",content)
    "\\s"
    pros = opinion.select("div.review-feature__col:has(> div[class$='positives']) > div.review-feature__item").pop(0).get_text().strip()
    pros = [item.get_text().strip() for item in pros]
    cons = opinion.select("div.review-feature__col:has(> div[class$='negatives']) > div.review-feature__item").pop(0).get_text().strip()
    try:
        verified = bool(opinion.select("div.rewiev-pz").pop(0).get_text().strip())
    except IndexError:
        verified = None
    post_date = opinion.select("span.user-post__published > time:nth-child(1)['datetime']").pop(0).get_text().strip()
    try:
        purchase_date = opinion.select("span.user-post__published > time:nth-child(2)['datetime']").pop(0).get_text().strip()
    except IndexError:
        purchase_date = None
    usefulness = int(opinion.select("span[id^='votes-yes']").pop(0).get_text().strip())
    uselessness = int(opinion.select("span[id^='votes-no']").pop(0).get_text().strip())

    single_opinion = {
        "opinion_id":opinion_id,
        "author":author,
        "recommendation":recommendation,
        "stars":stars,
        "content":content,
        "pros":pros,
        "cons":cons,
        "verified":verified,
        "post_date":post_date,
        "purchase_date":purchase_date,
        "usefulness":usefulness,
        "uselessness":uselessness,
    }

    all_opinions.append(single_opinion)


print(json.dumps(all_opinions, ensure_ascii=False, indent=4))
   