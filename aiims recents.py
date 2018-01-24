from selenium import webdriver
from time import sleep

url = "http://ebooks.damsdelhi.com/reader/86e66e8bd6b73694a5a38387667b28c9?loginMsg=1#@db71d46250293dbf90188dfaef39058b1%next"
path_to_chromedriver = r'C:\Users\game\Desktop\chromedriver_win32\chromedriver'
browser = webdriver.Chrome(executable_path= path_to_chromedriver)
browser.get(url)
uname= browser.find_element_by_name("email")
passw = browser.find_element_by_name("password")
uname.send_keys("GN108669")
sleep(1)
passw.send_keys("5QAGJRFM")
passw.submit()
for x in range(1,180):
    sleep(20)
    #element = browser.find_element_by_class_name("icon-arrow-right-5")
    #browser.execute_script("argument[0].click();", element )
    browser.find_element_by_xpath("//div[@id='db71d46250293dbf90188dfaef39058b1']").click()
    browser.implicitly_wait(10)
    name = str(x) + ".png"
    browser.save_screenshot(name)
    browser.find_element_by_xpath("//div[@class='button-next-reader navigation active']").click()
    '''div[@class='button-next-reader navigation active'''
    #browser.execute_script("var myIframe = document.getElementById('iframe');myIframe.onload = function () { myIframe.contentWindow.scrollTo(0,200);}")
    #name = str(x)+"sc.png"
    #browser.save_screenshot(name)
    #browser.find_element_by_xpath("//div[@class='button-next-reader navigation active']").click()
    print(x)







