from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 
import datetime
from playsound import playsound


PATH="C:/Users/YACINE/Documents/Selenium/chromedriver.exe"
html_path="C:/Users/YACINE/Documents/Selenium/Alert.html"

old_table='DIM. LUN. MAR. MER. JEU. VEN. SAM.\n29 30 1 2 3 4 5\n6 7 8 9 10 11 12\n13 14 15 16 17 18 19\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n+2 en plus\n+2 en plus\n+2 en plus\n+2 en plus\n+2 en plus\n20 21 22 23 24 25 26\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n08:00 TCF SO\n+2 en plus\n+2 en plus\n+2 en plus\n+2 en plus\n+2 en plus\n27 28 29 30 31 1 2\n3 4 5 6 7 8 9'



def go_december(drv):
    
    next_button=drv.find_element_by_xpath("//button[@class='fc-next-button fc-button fc-state-default fc-corner-right']")
    next_button.click()
    
    
    
#We want to use chrome and the path to the web driver is path
driver=webdriver.Chrome(PATH)
driver.get("https://portail.if-algerie.com/home#")
time.sleep(1)
email=driver.find_element_by_class_name('form-control')
email.send_keys(emails)
passwd=driver.find_element_by_name('password')
passwd.send_keys(password)
time.sleep(1)
login=driver.find_element_by_id("login")
login.click()
driver.maximize_window() #For maximizing window

time.sleep(10)
tests=driver.find_element_by_link_text('Tests et Examens')
tests.click()
tests2=driver.find_element_by_link_text("S'inscrire")
tests2.click()
time.sleep(1)



tests=driver.find_element_by_link_text('Tests et Examens')
tests.click()
tests2=driver.find_element_by_link_text("S'inscrire")
tests2.click()
time.sleep(1)



while True:
         
        driver.refresh() #Refresh November page
        time.sleep(15) 
        
        #Check if no error happened while going to december
        month=driver.find_element_by_xpath("//div[@class='fc-center']")
        while(month.text=='NOVEMBRE 2020'):
            go_december(driver) #Go to december 
            time.sleep(15)
            month=driver.find_element_by_xpath("//div[@class='fc-center']")
        
        time.sleep(15)
        
        table=driver.find_element_by_xpath("//div[@class='fc-view-container']") #Get december table
        print(table.text==old_table)#Prints True if nothing changed
        
        #Checks if the table changed
        if(table.text!=old_table):
            
            #Open an html alert page 
            driver2=webdriver.Chrome(PATH)
            driver2.get(html_path)

            #Click on the "Alert" button to generate the Simple Alert
            button = driver2.find_element_by_name('alert')
            button.click()

            #Switch the control to the Alert window
            obj = driver2.switch_to.alert

            #Retrieve the message on the Alert window
            msg=obj.text
            print ("Alert shows following message: "+ msg )
            
            #Alert in the PC sound
            while True :
                playsound('ALARM.wav',True)
        
        
        print('CHECK Website at {} ... No Dates'.format(datetime.datetime.now()))
        #Repeat the process every 5min.
        time.sleep(30)