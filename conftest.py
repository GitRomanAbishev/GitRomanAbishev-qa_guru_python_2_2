from selene.support.shared import browser
from selene import have
import pytest


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    yield
    browser.config.hold_browser_open = True


@pytest.fixture()
def open_browser_work():
    browser.open('http://feature5.def.k8s.dev.bi.zone/app/#/login')
    yield
    browser.config.hold_browser_open = True
