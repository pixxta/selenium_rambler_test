from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOCATOR_RAMBLER_LOGIN_MAIL_BUTTON = (By.CLASS_NAME, 'rc__KWXsu')
    LOCATOR_RAMBLER_LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-cerber-id='login_form::main::login_button']")
    LOCATOR_RAMBLER_LOGIN_INPUT = (By.ID, "login")
    LOCATOR_RAMBLER_PASSWORD_INPUT = (By.ID, "password")
