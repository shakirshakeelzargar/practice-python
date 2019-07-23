#from selenium import webdriver
#import time
#from selenium.webdriver.common.keys import Keys
#driver=webdriver.Chrome("D:/selenium/chromedriver.exe")
#driver.set_page_load_timeout(10)
#driver.get("http://google.com")
#driver.find_element_by_name("q").send_keys("HELLO GOOGLE")
#clickk=driver.find_element_by_xpath
#clickk.send_keys(Keys.RETURN)
#
#
#time.sleep(4)
#driver.quit()




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://accounts.google.com')

input = browser.find_element_by_xpath("//div[@class='Xb9hP']//input[@type='email']")
#WebDriverWait(driver,5)
input.send_keys("YourEmail")
input.send_keys(Keys.RETURN)
browser.implicitly_wait(100)
input = browser.find_element_by_xpath("//div[@class='Xb9hP']//input[@type='password']")
#WebDriverWait(driver,5)
input.send_keys("YourPassword")
input.send_keys(Keys.RETURN)
browser.implicitly_wait(100)
input = browser.find_element_by_xpath("//div[@class='gb_Ef gb_Ka gb_wg gb_f']//span[@class='gb_xa gbii']")
input.click()
browser.implicitly_wait(100)
input = browser.find_element_by_xpath("//div[@class='gb_1f gb_nb']//a[@class='gb_0 gb_5f gb_cg gb_Me gb_ob']")
input.click()




#search.send_keys("google search through python")
#search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
#browser.quit()