
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

driver = webdriver.Chrome(chrome_options=chrome_options)

def handler(email):
    driver = webdriver.Chrome("chromedriver.exe")

    driver.get("https://www.qwiklabs.com/users/sign_in")
    driver.set_window_size(1624, 838)
    driver.find_element(By.ID, "user_email").click()
    driver.find_element(By.ID, "user_email").send_keys("khalil.kasmi@softwarebusiness.us")
    driver.find_element(By.ID, "user_password").click()
    driver.find_element(By.ID, "user_password").send_keys("1P-assword")
    driver.find_element(By.ID, "user_password").send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, ".header-my-account-button > .mdl-button__ripple-container").click()
    driver.find_element(By.LINK_TEXT, "65 Credits").click()
    driver.find_element(By.LINK_TEXT, "Share Your Credits with Friends").click()
    driver.find_element(By.LINK_TEXT, "aws cloud practitioner").click()
    driver.find_element(By.ID, "token_allocation_group_filter_ids").click()
    driver.find_element(By.ID, "token_allocation_group_filter_ids").send_keys(""+email+"")
    driver.find_element(By.CSS_SELECTOR, ".form-row:nth-child(8) > .btn").click()

    wait = WebDriverWait(driver, 5)



def lambda_handler(event, context):
    string = "" + event + ""
    f = json.loads(string)
    email = f['email']
    encoded_string = email.encode("utf-8")
    handler(encoded_string)
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }