from selenium.webdriver.common.by import By


class YouTubeLocators:

    wait_loading_page = (By.TAG_NAME, "html")
    search_field_locator = (By.NAME, "search_query")
    wait_search_list = (By.CLASS_NAME, "sbsb_b")
    select_second_position_search_locator = (By.XPATH, "//body//div[2]/div[1]//ul/li[2]")
    wait_video_list_locator = (By.CLASS_NAME, "style-scope.ytd-section-list-renderer")
    select_fourth_position_video_locator = (By.XPATH, "//*[@id='contents']/ytd-video-renderer[4]")
    wait_user_form_locator = (By.CLASS_NAME, "style-scope.ytd-watch-metadata")
    select_user_profile_locator = (By.XPATH, "//*[@id='owner']/ytd-video-owner-renderer/a")
    wait_user_profile_locator = (By.CLASS_NAME, "style-scope.ytd-c4-tabbed-header-renderer")
    subscribe_button_locator = (By.XPATH, "//*[@id='subscribe-button']/ytd-button-renderer/yt-button-shape/button/div/span[contains(text(), 'Подписаться')]/ancestor::*/button")
    wait_container = (By.XPATH, "//body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown")
    input_button_locator = (By.XPATH, "//*[@id='button']/yt-button-shape/a/div/span[text()='Войти']")
