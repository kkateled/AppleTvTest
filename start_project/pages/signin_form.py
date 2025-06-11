from selene import be, browser
from selene.support.shared.jquery_style import s
import allure
import time


class SignInForm:
    def __init__(self):
        self.email_input = s("[data-test='accountName-input']")
        self.password_input = s("//input[@id='password_text_field']")
        self.invite_to_registration = s("//input[@id='password_text_field']")
        self.invite_to_sign_in = s("//button[@id='continue-password']")
        self.err_message1 = s("//p[@id='errMsg']")
        self.err_message2 = s("//h2[@id='alertInfo']")

    @allure.step('Enter email into the field')
    def enter_email(self, email):
        time.sleep(6)
        browser.driver.switch_to.frame(0)
        time.sleep(6)
        self.email_input.should(be.visible)
        time.sleep(2)
        self.email_input.should(be.blank).type(email).press_enter()
        time.sleep(2)

    @allure.step('Enter password into the field')
    def enter_password(self, password):
        browser.driver.switch_to.frame("aid-auth-widget-iFrame")
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
