from module import Site
import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("./testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_create_and_verify_post(x_selector1, x_selector2, x_selector3, btn_selector, error_code,
                                plus_button_selector, post_form_selectors, ok_button_selector, title, check_title):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    wait = WebDriverWait(site.driver, 10)
    plus_button = wait.until(EC.presence_of_element_located((By.XPATH, plus_button_selector)))

    plus_button.click()

    time.sleep(testdata["sleep_time"])

    post_form = post_form_selectors
    site.find_element("xpath", post_form["title"]).send_keys((testdata["title_n"]))
    site.find_element("xpath", post_form["description"]).send_keys((testdata["description_n"]))
    site.find_element("xpath", post_form["content"]).send_keys((testdata["content_n"]))

    ok_button = site.find_element("xpath", ok_button_selector)
    ok_button.click()

    time.sleep(testdata["sleep_time"])

    created_post_title = site.find_element("xpath", check_title).text
    assert created_post_title == title, "The created post title does not match the expected title."

    site.driver.close()




