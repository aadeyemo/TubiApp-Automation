from appium.webdriver.common.appiumby import AppiumBy

class ScrollUtils:
    @staticmethod
    def scroll_to_text(driver, text):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )
