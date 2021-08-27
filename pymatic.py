from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts = Options()
opts.headless = True
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--ignore-ssl-errors')
driver = Chrome(options=opts)

# logs in
driver.get('https://pragmatik.lcsinternalservices.lcs.dev/Account/Login')
print(driver.title)
username_field = driver.find_element_by_name("Username")
password_field = driver.find_element_by_name("Password")
username_field.send_keys("swolf")
password_field.send_keys("Sw052021!")
password_field.send_keys(Keys.RETURN)
print(driver.current_url)

driver.get('https://pragmatik.lcsinternalservices.lcs.dev/#/teamstatusreview')
driver.implicitly_wait(1)
attribute_value = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))).get_attribute("innerHTML")
print(attribute_value)