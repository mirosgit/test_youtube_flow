import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages.main_page import MainTests, ResultPassFailMainPage

YOUTUBE_URL = "https://www.youtube.com"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(YOUTUBE_URL)

    yield driver
    driver.quit()


def test_youtube_page(browser):

    main_page = MainTests(browser, YOUTUBE_URL)
    main_page.run_tab_name_tests()
    main_page.run_search_tests()
    main_page.run_user_text_tests()

    result_main = ResultPassFailMainPage(browser, YOUTUBE_URL)
    result_main.result()
    result_main.validate_result()


