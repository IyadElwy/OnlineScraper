from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from lxml import etree
from MainPortal.models import Settings, Product


def notify_by_email():
    pass


def nike_scraper(product: Product):
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.82 Safari/537.36'})

    webpage = requests.get(product.url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    dom = etree.HTML(str(soup))
    print(dom.xpath("//form[@id='buyTools']/div/div/div/button")[0].text)


def update_something():
    products = Product.objects.filter(is_available=False, is_purchased=False)
    for product in products:
        if product.website.name == 'Nike':
            nike_scraper(product)


def start():
    interval = int(Settings.objects.filter(p=1)[0].checking_interval) * 60
    if interval is None:
        interval = 300

    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', seconds=10)
    scheduler.start()
