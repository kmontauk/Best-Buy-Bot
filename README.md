# Best-Buy-Bot
This is an auto-purchase bot that can buy most items on Best Buy using Selenium in Python. \
Initially, I wrote this to snag an RTX 3080 FE, however it seems that Best Buy has implemented some anti-bot measures. I have not been able to make it work for the 3080 as I haven't been able to watch the bot or catch one of the drops myself. In addition, information I could find online about their new measures was limited.\
\
I'm pretty new to github and programming in general, so any feedback, tips, or ideas are appreciated!\
\
Setup:\
  -Run install.bat to install dependencies and configure venv.\
  -Download chromedriver at https://chromedriver.chromium.org/downloads pertaining to your chrome version and place it in the same directory as main.py.\
  -Configure your Best Buy account\
  -Configure config.py to the item you want, enter your CVV/Security code, and retrieve 2fa (2 factor authentication) key from Best Buy. More on 2fa below.\
  -In config.py, enter the path to your chrome profile.\
  -In config.py, change purchase from False to True when you're done testing the bot and are ready to purchase. When set to false, it will go all the way to checkout.\
 \
 Best Buy Account:\
  -Add your address and card information\
  -Retrieve 2fa secret key in settings and input it into config.py under auth_key. Do not link 2fa to your phone, you need the key for PyOTP to generate codes directly.*\
  -If you need a code generated to verify the setup of 2fa, run check.py with generate_code set to True.\
  -Make sure you set it to remain logged in.
 
 To run the bot, run.bat.

  *This isn't necessary and may not even work, as I do not know how Best Buy is verifying purchase attempts for the 3080. However, if it does ask for 2fa given you have it set up, this should work. The code still works without a key, and will succesfully purchase other items without anti-bot measures in place. DO NOT lose the secret key. Without it, you may lose access to your Best Buy account.
