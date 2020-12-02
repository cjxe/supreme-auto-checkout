from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time, json
import requests


# Launching chrome drivers
chrome_options = Options()
#chrome_options.add_argument("--headless")  # remove the "#" at the start of the line to launch Chrome in "headless" mode.
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)


# URLs that we will be using
MAIN_URL = 'https://www.supremenewyork.com'
SHOP_URL = 'https://www.supremenewyork.com/shop'
CHECKOUT_URL = 'https://www.supremenewyork.com/checkout'
TEST_URL = 'https://www.supremenewyork.com/shop/305555'


# Defining functions
def visit_url(url):
    """Visits a url/link/webpage."""
    try:
        driver.get(url)
        print(f'[SUCCESS] Loaded "{url}".')
    except Exception as e:
        print(f'[ERROR] Website "{url}" can not be reached!.')
        print(e)


def search_item(item): # under development
    """Looks for a specific item."""
    try: 
        #req = requests.get()
        print(f'[SUCCESS] {item} found.')
    except Exception as e:
        print(f'[ERROR] {item} not found!')
        print(e)


def add_to_basket():
    """Clicks "add to basket" button when on an item's webpage."""
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="add-remove-buttons"]/input')))
        driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
        print(f'[SUCCESS] Added item to basket.')
    except Exception as e:
        print(f'[ERROR] Could not add item to basket!')
        print(e)


def checkout():
    """Clicks "checkout" button and proceeds to /checkout."""
    try: 
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[1]/div/a[2]')))
        time.sleep(0.2) # stops and waits "checkout" button to appear. This is under development
        driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]').click()
        print('[SUCCESS] Clicked "checkout now" button.')
    except Exception as e:
        print('[ERROR] Could not click "checkout now" button!')
        print(e)


def enter_shipping_info(ship_config):
    """Enters the shipping info/details of the given profile/config.

    :param ship_config: A specific "id" of which shipping configuration/profile we want to load.
    :type  ship_config: int

    :Example:

    >>> ship_config = 1
    open(f'./data/shipping/shipping_1.json')
    """
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="order_billing_name"]'))) # Waits until shipping form to get loaded.
        with open(f'./data/shipping/shipping_{ship_config}.json') as shipping_info:
            data = json.load(shipping_info)
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="order_billing_name"]'))) 
            driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(data['fullName'])
            driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(data['email'])
            driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(data['fullName'])
            driver.find_element_by_xpath('//*[@id="bo"]').send_keys(data['address_1'])
            if data['address_2'] == '':
                driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(data['address_2'])
            else:
                pass
            driver.find_element_by_xpath('//*[@id="order_billing_address_3"]').send_keys(data['address_3'])
            driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(data['city'])
            driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(data['postcode'])
            Select(driver.find_element_by_xpath('//*[@id="order_billing_country"]')).select_by_visible_text(data['country'])
        print('[SUCCESS] Entered shipping details.')
    except Exception as e:
        print('[ERROR] Could not enter shipping details!')
        print(e)


def enter_card_info(card_config):
    """Enters the card info/details of the given profile/config.

    :param card_config: A specific "id" of which card configuration/profile we want to load.
    :type  card_config: int

    :Example:

    >>> card_config = 1
    open(f'./data/shipping/card_1.json')
    """
    try: 
        with open(f'./data/card/card_{card_config}.json') as card_info:
            data = json.load(card_info)
            Select(driver.find_element_by_xpath('//*[@id="credit_card_type"]')).select_by_visible_text(data['cardType'])
            driver.find_element_by_xpath('//*[@placeholder="number"]').send_keys(data['cardNumber'])
            Select(driver.find_element_by_xpath('//*[@id="credit_card_month"]')).select_by_visible_text(data['cardMonth'])
            Select(driver.find_element_by_xpath('//*[@id="credit_card_year"]')).select_by_visible_text(data['cardYear'])
            driver.find_element_by_xpath('//*[@placeholder="CVV"]').send_keys(data['cardCVV'])
            driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()  # terms and conditions
        print('[SUCCESS] Entered card details.')
    except Exception as e:
        print('[ERROR] Could not enter card details!')
        print(e)


def process_payment():
    """Clicks "process payment" button."""
    try:
        driver.find_element_by_xpath('//*[@id="pay"]/input').click()
        print(f'[SUCCESS] Clicked "process payment" button.')
        # print(f'[SUCCESS] Paid for the item.')
        # Add error correction: Scrape data after checkout and see if it really checked out. 
    except Exception as e:
        print(f'[ERROR] Could not click "process payment" button!')
        print(e)



visit_url(SHOP_URL)
ITEM = input('Enter item "id": ') # 305555
SHIPPING_CONFIG = input('Shipping config "id": ') # 1
CARD_CONFIG = input('Card config "id": ') # 1
input("Press ENTER to start")
start_time = time.time() #Start timer 
visit_url(SHOP_URL + f'/{ITEM}')
add_to_basket()
checkout()
enter_shipping_info(SHIPPING_CONFIG)
enter_card_info(CARD_CONFIG)
#process_payment()
elapsed_time = time.time() - start_time # End timer
print(f'Total processing time: {float(round(elapsed_time,2))} seconds')


time.sleep(3000) # Wait for 50 minutes before manually closing Chrome.