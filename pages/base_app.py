from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.rambler.ru/"

    def find_element(self, locator, time=20):
        visible_element = WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element by locator {locator} is not clickable"
        )

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_text_presence(self, text, time=10):
        try:
            WebDriverWait(self.driver, time).until(
                lambda driver: text in driver.page_source
            )
            return True
        except TimeoutException:
            return False

    def switch_window_to_new(self):
        window_handles = self.driver.window_handles
        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)

    def switch_window_to_old(self):
        window_handles = self.driver.window_handles
        old_window_handle = window_handles[0]
        self.driver.switch_to.window(old_window_handle)

    def safe_input_receivers_email(self, locator, text, rambler_email_locator, time=5):
        try:
            input_element = WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator)
            )
            input_element.clear()
            input_element.send_keys(text)

            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(rambler_email_locator)
            )

            input_text_element = WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator)
            )
            if input_text_element.get_attribute("value") == text:
                return True
            else:
                return False
        except TimeoutException:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
