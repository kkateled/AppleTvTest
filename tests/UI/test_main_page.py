import allure
from allure_commons.types import Severity
from start_project.pages.main_page import main_page


class TestMainPage:
    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Registration options')
    @allure.title('Check registration options')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_registration_options_available(self, generate_email):
        main_page.open()
        main_page.open_registration_form()
        main_page.check_registration_options_available()

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('AppleTV button')
    @allure.title('Checking AppleTV button')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_appletv_button_available(self):
        main_page.open()
        main_page.check_appletv_button_clickable()

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('MLS button')
    @allure.title('Checking MLS button')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_mls_button_available(self):
        main_page.open()
        main_page.check_mls_button_clickable()

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Film search')
    @allure.title('Search film by title')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_search_film_by_title(self):
        film_title_for_search = 'the gorge'
        main_page.open()
        main_page.search_film_by_title(film_title_for_search)
        main_page.check_result(film_title_for_search)

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Web-app sections')
    @allure.title('Check selected section availability')
    @allure.severity(Severity.CRITICAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_selected_section_available(self):
        section_name = 'Top 10 TV Shows'
        main_page.open()
        main_page.go_to_selected_section(section_name)
        main_page.check_section_name()

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Film genre')
    @allure.title('Select film by genre')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://tv.apple.com/', name='AppleTV')
    def test_select_film_by_genre(self):
        film_genre = 'Sci-Fi'
        main_page.open()
        main_page.check_title_genres_name()
        main_page.go_to_selected_films_genre(film_genre)

