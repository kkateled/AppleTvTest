from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure
from selenium.common import NoSuchElementException
import time


class MainPage:
    def __init__(self):
        self.appletv_element = s("//a[@dir='ltr'][normalize-space()='Apple TV+']")
        self.mls_element = s("//a[@dir='ltr'][normalize-space()='MLS']")
        self.first_element_in_apple_tv_page = s("//span[text()='Top 10 TV Shows']")

        self.signin_form = s("//button[normalize-space()='Sign In']")
        self.registration_element = s("[data-test='accountName-input']")

        self.search_button = s('[data-testid="search-input__text-field"]')

        self.sections = ss('.dir-wrapper')
        self.page_title_section = s('.dir-wrapper')

        self.film_genre = '//a[@aria-label="{genre}"]'
        self.name_title_of_all_film_genres = s('//span[text()="Browse by Category"]')

    @allure.step('Open browser')
    def open(self):
        browser.open('/')

    @allure.step('Open registration form')
    def open_registration_form(self):
        self.signin_form.should(be.visible)
        self.signin_form.should(be.clickable)
        for i in range(0, 5):
            browser.driver.execute_script("arguments[0].click();", self.signin_form())
            time.sleep(2)

    @allure.step('Check registration is available')
    def check_registration_options_available(self):
        time.sleep(6)
        browser.driver.switch_to.frame(0)
        time.sleep(6)
        self.registration_element.should(be.visible)

    @allure.step('Check AppleTV button is clickable')
    def check_appletv_button_clickable(self):
        self.appletv_element.click()
        self.first_element_in_apple_tv_page.should(have.text('Top 10 TV Shows'))

    @allure.step('Check MLS button is clickable')
    def check_mls_button_clickable(self):
        self.mls_element.click()
        browser.should(have.url_containing('tvs.sbd.7000'))

    @allure.step('Search film by title')
    def search_film_by_title(self, film_title):
        self.search_button.click()
        time.sleep(2)
        self.search_button.should(be.blank).type(film_title).press_enter()
        time.sleep(2)

    @allure.step('Check search result')
    def check_result(self, film_title):
        try:
            search_hints = browser.all('ul.shelf-grid__list li')
            search_hints.should(have.size_greater_than(0))
            search_hints.first.click()
        except NoSuchElementException:
            print(f'Search for the request:{film_title} did not find anything')

    @allure.step('Go to selected section')
    def go_to_selected_section(self, section_name):
        element = self.sections.element_by(have.exact_text(section_name))
        time.sleep(2)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element())
        time.sleep(2)
        element.should(be.visible).click()

    @allure.step('Verify section name')
    def check_section_name(self):
        current_url_after = browser.driver.current_url
        browser.open(current_url_after)
        self.page_title_section.should(be.visible)

    @allure.step('Verify name of title')
    def check_title_genres_name(self):
        self.name_title_of_all_film_genres.should(be.visible)

    @allure.step('Go to selected films genre section')
    def go_to_selected_films_genre(self, genre):
        selector = self.film_genre.format(genre=genre)
        element = s(selector)
        element.should(be.visible).click()


main_page = MainPage()
