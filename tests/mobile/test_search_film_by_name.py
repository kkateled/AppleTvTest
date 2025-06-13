from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():

    with step('Type search'):
        browser.element((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Button")).click()
        browser.element((AppiumBy.XPATH, "//*[contains(@text, 'Search')]")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.EditText")).type('The Gorge')

    with step('Verify content found'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('The Gorge'))
