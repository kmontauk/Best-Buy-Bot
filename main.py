from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from check import totp_code
from config import *
import time
import os

is_empty = False


# Attempt to run web driver.
def init_web_driver(k):
    try:
        options = webdriver.ChromeOptions()
        # Path to your chrome profile line 18
        options.add_argument(rf'--user-data-dir={path_to_profile}')
        driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        options.add_experimental_option("detach", True)
        print('Webdriver Initialized')
    except InvalidArgumentException as error:  # Webdriver doesn't work if you have another instance of the same profile
        print(f'Tried to run but there was likely another instance of the selected profile in use. '
              f'Chrome will close in 10 seconds, and the program will rerun. {error}.')
        time.sleep(10)
        os.system('taskkill /IM "chrome.exe" /F')
        init_web_driver(k)
    check_avail(k, driver)


# Loops, checking availability/attempting purchase.
def check_avail(k, driver):
    out_of_stock = True
    while out_of_stock:
        global is_empty
        if check_cart and not is_empty:
            empty_cart(k, driver)
            is_empty = True
        print('Checking Availability...')
        driver.get(keys['product_url'])
        if driver.find_element_by_class_name("fulfillment-add-to-cart-button").text == 'Sold Out':
            print('Sold Out')
        elif driver.find_element_by_class_name("fulfillment-add-to-cart-button").text == 'Add to Cart':
            print('In Stock')
            try:       # Plays the alert if you opt to add one.
                os.startfile('alert.wav')
            except:
                pass
            if add_to_cart(k, driver):
                break
            else:
                is_empty = False
        time.sleep(refresh_rate)


# Empties the cart
def empty_cart(k, driver):
    driver.get('https://www.bestbuy.com/cart')
    time.sleep(3)
    try:
        if driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/'
                                        'div[1]/section[2]/div/div/div[3]/div/div[1]/button'):
            print('Found items in cart. Removing Items.')
            driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/'
                                         'section[1]/div[4]/ul/li/section/div[2]/div[3]/a[1]').click()
            empty_cart(k, driver)
    except NoSuchElementException:
        print('No items in cart.')
        pass


# Checks for TOTP verification. Currently scattered throughout the process as I don't know where it asks you for it.
def verify(driver):
    try:
        driver.find_element_by_id('verificationCode').send_keys(totp_code()).submit()
        return True
    except NoSuchElementException:
        print('No verification box found.')
        return False


# Add to cart
def add_to_cart(k, driver):
    try:
        print(f'Adding {k["product_url"]} to cart.')
        driver.find_element_by_class_name('fulfillment-add-to-cart-button').click()
        # driver.get('https://www.bestbuy.com/cart')   # debug line
        driver.get(k['checkout_url'])
        time.sleep(2)
        verify(driver)
        # links directly to checkout. if redirects to cart, clicks on checkout.
        if driver.current_url == 'https://www.bestbuy.com/checkout/r/fast-track':
            checkout(k, driver)
        elif driver.current_url == 'https://www.bestbuy.com/cart':
            print('BestBuy is likely redirecting to cart page. Attempting manual checkout.')
            driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/'
                                         'section[2]/div/div/div[3]/div/div[1]/button').click()
            time.sleep(2)
            verify(driver)
            time.sleep(2)
            checkout(k, driver)
        else:
            print('Something is going wrong in checkout process...')
            return False
    except NoSuchElementException as path:
        print(f'Unable to locate element: {path}')
        return False


# Attempt checkout/purchase
def checkout(k, driver):
    print('Attempting check out at checkout/r/fast-track')
    time.sleep(0)
    try:  # Sometimes (esp. if you bought something recently) Best Buy wont ask for a security code. The bot still works
        driver.find_element_by_id('credit-card-cvv').send_keys(security_code)
        print('Cvv entered')
    except NoSuchElementException:
        print('No CVV box found. Moving on.')
    verify(driver)
    if purchase:
        print('About to click purchase')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button').click()
        time.sleep(10)
        verify(driver)
    # Checks for thank you for purchase page before sleeping (so you can see the page if you're afk)
    if driver.current_url == 'https://www.bestbuy.com/checkout/r/thank-you':
        time.sleep(25000)
        quit()


if __name__ == '__main__':
    init_web_driver(keys)

# driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button').click()
