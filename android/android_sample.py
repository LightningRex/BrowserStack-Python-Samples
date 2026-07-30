import os, time

from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

URL = os.environ.get('URL')

options = UiAutomator2Options().load_capabilities({})

driver = webdriver.Remote(URL,options=options)

print("Test started")
minutes=5
for i in range(minutes):
    driver.page_source
print("Test completed")

driver.quit()