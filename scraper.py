import threading
from apscheduler.schedulers.background import BackgroundScheduler
from MainPortal.models import Settings, Product
from playwright.sync_api import sync_playwright
import sendgrid
from django.conf import settings


def notify_by_email(product: Product):
    message = sendgrid.Mail(
        from_email='iyadelwy2@gmail.com',
        to_emails='iyadelwy@gmail.com',
        subject=f'{product.name}',
        html_content='<h1>Product available</h1>'
                     f'<h2>Product {product.name} available</h2>'
                     f'<h2>Check it out at {product.url}</h2>')
    try:
        sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)


def change_product_status(chosen_product: Product):
    Product.objects.filter(name=chosen_product.name).update(is_available=True)


def nike_scraper(product: Product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(product.url)
        check_out_box = page.locator('text=In den Warenkorb').first.text_content()
        if check_out_box.strip() == 'In den Warenkorb':
            x = threading.Thread(target=change_product_status, args=(product,))
            x.start()
            x.join()
            x = threading.Thread(target=notify_by_email, args=(product,))
            x.start()
            x.join()


def update_something():
    products = Product.objects.filter(is_available=False, is_purchased=False)
    for product in products:
        if product.website.name == 'Nike' and product.is_available is False and product.is_purchased is False:
            nike_scraper(product)


def start():
    interval = int(Settings.objects.filter(p=1)[0].checking_interval) * 60
    if interval is None:
        interval = 300

    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', seconds=interval)
    scheduler.start()
