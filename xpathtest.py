from selenium import webdriver

from time import sleep


path_to_chromedriver = r'C:\Users\game\Desktop\chromedriver_win32\chromedriver'
browser = webdriver.Chrome(executable_path= path_to_chromedriver)
url = "http://www.google.com"
browser.get(url)
browser.find_element_by_name("q").send_keys("hello world")

browser.find_element_by_xpath("//input[@value='Google Search']").click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
