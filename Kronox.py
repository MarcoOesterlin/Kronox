from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import SessionNotCreatedException

"""
Scriptet måste köras med Mozilla Firefox, och geckodriver inlagd i PATH
"""





options = Options()
driver = webdriver.Firefox(options=options)
print ("Headless Firefox Initialized")
options.headless = True
css = driver.find_element_by_css_selector
xpath = driver.find_element_by_xpath
classname = driver.find_element_by_class_name
name = driver.find_element_by_name
id = driver.find_element_by_id


def main():

    username = "JohnDoe"
    password = "Password"


    driver.get("https://schema.mau.se/index.jsp")
    classname('signin').click()
    name('username').send_keys(username)
    name('password').send_keys(password)
    id('login_button').click()
    xpath("/html/body/div[1]/div[2]/div/div/ul/li[9]/a").click()
    Niagara_10_13(username)


def Niagara_10_13(username):
    for i in range(2,24):
        try:
            if i == 23:
                print("Inga Lediga Tider")
                driver.close()
                driver.quit()
            else:
                css(".grupprum-table>tbody:nth-child(1)>tr:nth-child({})>td:nth-child(3)>a:nth-child(1)".format(i)).click()
                css("#moment").click()
                css("#moment").send_keys(username)
                xpath("/html/body/div[3]/div[11]/div/button[2]").click()
                print("Success")
                driver.quit()
                break
        except ElementNotInteractableException:
            continue
        except NoSuchElementException:
            continue
        except SessionNotCreatedException:
            continue
"""
def book15to17Niagara():
    for i in range(2,24):
        try:
            print(i)
            if i == 23:
                print("Inga Lediga Tider")
                driver.close()
                driver.quit()
            css(".grupprum-table>tbody:nth-child(1)>tr:nth-child({})>td:nth-child(4)".format(i)).click()
            css("#moment").click()
            css("#moment").send_keys("mm")
            xpath("/html/body/div[3]/div[11]/div/button[2]").click()
            print("Success")
            driver.quit()
            break
        except ElementNotInteractableException:
            continue
        except NoSuchElementException:
            continue
        except SessionNotCreatedException:
            continue
"""
main()
