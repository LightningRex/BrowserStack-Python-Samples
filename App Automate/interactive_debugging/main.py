from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.options.ios.xcuitest.base import XCUITestOptions

import os,time

URL = os.environ.get('URL')
options = UiAutomator2Options().load_capabilities({})
# options = XCUITestOptions().load_capabilities({})

driver = webdriver.Remote(URL,options=options)
print("Test started")
time.sleep(200)
driver.quit()
print("Test completed")