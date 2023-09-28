import pytest
import yaml

with open("./testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def error_code():
    return "401"


@pytest.fixture()
def account_name():
    return f"Hello, {testdata['login']}"


@pytest.fixture()
def plus_button_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def post_form_selectors():
    return {
        "title": """//*[@id="create-item"]/div/div/div[1]/div/label/input""",
        "description": """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""",
        "content": """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    }


@pytest.fixture()
def ok_button_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def title():
    return f"{testdata['title_n']}"
