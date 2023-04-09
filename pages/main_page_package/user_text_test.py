from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_youtube.locators import YouTubeLocators

from ..base_page import BasePage
from ..counter import Counter

counter = Counter()


class UserTextValidationTest(BasePage):

    def select_user(self, timeout=20):
        """Click User Icon"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_user_logo = wait.until(EC.visibility_of_element_located(YouTubeLocators.wait_user_form_locator),
                                      f"Could not find user form in {timeout} seconds")

        select_user_profile = self.browser.find_element(*YouTubeLocators.select_user_profile_locator)

        select_user_profile.click()

    def click_subscribe(self, timeout=20):
        """Click Subscribe Button"""
        wait = WebDriverWait(self.browser, timeout)
        _wait_subscribe_button = wait.until(EC.presence_of_element_located(YouTubeLocators.wait_user_profile_locator),
                                     f"Could not find subscribe button in {timeout} seconds")

        subscribe_button = self.browser.find_elements(*YouTubeLocators.subscribe_button_locator)

        subscribe_button[-1].click()

    def user_text_validation(self, timeout=20):
        """Check Text in Container"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_container = wait.until(EC.presence_of_element_located(YouTubeLocators.wait_user_profile_locator),
                                            f"Could not find subscribe button in {timeout} seconds")

        try:
            _input_button = self.browser.find_element(*YouTubeLocators.input_button_locator)
            print(f"User Text 'Войти' is PASSED")
            counter.add_pass()

        except(NoSuchElementException):
            print(f"User Text 'Войти' is FAILED")
            counter.add_fail()


class ResultUserText(BasePage):

    def result_pass_user_text(self):
        result_pass_user_text = counter.count_pass

        return result_pass_user_text

    def result_fail_user_text(self):
        result_fail_user_text = counter.count_fail

        return result_fail_user_text