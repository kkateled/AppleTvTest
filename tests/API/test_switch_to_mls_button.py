import allure
from start_project.utils.api_helper import api_request


@allure.title("Checking mls page")
def test_switch_to_mls_api(base_api_url):
    endpoint = "/api/uts/v3/canvases/channels/tvs.sbd.7000"
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
    with allure.step('True headers'):
        assert response.headers["Content-Type"] == "application/json"
    with allure.step('Schema is validate'):
        assert "MLS" in response.text
