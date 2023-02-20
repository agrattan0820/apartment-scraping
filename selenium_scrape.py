from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# Don't close selenium window automatically
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), chrome_options=chrome_options)
driver.get("https://www.apartments.com/")
assert "Apartments.com: Apartments and Homes for Rent" in driver.title
driver.implicitly_wait(3)
search_input = driver.find_element(By.ID, "quickSearchLookup")
search_input.clear()
search_input.send_keys("Pittsburgh")

search_btn = driver.find_element(By.CLASS_NAME, "go")
search_btn.click()

# driver.close()
