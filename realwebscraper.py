from selenium import webdriver

from time import sleep



name = "http://ebooks.damsdelhi.com/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg"
path_to_chromedriver = r'C:\Users\game\Desktop\chromedriver_win32\chromedriver'
browser = webdriver.Chrome(executable_path= path_to_chromedriver)
url = "http://ebooks.damsdelhi.com/reader/86e66e8bd6b73694a5a38387667b28c9?loginMsg=1#@db71d46250293dbf90188dfaef39058b1%next"
browser.get(url)
uname= browser.find_element_by_name("email")
passw = browser.find_element_by_name("password")
uname.send_keys("GN108669")
sleep(1)
passw.send_keys("5QAGJRFM")
passw.submit()
print(browser.current_url)
browser.save_screenshot("test1.png")
for x in range(1,355):
    name = '//div[text()="Page ' + str(x) + '/355"]'
    browser.find_element_by_xpath(name).click()
    sleep(5)
    browser.save_screenshot(str(x) + ".png")








                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bge5.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg64.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg3e.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg2.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg4.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg5.jpg">
                                            #<img class="bi x0 y0 w0 h0" alt="" src="/reader/25f5fb2eed7f3de888fb04ea0d3edd18/assets/bg4.jpg">

