# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:09:28 2021

@author: nkonijeti

Install the requirements by running below command in cmd before running this script
pip3 install -r requirements.txt
"""

from selenium import webdriver
import re,time
import matplotlib.pyplot as plt
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

y=int(input("Enter the browser you want to use 1.Chrome | 2.Firefox | 3.Edge : "))
x=input("Enter your registered 10-digit zomato mobile number: ")

if(y==1):
    browser = webdriver.Chrome(ChromeDriverManager().install())
elif(y==2):
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif(y==3):
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())

browser.get('https://www.zomato.com/andover-ma')
print("Opened zomato homepage")
time.sleep(15)

# Click on Login
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/header/nav/ul[2]/li[2]/a").click()
print("Clicked on Login button")
time.sleep(5)

# Click on country code
browser.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/div[1]/div/div/div/div[1]/div/span").click()
print("Clicked on country code")
time.sleep(3)

# Change country code to India
browser.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/div[1]/div/div/div/div[2]/div[1]/div/p").click()
print("Provided +91 country code")
time.sleep(3)

# Change mouse pointer to text section to provide mobile number
text_area = browser.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/div[1]/div/input")
time.sleep(3)

# Providing mobile number
text_area.send_keys(x)
print("Provided given mobile number")
time.sleep(3)

# Click on Send OTP
browser.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/button/span/span").click()
print("Clicked on Send OTP")
print("Please enter the OTP(s) sent to given mobile number(and e-mail if applicable) in the browser")
time.sleep(90)

# Click on Profile
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/header/nav/ul[2]/li[2]/div/div/div[1]/span").click()
print("Clicked on your zomato username")
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/header/nav/ul[2]/li[2]/div/div/div[2]/div[1]/div").click()
print("Clicked on Profile button")
time.sleep(10)

# Open zomato Order History webpage
browser.get(browser.current_url[:-7]+"ordering")
print("Opened zomato Order History webpage")
time.sleep(10)

sum1=0
flag=0
list1=[]
list2=[]
list3=[]

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)   
try:     
    str1=browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[2]/div[2]/section/div/div[2]/div[1]").text
except:
    pass

print("Processing the orders in Page-1")
try:
    for k in range(1,11):
        list1.append(browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div[2]/div[2]/section/div/div[1]/div["+ str(k)+ "]/div/div[2]/div[2]/p[2]").text)
        list1[k-1]=float(list1[k-1][1:].replace(',', ''))
        list2.append(list1[k-1])
        sum1+=list1[k-1]
except:
    flag=1
    print("Total money spent in Zomato: Rs." + str(sum1))

if(flag==0):   
    # Calculate total no.of orders
    result = re.search('of(.*)orders', str1)
    result=int(result.group(1))
    print("Total no.of orders: " + str(result))
    
    #Calculate the total no.of sub wepages for orders
    if((result%10)!=0):
        result=(result//10)+2
    else:
        result=(result//10)+1
    time.sleep(5)

    # Collect the price for each order in further pages and calculate the sum
    for i in range(2,result):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        browser.find_element_by_link_text(str(i)).click()
        print("Processing the orders in Page-" + str(i))
        time.sleep(5)
        list1=[]
        browser.execute_script("window.scrollTo(0,0)")
        time.sleep(5)
        try:
            for j in range(1,11):
                list1.append(browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div[2]/div[2]/section/div/div[1]/div["+ str(j) +"]/div/div[2]/div[2]/p[2]").text)
                list1[j-1]=float(list1[j-1][1:].replace(',', ''))
                list2.append(list1[j-1])
                sum1+=list1[j-1]
        except:
            break
        
    print("Total money spent in Zomato: Rs." + str(sum1))

for m in range(len(list2),0,-1):
    list3.append(m)

fig = plt.figure(figsize = (15, 5))
 
# creating the bar plot
plt.bar(list3, list2, color ='maroon', width = 0.4)
 
plt.ylabel("Cost")
plt.xlabel("Order Number")
plt.title("Cost comparision for orders in Zomato")
plt.show()