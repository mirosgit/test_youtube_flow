from ..pages import main_page_package
from .base_page import BasePage


class MainTests(BasePage):

    def run_tab_name_tests(self):

        main_page_package.TabNameValidationTest.tab_name_validation(self)

    def run_search_tests(self):

        main_page_package.SearchValidationTest.input_number_to_search_field(self)
        main_page_package.SearchValidationTest.select_second_position_search(self)
        main_page_package.SearchValidationTest.select_fourth_position_video(self)

    def run_user_text_tests(self):

        main_page_package.UserTextValidationTest.select_user(self)
        main_page_package.UserTextValidationTest.click_subscribe(self)
        main_page_package.UserTextValidationTest.user_text_validation(self)


class ResultInModules(BasePage):

    def result_in_modules_pass(self):
        result_in_modules_pass = main_page_package.ResultTabName.result_pass_tab_name(self) + \
                                 main_page_package.ResultUserText.result_pass_user_text(self)

        return result_in_modules_pass

    def result_in_modules_fail(self):
        result_in_modules_fail = main_page_package.ResultTabName.result_fail_tab_name(self) + \
                                 main_page_package.ResultUserText.result_fail_user_text(self)

        return result_in_modules_fail


class ResultPassFailMainPage(BasePage):

    def result(self):
        _sum_tests = ResultInModules.result_in_modules_pass(self) + ResultInModules.result_in_modules_fail(self)
        _percent_pass = round(((ResultInModules.result_in_modules_pass(self) / _sum_tests) * 100), 2)
        _percent_fail = round((100 - _percent_pass), 2)
        print("==================================")
        print("Total:", _sum_tests, "Test Scenarios")
        print("Passed Tests:", ResultInModules.result_in_modules_pass(self), "-", _percent_pass, "%")
        print("Failed Tests:", ResultInModules.result_in_modules_fail(self), "-", _percent_fail, "%")
        print("==================================")

    def validate_result(self):

        if ResultInModules.result_in_modules_fail(self) > 0:

            assert False

