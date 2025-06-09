import os
import allure
import requests
from allure_commons.types import AttachmentType
import logging
import json


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_video(browser):
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
        auth=(user_name, access_key),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def response_logging(response: requests.Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: requests.Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body.decode('utf-8'), indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    else:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
