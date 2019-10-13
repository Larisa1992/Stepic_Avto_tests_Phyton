from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math


message = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    #time.sleep(5)
    browser.quit()

@pytest.mark.parametrize('list_link', ["236895/step/1","236896/step/1","236897/step/1","236898/step/1","236899/step/1","236903/step/1","236904/step/1","236905/step/1"])
@pytest.mark.xfail
#(reason="Not Correct!")
def test_insert_answer(browser, list_link):
    link = f"https://stepik.org/lesson/{list_link}"
    browser.get(link)
    answer = math.log(int(time.time()))
    time.sleep(5)
    input_int = browser.find_element_by_css_selector("textarea.ember-text-area.ember-view")
    input_int.send_keys(str(answer))
    #button_send = browser.find_element_by_css_selector(".submit-submission")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button_send = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR , ".submit-submission"))
    )
    button_send.click()
    #message += WebDriverWait(browser, 5).until(
    #    EC.presence_of_element_located((By.CSS_SELECTOR , ".smart-hints__hint")).text
    #)
    fitback = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR , ".smart-hints__hint"))
        #EC.text_to_be_present_in_element((By.CSS_SELECTOR , ".smart-hints__hint"))
        #,"Correct!")
    )
    
    if (fitback.text != "Correct!"):
        print(fitback.text)
        message += fitback.text
        print(message)
print(message)   
    #ptint(message)
    #time.sleep(1)
    #smart-hints__hint
