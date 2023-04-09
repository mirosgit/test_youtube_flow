import random

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_youtube.locators import YouTubeLocators
from test_youtube.test_data import TestData

from ..base_page import BasePage


class SearchValidationTest(BasePage):

    def input_number_to_search_field(self, timeout=20):
        """Input Random Number to Search Field"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_search_field = wait.until(EC.visibility_of_element_located(YouTubeLocators.search_field_locator),
                                         f"Could not find search field in {timeout} seconds")

        search_field = self.browser.find_element(*YouTubeLocators.search_field_locator)

        for value in range(TestData.len_random_number):

            search_field.send_keys(random.randint(0, 9))

    def select_second_position_search(self, timeout=20):

        """Select 2nd position in search list"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_search_list = wait.until(EC.visibility_of_element_located(YouTubeLocators.wait_search_list),
                                         f"Could not find search list in {timeout} seconds")

        select_second_position_search = self.browser.find_element(*YouTubeLocators.select_second_position_search_locator)

        select_second_position_search.click()

    def select_fourth_position_video(self, timeout=20):
        """Select 4th position in video list"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_video_list = wait.until(EC.visibility_of_element_located(YouTubeLocators.wait_video_list_locator),
                                       f"Could not find video list in {timeout} seconds")

        select_fourth_position_video = self.browser.find_element(*YouTubeLocators.select_fourth_position_video_locator)

        select_fourth_position_video.click()