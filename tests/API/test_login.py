import allure
import os
from start_project.utils.api_helper import api_request


@allure.title("Check auth")
def test_trailer_api():
    base_api_url = "https://idmsa.apple.com"
    endpoint = "/appleauth/auth/federate"
    params = {"isRememberMeEnabled": "false"}
    LOGIN = os.getenv("LOGIN")
    payload = {"accountName": LOGIN,
               "rememberMe": "false",
               }

    response = api_request(base_api_url, endpoint, "POST", payload, params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Check cookies'):
        assert response.cookies.get("dslang") == "US-EN"
        assert response.cookies.get("site") == "USA"
