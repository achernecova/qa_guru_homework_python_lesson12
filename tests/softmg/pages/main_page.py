from tests.softmg.pages.header_panel import HeaderPanel


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.header_panel = HeaderPanel()
