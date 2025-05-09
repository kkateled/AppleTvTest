import pytest
import allure
from allure_commons.types import Severity
from start_project.pages.main_page import main_page
from start_project.pages.signin_form import signin_form


class TestSignInForm:
    @pytest.mark.positive
    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('User SignIn')
    @allure.title('SignIn with valid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_signin_with_valid_email(self, generate_email):
        main_page.open()
        main_page.open_registration_form()
        signin_form.enter_email(generate_email)
        signin_form.check_result()

    @pytest.mark.negative
    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('User SignIn')
    @allure.title('SignIn with invalid email')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_signin_with_invalid_email(self):
        main_page.open()
        main_page.open_registration_form()
        invalid_email = 'test@gmailcom'
        invalid_password = 'test_password'
        signin_form.enter_email(invalid_email)
        signin_form.enter_password(invalid_password)
        signin_form.check_result(email_valid=False)
