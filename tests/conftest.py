import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options

from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browserVersion',
        help = 'Версия браузера в котором будут запущены тесты',
        default='127.0'
    )



@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    _browserVersion = request.config.getoption('--browserVersion')
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", _browserVersion)
    options.add_argument("--window-size=1280,900")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield
    browser.driver.maximize_window()
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


# @pytest.fixture(scope="function", autouse=True)
# def setup_browser():
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "128.0")
#     options.add_argument("--window-size=1280,900")
#     options.set_capability("selenoid:options", {
#         "enableVNC": True,
#         "enableVideo": True
#     })
#     options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})  # Включаем логирование браузера
#
#     browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
#     browser.config.driver_options = options
#     browser.config.timeout = 6
#
#     yield
#     browser.driver.maximize_window()
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()