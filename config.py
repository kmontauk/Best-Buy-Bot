# Wordwrap off.

# Input your auth key for PyOtp. You can also test with different products by changing the product url.
keys = {
    'product_url':
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    # 'https://www.bestbuy.com/site/wd-wd_black-sn750-nvme-1tb-internal-pci-express-3-0-x4-solid-state-drive-for-laptops-desktops/6338995.p?skuId=6338995',
    # 'https://www.bestbuy.com/site/insignia-6-3-5mm-audio-cable-black/5019219.p?skuId=5019219',
    # 'https://www.bestbuy.com/site/microsoft-controller-for-xbox-series-x-xbox-series-s-and-xbox-one-latest-model-shock-blue/6430660.p?skuId=6430660',
    'checkout_url': 'https://www.bestbuy.com/checkout/r/fast-track',
    'auth_key': '',
}

# Change this if you want the bot to empty your cart before attempting to purchase.
# Useful if it's running autonomously, as you may not want 2+ items if an error occurs on checkout. True to check cart.
check_cart = True

# Use this if you want to test the bot without purchasing product. True to purchase, false to test.
purchase = False

# Your security code.
security_code = ''

# Refresh rate for checking stock
refresh_rate = 6

