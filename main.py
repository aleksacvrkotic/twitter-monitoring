import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Define the accounts to monitor
accounts = ['JeffGordonWeb', 'PixelArtJourney', 'minireview_io']

# Configuring the driver
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode without opening a browser window
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

webdriver_path = 'C:/Program Files (x86)/chromedriver.exe'  # Replace with the path to your ChromeDriver executable

def monitor_tweets(account):
    driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
    # Getting the url for the specific account
    profile_url = f'https://twitter.com/{account}'
    driver.get(profile_url)
    # Getting the last tweet posted so it can be compared if the new tweet is spoted
    last_tweet = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetText']"))).text
    while True:
        try:
            # Driver needs to refresh the page because the twitter will not update the page with a new tweet if it is posted without refreshing
            driver.refresh()
            new_tweet = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetText']"))).text
            #Comparing the tweets
            if new_tweet != last_tweet:
                print(f"NEW TWEET ------ {account} ------ {new_tweet}")
                last_tweet = new_tweet
            elif new_tweet == last_tweet:
                print(f"SAME TWEET ------ {account}")
        except Exception as err:
            print(f"ERROR: {err}")
        time.sleep(3)

# Utilizing threading to increase the efficiency
threads = []
for account in accounts:
    thread = threading.Thread(target=monitor_tweets, args=(account,))
    threads.append(thread)
    print(len(threads))
    thread.start()

for thread in threads:
    thread.join()
