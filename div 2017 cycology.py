from selenium import webdriver
from time import sleep

url = "http://ebooks.damsdelhi.com/reader/e2d329b3c8a7359888ae53892253cc60#@c09aa584074630edbfebb214635744891%next"
path_to_chromedriver = r'C:\Users\game\Desktop\chromedriver_win32\chromedriver'
browser = webdriver.Chrome(executable_path= path_to_chromedriver)
browser.get(url)
uname= browser.find_element_by_name("email")
passw = browser.find_element_by_name("password")
uname.send_keys("GN108669")
sleep(1)
passw.send_keys("5QAGJRFM")
passw.submit()
counter = 1
elphabet = ['a','b','c','d','e','f']
nos = ['0','1','2','3','4','5','6','7','8','9']
for x in nos:
    counter += 1
    browser.get('http://ebooks.damsdelhi.com/reader/e2d329b3c8a7359888ae53892253cc60/assets/bg' + str(x)+'.jpg')
    browser.save_screenshot(str(counter) + ".png")
for y in elphabet:
    counter += 1
    browser.get('http://ebooks.damsdelhi.com/reader/e2d329b3c8a7359888ae53892253cc60/assets/bg' + str(y) + '.jpg')
    browser.save_screenshot(str(counter) + ".png")
for x in nos:
    if x is 0:
        continue
    for x1 in nos:
        counter += 1
        browser.get('http://ebooks.damsdelhi.com/reader/e2d329b3c8a7359888ae53892253cc60/assets/bg' + str(x)+ str(x1) + '.jpg')
        browser.save_screenshot(str(counter) + ".png")
    for y1 in elphabet:
        counter += 1
        browser.get('http://ebooks.damsdelhi.com/reader/e2d329b3c8a7359888ae53892253cc60/assets/bg' + str(x) + y1 + '.jpg')
        browser.save_screenshot(str(counter) + ".png")





