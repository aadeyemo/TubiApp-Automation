from appium.webdriver.common.appiumby import AppiumBy

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open_search(self):
        self.driver.find_element(AppiumBy.ID, "com.tubitv:id/search_icon").click()

    def search_movie(self, movie_name):
        search_box = self.driver.find_element(AppiumBy.ID, "com.tubitv:id/search_src_text")
        search_box.send_keys(movie_name)
