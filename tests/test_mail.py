from pages.rambler_mail import LoginHelper
import allure
from config import RAMBLER_LOGIN, RAMBLER_PASSWORD, SENDER_EMAIL


class TestRambler:

    @allure.title('Логин в почте Rambler')
    def test_rambler_mail_login(self, browser):
        rambler_main_page = LoginHelper(browser)
        rambler_main_page.go_to_site()
        rambler_main_page.click_mail_button_to_login()
        rambler_main_page.go_to_login_window()
        rambler_main_page.enter_login(RAMBLER_LOGIN)
        rambler_main_page.enter_password(RAMBLER_PASSWORD)
        rambler_main_page.click_login()
        rambler_main_page.go_to_main_window()
        assert rambler_main_page.check_is_login(RAMBLER_LOGIN.split('@')[0])

    @allure.title('Отправка сообщения на почту')
    def test_rambler_mail_messages(self, browser):
        rambler_mail_page = LoginHelper(browser)
        rambler_mail_page.go_to_mail()
        rambler_mail_page.send_message(SENDER_EMAIL, 'Тестовое задание Selenium')
        assert rambler_mail_page.check_message_is_sent()
