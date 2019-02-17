## jfs stands for getting jobs from sitemap.xml

from selenium import webdriver
import sys
import chilkat
import bs4
import os
import lxml
import time

driver = webdriver.Chrome(executable_path='C:/Users/Ambuj sahu/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')
driver.get('https://www.careerbuilder.co.in/sitemap.xml')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()


soup = bs4.BeautifulSoup(res,'xml')
count =1
for url in soup.find_all('loc'):
    print(count,' >> ',url.text)
    time.sleep(4)

    driver = webdriver.Chrome(executable_path='C:/Users/Ambuj sahu/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')
    driver.get(url.text)
    res1 = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    s = bs4.BeautifulSoup(res1,'lxml')

    all_job_list = s.find_all('div',{'class':'job'})
    count +=1



    if all_job_list == None:
        print('None joblists')
        continue





    city = url.text.split("/")[-1]
    print('above link provide jobs in ',city,'\n\n')

    count2 =1
    for job in all_job_list:
        time.sleep(4)
        
        title = job.find('a',{'class':'job-title'})
        if title == None:
            print('None-title')
            continue
        name = job.find('div',{'class':'snapshot'})
        compname = name.find('a')


        print(count2,'>>>',title.text)
        print('>>>>companyname- ',compname.text)
        print('----------------\n')
        count2+=1
        time.sleep(4)
