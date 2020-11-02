import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

    def tearDown(self):
        self.driver.quit()

    def testValidLogin(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
        email_field.send_keys('tester@tester.com')
        pwd_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'passwd')))
        pwd_field.send_keys('123qweasd')
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#SubmitLogin')))
        button.click()
        signout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')))
        assert signout.text == 'Sign out'

    def testInvalidLogin(self):
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
        email_field.send_keys('tester@tester.com')
        pwd_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'passwd')))
        pwd_field.send_keys('123qw')
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#SubmitLogin')))
        button.click()
        alert = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')))
        assert alert.text == 'Authentication failed.'


if __name__ == '__main__':
    unittest.main()
