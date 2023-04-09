from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_youtube_flow.locators import YouTubeLocators
from test_youtube_flow.test_data import TestData

from ..base_page import BasePage
from ..counter import Counter

counter = Counter()


class TabNameValidationTest(BasePage):

    def tab_name_validation(self, timeout=20):
        """Check Name Tab"""

        wait = WebDriverWait(self.browser, timeout)
        _wait_loadings_page = wait.until(EC.presence_of_element_located(YouTubeLocators.wait_loading_page),
                                       f"Could not load the page in {timeout} seconds")

        if str(self.browser.title) == str(TestData.tab_name_data):
            print(f"Tab Name Text is PASSED")
            counter.add_pass()

        else:
            print(f"Tab Name Text is FAILED")
            counter.add_fail()


class ResultTabName(BasePage):

    def result_pass_tab_name(self):
        result_pass_tab_name = counter.count_pass

        return result_pass_tab_name

    def result_fail_tab_name(self):
        result_fail_tab_name = counter.count_fail

        return result_fail_tab_name