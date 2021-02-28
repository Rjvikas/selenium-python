'''
Created on Dec 23, 2020

@author: Vikas
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
 
class Login(object):
    
    submit_button="//button[normalize-space()='Log In']"
    email="//input[@id='email']"
    password="//input[@id='pass']"
    user_name="//span[contains(text(),'Vikas Mishra')]"
    
    def __init__(self,webdriver):
        
        self.webdriver=webdriver
    
    
    def setupClass(self):
        try:
            self.driver=webdriver.Chrome(r"C:\Users\Vikas\git\repository\selenium-python\Browser\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("https://en-gb.facebook.com/login/")
        except Exception as e:
            print("unable to find the element",e)    
    def click_villinger(self):
        
        try:
            time.sleep(2)
            self.driver.save_screenshot(r"C:\Users\Vikas\git\repository\selenium-python\pageactions\Screenshot" + "login_click_page.png")
            self.driver.find_element_by_xpath(self.submit_button).click()
            element= self.driver.find_element_by_xpath(self.user_name).text
            self.driver.save_screenshot(r"C:\Users\Vikas\git\repository\selenium-python\pageactions\Screenshot" + "facebook_page.png")
            time.sleep(2)
            return element
        except Exception as e:
            print("unable to find the element",e)
            
    def enter_email(self,user_email):
        try:
            time.sleep(2)
            self.driver.save_screenshot(r"C:\Users\Vikas\git\repository\selenium-python\pageactions\Screenshot" + "login_page.png")
            self.driver.get("https://en-gb.facebook.com/login/") 
            self.driver.find_element_by_xpath(self.email).send_keys(user_email)
            time.sleep(2)
        except Exception as e:
            print("unable to find the element",e)  
    def enter_pass(self,user_pass):
        try:
            time.sleep(2)
            
            self.driver.find_element_by_xpath(self.password).send_keys(user_pass)
            time.sleep(2)
        except Exception as e:
            print("unable to find the element",e) 
            
            
                            