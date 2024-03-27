from selenium.webdriver.common.by import By


class MailPageLocators:
    LOCATOR_RAMBLER_WRITE_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button.rc__IEemq')
    LOCATOR_RAMBLER_MESSAGE_TOPIC = (By.CLASS_NAME, "ListItem-subject-2M")
    LOCATOR_RAMBLER_MESSAGE_RECEIVERS_INPUT = (By.ID, 'receivers')
    LOCATOR_RAMBLER_MESSAGE_TOPIC_INPUT = (By.ID, 'subject')
    LOCATOR_RAMBLER_EMAIL_RECEIVERS_RAMBLER = (By.CSS_SELECTOR, 'span[id^="EmailBadge-name"]')
    LOCATOR_RAMBLER_EMAIL_RECEIVERS_ANOTHER_PLATFORM = (By.CSS_SELECTOR, 'span[id^="EmailBadge-text"]')
    LOCATOR_RAMBLER_MESSAGE_TEXT = (By.CSS_SELECTOR, 'iframe[id^="tiny-react_"]')
    LOCATOR_RAMBLER_MESSAGE_TEXT_INPUT = (By.TAG_NAME, "body")
    LOCATOR_RAMBLER_SEND_MAIL_BUTTON = (By.CSS_SELECTOR,
                                        'button[data-mail-desktop="compose::footer_tools::3::send_button"]')
