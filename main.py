import argparse
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import random
from selenium.webdriver.firefox.options import Options
import os.path
i = 0

#------------------------------Parser args--------------------------------------------------
def opcije():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Username nad kojim zelimo izvrsiti skriptu",required=True)
    parser.add_argument("-u","--user",dest="user",help="Instagram Username")
    parser.add_argument("-p","--pass",dest="password",help="Instagram Password")
    parser.add_argument("--files", dest="usersfile",help="Odaberi File za bazu")
    parser.add_argument("-l","--like",dest="like",help="Like sve slike", action="store_true")
    parser.add_argument("-f","--follow",dest="follow",help="Odaberi za follow",action="store_true",default=False)
    odabir = parser.parse_args()
    if odabir.target and odabir.follow is False and odabir.like is False and odabir.usersfile is None:
        parser.error("Mora te izabrati radnju (-h za pomoć) ")
    if (odabir.follow or odabir.like) and odabir.usersfile is None and(odabir.user is None or odabir.password is None):
        parser.error("Mora te odabrati Username i Password, (-u, -p)")
    if odabir.usersfile and(odabir.follow is False and odabir.like is False):
        parser.error("Mora te odabrati follow ili like(-f, -l)")
    return odabir
#-------------------------------------------------------------------------------------------

#-----------------------------odabir && start browser---------------------------------------
odabir = opcije()
binary = FirefoxBinary('')
browser = webdriver.Firefox(firefox_binary=binary, executable_path="")
browser.implicitly_wait(5)
browser.get("https://www.instagram.com")
sleep(3)
#-------------------------------------------------------------------------------------------
#----------------------------------Fileov users---------------------------------------------
def skirpta_useri(fileovi, broj):
    file = open(fileovi)
    content = file.read()
    file.close()
    users = content.split(";")[broj]
    user1 = users.split(",")[0]
    pass1 = users.split(",")[1]
    return user1,pass1;
#-------------------------------------------------------------------------------------------


#---------------------------------------Login def-------------------------------------------
def login(username, password):
     #--------------------------------Unos Podataka--------------------------------
     username_input = browser.find_element_by_css_selector("input[name='username']")
     password_input = browser.find_element_by_xpath("//input[@type='password']")
     username_input.send_keys(username)
     password_input.send_keys(password)
     sleep(0.3)
     #------------------------------------------------------------------------------



     #--------------------------------Buttoni---------------------------------------

     login_butt = browser.find_element_by_xpath("//button[@type='submit']")
     login_butt.click();
     sleep(2)
     not_now = browser.find_element_by_xpath("//button[text()='Not Now']")
     not_now.click();
     sleep(1)
     not_now = browser.find_element_by_xpath("//button[text()='Not Now']")
     not_now.click();
     sleep(1)
     #------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------



#---------------------------------------Follow def-------------------------------------------
def follow(target):
    link = "https://www.instagram.com/" + target
    browser.get(link)
    follow_button = browser.find_element_by_css_selector("._6VtSN")
    follow_button.click()
    sleep(0.3)
    try:
        cancel_button = browser.find_element_by_xpath("//button[text()='Cancel']")
        if cancel_button:
            cancel_button.click()
    except:
        pass
    sleep(0.5)
#--------------------------------------------------------------------------------------------

#-------------------------------------Like posts---------------------------------------------
def like():
    a = 0
    posts = browser.find_elements_by_css_selector("a[href*='/p/']")
    links = [elem.get_attribute('href') for elem in posts]
    for link in links:
        random_time_addon = random.random()

        browser.get(link)
        sleep(2 + random_time_addon)
        check_btn = browser.find_element_by_css_selector(".fr66n .QBdPU ._8-yf5 ")
        if check_btn.get_attribute('aria-label') == "Unlike":
            pass

        elif check_btn.get_attribute('aria-label') == "Like":
            like_btn = browser.find_element_by_css_selector(".fr66n .wpO6b")
            like_btn.click()
        sleep(0.5 + random_time_addon)
#--------------------------------------------------------------------------------------------

#---------------------------------------Logout def-------------------------------------------
def logout():
    span_lg_btn = browser.find_element_by_xpath("//span[@tabindex='0']")
    span_lg_btn.click()
    sleep(0.3)
    logout_btn = browser.find_element_by_xpath("//div[text()='Log Out']")
    logout_btn.click()
    sleep(0.5)
#--------------------------------------------------------------------------------------------








#-----MAIN------MAIN--------MAIN---------MAIN------MAIN------MAIN--------MAIN--------MAIN
if odabir.usersfile and odabir.follow and odabir.like is False:
    if os.path.isfile(odabir.usersfile):
        try:
            while True:
                user1, pass1 = skirpta_useri(odabir.usersfile, i)
                login(user1,pass1)
                follow(odabir.target)
                logout()
                i+=1

        except:
            print("Program završen...")
    else:
        print("File nije pronađem...")
        exit()
elif odabir.usersfile and odabir.follow and odabir.like:
    if os.path.isfile(odabir.usersfile):
        try:
            while True:
                user1, pass1 = skirpta_useri(odabir.usersfile, i)
                login(user1,pass1)
                follow(odabir.target)
                like()
                logout()
                i+=1

        except:
            print("Program završen...")
    else:
        print("File nije pronađen...")
        exit()
elif odabir.usersfile and odabir.follow is False and odabir.like:
    if os.path.isfile(odabir.usersfile):
        try:
            while True:
                user1, pass1 = skirpta_useri(odabir.usersfile, i)
                login(user1,pass1)
                like()
                logout()
                i+=1

        except:
            print("Program završen...")
    else:
        print("File nije pronađen...")
        exit()




if odabir.follow and odabir.like is False and odabir.usersfile is None:
    login(odabir.user, odabir.password)
    follow(odabir.target)
elif odabir.like and odabir.follow is False and odabir.usersfile is None:
    login(odabir.user, odabir.password)
    like()
elif odabir.follow and odabir.like and odabir.usersfile is None:
    login(odabir.user, odabir.password)
    follow(odabir.target)
    like()




#binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
#browser = webdriver.Firefox(firefox_binary=binary, executable_path="C:/Users/salih/Desktop/Python/geckodriver.exe")
#browser.implicitly_wait(5)
#browser.get("https://instagram.com")
