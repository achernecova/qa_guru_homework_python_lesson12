import allure

from tests.demoqa.pages import users
from tests.demoqa.pages.application import app
from tests.demoqa.pages.users import User


@allure.title("Successful fill form with app manager")
def test_registration_in_simple_form_with_app_manager():
    with allure.step("Открываем страницу"):
        app.left_panel.open()
    with allure.step("Заполняем поля и проверяем отправку"):
        app.simple_page.fill_full_name(users.first_user)


@allure.title("Successful fill form with user in dataclass")
def test_registration_in_simple_form_with_app_manager_with_user():
    with allure.step("Открываем страницу"):
        app.left_panel.open()
        user = User(
            fullname="Alexandra",
            email="achernecova@inbox.ru",
            current_address="Москва",
            permanent_address="Москва",
        )
    with allure.step("Заполняем поля и проверяем отправку"):
        app.simple_page.fill_full_name(user)
