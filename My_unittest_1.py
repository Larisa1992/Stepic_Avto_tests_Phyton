import unittest

class MyFirstTest(unittest.TestCase):
    def test_lesson5_step7_2(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector(".form-group.first_class input[placeholder = 'Введите имя']")
        name.send_keys("Имя") 
        Fam = browser.find_element_by_css_selector(".form-group.second_class input[placeholder = 'Введите фамилию']")
        Fam.send_keys("Фамилия")
        email = browser.find_element_by_css_selector(".form-group.third_class input[placeholder = 'Введите Email']")
        email.send_keys("Почта")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        #    Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!" , welcome_text)
        time.sleep(2)
        browser.close()

    
    def test_lesson5(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector(".form-group.first_class input[placeholder = 'Введите имя']")
        name.send_keys("Имя") 
        Fam = browser.find_element_by_css_selector(".form-group.second_class input[placeholder = 'Введите фамилию']")
        Fam.send_keys("Фамилия")
        email = browser.find_element_by_css_selector(".form-group.third_class input[placeholder = 'Введите Email']")
        email.send_keys("Почта")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        #    Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!" , welcome_text)
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    unittest.main()
