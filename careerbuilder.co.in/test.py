from selenium import webdriver
import sys
import chilkat
import bs4
import os
import lxml


url = 'https://www.careerbuilder.co.in/jobsearch'
driver = webdriver.Chrome(executable_path='C:/Users/Ambuj sahu/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')
driver.get(url)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()



soup = bs4.BeautifulSoup(res,'lxml')
all_job_list = soup.find_all('div',{'class':'job'})
city = url.split("/")[-1]
print('above link provide jobs in ',city,'\n\n')
count2 =1
for job in all_job_list:


    title = job.find('a',{'class':'job-title'})
    if title == None:
        continue
    name = job.find('div',{'class':'snapshot'})
    compname = name.find('a')


    print(count2,'>>>',title.text)
    print('>>>>companyname- ',compname.text)
    print('----------------\n')



    count2+=1
