from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("chromedriver")  # Update with your chromedriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_dynamic_content(url):
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load
    page_text = driver.find_element(By.TAG_NAME, "body").text
    return page_text

url = "https://www.ppsc.gop.pk/(S(oxicsm3utyrfa3nfxn0c3tws))/jobs.aspx"
content = fetch_dynamic_content(url)
print(content)

driver.quit()
