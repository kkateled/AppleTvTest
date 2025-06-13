import allure_commons
import pytest
from selene import browser, support
import os
from appium.options.android import UiAutomator2Options
from appium import webdriver
from start_project.utils.attach import add_screenshot, add_video, add_xml
from dotenv import load_dotenv


load_dotenv()
username = os.getenv('BROWSERSTACKUSERNAME')
access_key = os.getenv('BROWSERSTACKACCESSKEY')


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv(
        'base_url', 'https://tv.apple.com'
    )
    browser.config.driver_name = os.getenv('driver_name', 'chrome')
    browser.config.hold_driver_at_exit = (
        os.getenv('hold_driver_at_exit', 'false').lower() == 'true'
    )
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_height', '768')
    browser.config.timeout = float(os.getenv('timeout', '3.0'))

    yield


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",
        # Set URL of the application under test
        "app": "bs://sample.app",
        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "AppleTV test project",
            "buildName": "browserstack-build-1",
            "sessionName": "AppleTV first_test",
            # Set your access credentials
            "userName": username,
            "accessKey": access_key
        }
    })
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))  # Timeout for waiting for elements

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    session_id = browser.driver.session_id

    yield

    add_screenshot(browser)
    add_xml(browser)
    add_video(session_id, username, access_key)

    browser.quit()
