import allure
from start_project.utils.api_helper import api_request
from jsonschema import validate
from start_project.shemas.trailer_shema import trailer


@allure.tag('API')
@allure.feature('API')
@allure.story('Trailer movie')
@allure.title("Checking trailer data")
def test_trailer_api(base_api_url):
    endpoint = "/api/uts/v3/shelves/uts.col.Trailers.umc.cmc.26o403koqo2klixc0jtqy6tmc"
    params = {"caller": "web",
              "locale": "en-US",
              "pfm": "web",
              "sf": "143441",
              "utscf": "OjAAAAEAAAAAAAAAEAAAACMA",
              "utsk": "6e3013c6d6fae3c2::::::235656c069bb0efb",
              "v": "84"
              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('title = Trailers'):
        assert response.json()["data"]["shelf"]["header"]["title"] == "Trailers"
    with allure.step('movieTitle correct'):
        assert response.json()["data"]["shelf"]["items"][0]["playables"][0]["canonicalMetadata"]["movieTitle"] == "The Gorge"
    with allure.step('Schema is validate'):
        validate(response.json(), trailer)
