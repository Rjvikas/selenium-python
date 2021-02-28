'''
Created on Dec 23, 2020

@author: Vikas
'''
from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys 
from pageobjectmodels.villinger.login import Login 

user_password="9889136912"
email="vikas.mishrabbd13@gmail.com"
print("sample test case started") 

expected_result="Vikas Mishra" 

page=Login(webdriver)
page.setupClass()

page.enter_email(email)
page.enter_pass(user_password)
actual_result=page.click_villinger()
print(actual_result)
 
if  expected_result==actual_result:
     
    print("sample test case successfully completed")  
else:
    print("sample test case failed") 