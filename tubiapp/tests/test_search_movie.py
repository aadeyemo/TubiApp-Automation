import pytest
from tubiapp.pages.home_page import HomePage
from tubiapp.pages.search_page import SearchPage
from tubiapp.utils.screen_recorder import ScreenRecorder

@pytest.mark.positive
def test_search_uglydolls(driver):
    ScreenRecorder.start_recording(driver)

    home = HomePage(driver)
    search = SearchPage(driver)

    home.skip_onboarding()
    search.open_search()
    search.search_movie("UglyDolls")

    ScreenRecorder.stop_and_save_recording(driver, "reports/test_search_uglydolls.mp4")
