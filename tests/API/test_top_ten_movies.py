import allure
from jsonschema import validate
from start_project.shemas.top_ten_movies_shema import movies
from start_project.utils.api_helper import api_request


@allure.tag('API')
@allure.feature('API')
@allure.story('Top 10 movies')
@allure.title("Checking top 10 movies")
def test_top_ten_movies_api(base_api_url):
    endpoint = "/api/uts/v3/shelves/uts.col.ChartsMovies.tvs.sbd.4000"
    params = {"caller": "web",
              "ctx_brand": "tvs.sbd.4000",
              "ctx_cvs": "edt.cvs.610c550f-938a-46e7-98e3-c573fcd24208",
              "ctx_shelf": "edt.shelf.649e17ea-7079-4fe6-a1e2-acccee44acec",
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
    with allure.step('title = Top 10 Movies'):
        assert response.json()["data"]["shelf"]["header"]["title"] == "Top 10 Movies"
    with allure.step('Schema is validate'):
        validate(response.json(), movies)
