from pragmatic_automation import * 

driver = getDriver()
log_in(driver, "swolf", "Sw052021!")

driver.get('https://pragmatik.lcsinternalservices.lcs.dev/#/teamstatusreview')
driver.implicitly_wait(1)
attribute_value = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))).get_attribute("innerHTML")
print(attribute_value)