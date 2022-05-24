from asyncore import write
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Username = str(input("Enter your username>>"))
# Password = str(input("Enter your password>>"))
print("\t\tYOU ARE ALL SET!!\n\tKEEP WORKING YOUR TIME IS PRECIOUS\nI will like all your new feed posts of instagram until you close me")
sleep(8)
while True:
    try:
        driver = webdriver.Firefox(executable_path="/home/daffolap-1025/Desktop/my files/python/geckodriver")
        driver.implicitly_wait(20)
        driver.get("https://github.com/")
        sleep(4)


        notnow = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
        notnow.click()
        sleep(2)
        driver.find_element_by_name("login").send_keys("deepu84")
        driver.find_element_by_name("password").send_keys("DeepuCoder@#0")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep (2)

        notnow = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/span[1]')
        notnow.click()
        sleep(2)
        notnow = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]')
        notnow.click()
        sleep(2)
        notnow = driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[1]')
        notnow.click()
        sleep(2)



        while True:
            notnow = driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a')
            notnow.click()
            sleep(2)
            notnow = driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[2]/div/a[1]')
            notnow.click()
            sleep(2)

            for i in range(1,50):
                try:
                    notnow = driver.find_element(by=By.XPATH, value='/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div['+str(i)+']/div[3]/span/form[1]')
                    notnow.click()
                    s = '/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div['+str(i)+']/div[3]/span/form[1]/input[2]'
                    print(s)
                    notnow = driver.find_element_by_xpath('/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div['+str(i)+']/div[3]/span/form[1]/input[2]')
                    notnow.click()
                    sleep(1)
                except:
                    pass
            
            notnow = driver.find_element(by=By.XPATH, value='/html/body/div[5]/main/div[2]/div/div[2]/div[2]/div/div[51]/div/a')
            notnow.click()
            sleep(300)
    except:
        pass
