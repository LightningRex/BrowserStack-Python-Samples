from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from concurrent.futures import ThreadPoolExecutor, as_completed
import os, time

def run_test(test_id: int):
    driver = webdriver.Remote('https://hub.browserstack.com/wd/hub')

    time.sleep(10)
    main_screen = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Welcome to The Red Sea"]')

    time.sleep(10)
    text = main_screen.text

    if text == "Welcome to The Red Sea":
        print("Success!")

    driver.quit()

if __name__ == "__main__":
    # Run 10 tests in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(run_test, i) for i in range(1, 11)]
        for future in as_completed(futures):
            print("Test finished:", future.result())