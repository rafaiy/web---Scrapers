from selenium import webdriver
from urllib import request,response,error,parse,robotparser

path_to_chromedriver = r'C:\Users\game\Desktop\chromedriver_win32\chromedriver' # change path as needed

browser = webdriver.Chrome(executable_path= path_to_chromedriver)
url = "http://www.google.com"
browser.get(url)
search = browser.find_element_by_id("lst-ib")

search.send_keys("hello world")
submitButton = browser.find_element_
submitButton.submit()

browser.save_screenshot("test.png")
#<input value="Google Search" aria-label="Google Search" name="btnK" type="submit" jsaction="sf.chk">