from selene.support.shared import browser
from selene import have
import pytest


@pytest.fixture(scope='package')
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_find_selene(open_browser_work):
    browser.element('[[name="1662479857_1"]]').type('')
    browser.element('[[name="1662479857_2"]]').type('')

#     browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
#     pass
#
#
# def test_bad_request(open_browser):
#     browser.element('[name="q"]').type('asdddfssdf').press_enter()
#     browser.element('[id="search"]').should(have.no.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
#     pass