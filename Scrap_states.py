from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import wget
from tqdm import tqdm
import time 
import pandas as pd
import datetime


PATH="./Projects/Selenium/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://statesymbolsusa.org/categories/flower")
time.sleep(1)
element_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li[1]"
state_name_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li[1]/div[2]/span/a"
flower_name_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li[1]/div[3]/span/a"
image_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li[1]/div[1]/div/a/img"

state_names=[]
flower_names=[]
image_filenames=[]

for i in tqdm(range(62)):
    
    state_name_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li["+str(i+1)+"]/div[2]/span/a"
    flower_name_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li["+str(i+1)+"]/div[3]/span/a"
    image_xpath="//*[@id=\"block-views-symbols-block-16\"]/div/div/div/div/div/ul/li["+str(i+1)+"]/div[1]/div/a/img"
    
    # Get states names
    state_name=driver.find_element_by_xpath(state_name_xpath).text
    state_names.append(state_name)
    
    # Get flowers names
    flower_name=driver.find_element_by_xpath(flower_name_xpath).text
    flower_names.append(flower_name)
    
    #Get images of the flower
    img=driver.find_element_by_xpath(image_xpath)
    src = img.get_attribute('src')
    
    image_filename = wget.download(src)
    image_filenames.append(image_filename)
    


data3=pd.DataFrame(columns=['State','Flower','img'])
data3['State']=state_names
data3['Flower']=flower_names
data3['img']=image_filenames
data3.to_csv('data3.csv',index=False)


driver.get("https://worldpopulationreview.com/states/state-capitals")
time.sleep(1)
states=[]
populations=[]

for i in range(50):
    
    
    states.append(driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr["+str(i+1)+"]/td[2]").text)
    populations.append(driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr["+str(i+1)+"]/td[3]").text)

data2=pd.DataFrame(columns=['States','Populations'])
data2['States']=states
data2['Populations']=populations
data2.to_csv('data2.csv',index=False)

data1=pd.read_csv('data.csv')
data2=pd.read_csv('data2.csv')
data3=pd.read_csv('data3.csv')
data=data1.merge(data3,left_on='State',right_on='State').drop_duplicates(subset=['State'])
data=data.merge(data2,left_on='State',right_on='States')[['State','Capital','Populations','Flower_x','img']]
pop=data['Populations']
popf=[float(x.replace(',','')) for x in pop]
data['Populations']=popf
data=data.rename(columns={"Populations":"Population","Flower_x":"Flower"})

data.to_csv('data_all.csv',index=False)