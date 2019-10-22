from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://scrapingclub.com/exercise/detail_json')

r.html.render()

card_body = r.html.find('div.card-body', first = True)
title = card_body.find('card-title', first = True).text
price = card_body.find('card-price', first = True).text
desc = card_body.find('card-description', first = true).text

print('title:\t' + title)
print('price:\t' + price)
print('description:\t' + desc)