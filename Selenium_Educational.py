'''
This program will open the URL, maximize it, 
takes a sceenshot from the webpage, and
saves it as a png file in the same folder.
by: Mersad Zanbagh <zanbagh.mersad@gmail.com>
'''

#Importing webdriver from selenium library
from selenium import webdriver

#the instance of Chrome WebDriver is created 
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#getting website to the driver
driver.get("https://sundialhomeproducts.com/")

#maximizing window
driver.maximize_window()

#Take and save screen shot as png file
driver.find_element_by_css_selector('.btn.popup-close').click()

#Close the driver
driver.close()

#END