import allure
from jsonschema import validate
from start_project.shemas.search_shema import search
from start_project.utils.api_helper import api_request


@allure.tag('API')
@allure.feature('API')
@allure.story('Search movie')
@allure.title("Checking movie data")
def test_search_movie_api(base_api_url):
    endpoint = "/api/uts/v3/search"
    params = {"caller": "web",
              "locale": "en-US",
              "pfm": "web",
              "searchTerm": "the gorge",
              "sf": "143441",
              "utscf": "OjAAAAEAAAAAAAAAEAAAACMA",
              "utsk": "6e3013c6d6fae3c2::::::235656c069bb0efb",
              "v": "84"
              }
    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('title = The Gorge'):
        assert response.json()["data"]["canvas"]["shelves"][0]["items"][0]["title"] == "The Gorge"
    with allure.step('Schema is validate'):
        validate(response.json(), search)
