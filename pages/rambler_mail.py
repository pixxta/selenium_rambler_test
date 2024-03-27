from pages.base_app import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.mail_page_locators import MailPageLocators

class LoginHelper(BasePage):

    def click_mail_button_to_login(self):
        self.find_element(LoginPageLocators.LOCATOR_RAMBLER_LOGIN_MAIL_BUTTON).click()

    def go_to_login_window(self):
        self.switch_window_to_new()

    def enter_login(self, word):
        login_input = self.find_element(LoginPageLocators.LOCATOR_RAMBLER_LOGIN_INPUT)
        login_input.send_keys(word)

    def enter_password(self, word):
        login_input = self.find_element(LoginPageLocators.LOCATOR_RAMBLER_PASSWORD_INPUT)
        login_input.send_keys(word)

    def click_login(self):
        self.find_element(LoginPageLocators.LOCATOR_RAMBLER_LOGIN_BUTTON).click()

    def go_to_main_window(self):
        self.switch_window_to_old()

    def check_is_login(self, login):
        return self.check_text_presence(login)

    def go_to_mail(self):
        return self.driver.get("https://mail.rambler.ru/")

    def check_count_messages_by_topic(self, topic):
        messages = self.find_elements(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_TOPIC)
        messages_topics = [item.text for item in messages]
        return messages_topics.count(topic)

    def send_message(self, mail, topic):
        count_messages = self.check_count_messages_by_topic('Тестовое задание Selenium')

        self.find_element(MailPageLocators.LOCATOR_RAMBLER_WRITE_MESSAGE_BUTTON).click()

        self.safe_input_receivers_email(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_RECEIVERS_INPUT, mail,
                                        MailPageLocators.LOCATOR_RAMBLER_EMAIL_RECEIVERS_RAMBLER)
        input_receivers = self.find_element(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_RECEIVERS_INPUT)
        input_receivers.send_keys(mail)

        input_topic = self.find_element(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_TOPIC_INPUT)
        input_topic.send_keys(topic)

        input_text = self.find_element(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_TEXT)
        self.driver.switch_to.frame(input_text)
        text_field = self.find_element(MailPageLocators.LOCATOR_RAMBLER_MESSAGE_TEXT_INPUT)
        text_field.send_keys(count_messages)
        self.driver.switch_to.default_content()

        self.find_element(MailPageLocators.LOCATOR_RAMBLER_SEND_MAIL_BUTTON).click()

    def check_message_is_sent(self):
        return self.check_text_presence('Письмо отправлено', time=20)
