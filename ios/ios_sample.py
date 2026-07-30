import os,time

from appium import webdriver
from appium.options.ios.xcuitest.base import XCUITestOptions

URL = os.environ.get('URL')

options = XCUITestOptions().load_capabilities({})

driver = webdriver.Remote(URL,options=options)

print("Test started")
minutes=5
for i in range(minutes):
    driver.page_source
print("Test completed")

driver.quit()