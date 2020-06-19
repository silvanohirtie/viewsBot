import os
from pathlib2 import Path
#Importing selenium and all the stuff we need
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from userAgents import agents
import random
from random import randrange
import os
import time

current_path = os.path.dirname(os.path.realpath(__file__))
links_n = 0
for line in open((current_path+'/links.txt')).readlines(  ): 
    links_n += 1
print("File has",links_n,"links")


path = Path(current_path+'/links.txt')
text = path.read_text()
text = text.replace("aff_c", "aff_l")
path.write_text(text)


botCount = 0
chooseAgent = ""
agentPrint = input("What Agent do you want to use? [iPhone, Android, Random]: ")
if(agentPrint == "Android"):
    chooseAgent = "user-agent=Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19"
elif(agentPrint == "iPhone"):
    chooseAgent = "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

links = open(current_path+'/links.txt').read().splitlines()
to_use = 0
while True: #Loop
    url = links[to_use]
    if(agentPrint == "Random"):
        chooseAgent = random.choice(agents) #Take random choice from the agents array
    botCount +=1
    print("Bot N.",botCount)
    print("Url: ",url)
    lines = open(current_path+'/proxies.txt').read().splitlines() #Open the proxies.txt file and read all the lines
    chooseProxy = random.choice(lines) #Choose a random line
    print("Proxy: ",chooseProxy)
    print(chooseAgent)

    #Options
    opts = Options()
    opts.add_argument(chooseAgent) 
    opts.add_experimental_option('excludeSwitches', ['enable-logging']) #Disable useless logs in the console
    opts.add_argument('--proxy-server=%s' % chooseProxy) #Set proxy
    opts.add_argument('headless') #Make it run in background
    driver = webdriver.Chrome(current_path+"/chromedriver.exe",options=opts) #Select WebDriver
    driver.set_page_load_timeout(15) #Setting a 15 seconds timeout
    try:
        driver.get(url) #Fire the url
        time.sleep(2) #Wait 2 seconds
    except TimeoutException as ex:
        print("Proxy is taking too much time...")
    else:
        print(u"\u001b[32;1mDone!\u001b[0m")
        
    print("Cleaning Cookies")
    driver.delete_all_cookies() #Clean the cookies
    print("Cookie cleaned, exiting..\n")
    driver.quit() #exit
    to_use+=1
    if int(counter) > int(maxloop):
        print("Finished!")
        break
