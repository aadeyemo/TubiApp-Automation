from appium.webdriver.common.appiumby import AppiumBy

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def skip_onboarding(self):
        try:
            skip_btn = self.driver.find_element(AppiumBy.ID, "com.tubitv:id/btn_skip")
            skip_btn.click()
        except:
            pass
