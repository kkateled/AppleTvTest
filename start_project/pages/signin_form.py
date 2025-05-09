from selene import be, have, browser
from selene.support.shared.jquery_style import s
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import allure
import time


class SignInForm:
    def __init__(self):
        self.email_input = s("//input[@id='accountName']")
        self.password_input = s("//input[@id='password_text_field']")
        self.sliding_panel = s('.form-row.swp-account-name')
        self.invite_to_registration = s("//h1[@class='heading typography-headline']")
        self.invite_to_sign_in = s("//h1[@class='generic-auth-presentation__header']")
        self.err_message1 = s("//p[@id='errMsg']")
        self.err_message2 = s("//h2[@id='alertInfo']")

    @allure.step('Enter email into the field')
    def enter_email(self, email):
        browser.switch_to.frame(0)
        self.email_input.should(be.visible)
        time.sleep(2)
        self.email_input.should(be.blank).type(email).press_enter()
        time.sleep(2)

    @allure.step('Enter password into the field')
    def enter_password(self, password):
        browser.switch_to.frame(0)
        time.sleep(6)
        self.password_input.should(be.visible)
        time.sleep(2)
        self.password_input.should(be.blank).type(password).press_enter()
        time.sleep(2)

    @allure.step('Verify registration')
    def check_result(self, email_valid=True):
        if email_valid:
            self.invite_to_sign_in.matching(be.visible) or self.invite_to_registration.matching(be.visible)
        else:
            self.err_message2.matching(be.visible) or self.err_message1.matching(be.visible)


signin_form = SignInForm()
