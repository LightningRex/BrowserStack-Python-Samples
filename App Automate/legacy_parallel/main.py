import os,time
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from concurrent.futures import ThreadPoolExecutor


BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL") 

def run_test(test_id):
    options = UiAutomator2Options().load_capabilities({
        "platformName" : "android",
        "platformVersion" : "10.0",
        "deviceName" : "Samsung Galaxy A51",
        "app" : "bs://c7dc0b75625ef19dd43aca9e97ea5d43e96e1522", #specify app url (test suite = bs://25ecd2fc1ba5d74d113c72f954ad275ffebedde6)
        'bstack:options' : {
            "buildName" : "Samsung Galaxy A51 occasionally gets stuck",
            "sessionName" : "Unable to Launch App",
            "userName" : BROWSERSTACK_USERNAME,
            "accessKey" : BROWSERSTACK_ACCESS_KEY,
        }
    })

    driver = webdriver.Remote(URL, options=options)
    print("Sleeping...")
    time.sleep(10)
    print("Good morning!")
    driver.quit()


#Execute parallel tests
if __name__ == "__main__":
    PARALLEL_TESTS = 10

    with ThreadPoolExecutor(max_workers=PARALLEL_TESTS) as executor:
        results = [executor.submit(run_test, i + 1) for i in range(PARALLEL_TESTS)]
        for r in results:
            r.result()