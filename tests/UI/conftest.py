import pytest
import allure
from start_project.utils import attach
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from faker import Faker


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')


@pytest.fixture(scope='function', autouse=True)
def manage_browser(request):
    browser_name = request.config.getoption('--browser_name')
    options = ChromeOptions()
    driver_class = webdriver.Chrome
    browser.config.driver = driver_class(options=options)
    browser.config.base_url = "https://tv.apple.com/"
    browser.config.window_width = 1700
    browser.config.window_height = 1080
    browser.config.timeout = 30
    yield
    report = request.node.rep_call
    if report.failed:
        with allure.step('Add screenshot'):
            attach.add_screenshot(browser)
    with allure.step('Add browser logs'):
        if browser_name == 'chrome':
            attach.add_logs(browser)
    with allure.step('Add HTML'):
        attach.add_html(browser)
    browser.quit()


@pytest.fixture
def generate_email():
    fake = Faker()
    return fake.email()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, 'rep_' + report.when, report)

