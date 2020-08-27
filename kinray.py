from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Kinray():
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome()
        self.options.binary_location = "\GoogleChromePortable\GoogleChromePortable.exe"
    
    def connect(self, username, password):
        driver = self.driver
        driver.get('http://www.kinray.com')
        userElem = self.driver.find_element_by_xpath('//*[@id="custId"]') 
        passElem = self.driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
        userElem.send_keys(username)
        passElem.send_keys(password)
        passElem.submit()
        driver.implicitly_wait(10)
        popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/img')
        popup.click()
        driver.implicitly_wait(10)
        popup.click()
        driver.implicitly_wait(10)
        popup.click()
        
    def home(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.switch_to.default_content()
        driver.switch_to.frame('search')
        poElem = driver.find_element_by_xpath('/html/body/div/button[1]')
        poElem.click()

    def history(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.switch_to.default_content()
        driver.switch_to.frame('search')
        poElem = driver.find_element_by_xpath('/html/body/div/button[3]')
        poElem.click()

    def returns(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.switch_to.default_content()
        driver.switch_to.frame('search')
        poElem = driver.find_element_by_xpath('/html/body/div/button[5]')
        poElem.click()

    def driver(self):
        driver = self.driver
        return driver

''' 
def main():
    kinray = Kinray()
    kinray.connect('','')
    kinray.history()
   
if __name__ == '__main__':
    main()
'''
