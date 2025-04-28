import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "A7S200939064244 device"
    options.app_package = "com.tubitv"
    options.app_activity = "com.tubitv.activities.SplashActivity"
    options.no_reset = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
