#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.common.by import By

import time
df = pd.read_excel("item.xlsx",headers=False)
path ="C:\Program Files (x86)\chromedriver.exe"
url = "https://www.google.com/imghp?hl=EN"
driver = webdriver.Chrome(path)
n=0
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="sbtc"]/div/div[2]/input').send_keys("item" + "\n")
for item in df["product"]:
    try:
        driver.find_element(By.XPATH,'//*[@id="REsRA"]').clear()
        driver.find_element(By.XPATH,'//*[@id="REsRA"]').send_keys(item + "\n")
    except:
        print("refrish")
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('r').key_up(Keys.CONTROL).perform()
        try:
            driver.find_element(By.XPATH,'//*[@id="REsRA"]').clear()
            driver.find_element(By.XPATH,'//*[@id="REsRA"]').send_keys(item + "\n")
        except:
            driver.get(url)
            driver.find_element(By.XPATH,'//*[@id="sbtc"]/div/div[2]/input').send_keys("item" + "\n")
            print("NoSuchWindowException even after refresh")
            n+=1
            continue
    try:
        image=driver.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute("src")
        df.loc[n,"Image"]= image 
    except:
        df.loc[n,"Image"]= "wrong"
    print(n)
    n+=1


# In[ ]:





# In[11]:


df.tail()


# In[12]:


df.to_csv('first_1000.csv')


# In[ ]:




