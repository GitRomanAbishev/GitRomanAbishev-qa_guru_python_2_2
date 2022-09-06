from selene.support.shared import browser
from selene import have
import pytest


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    yield
    browser.config.hold_browser_open = True


