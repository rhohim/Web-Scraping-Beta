# import requests
# from bs4 import BeautifulSoup 

# url = "https://shopee.co.id/search?keyword=kaos%20polos"
# response = requests.get(url) 
# soup = BeautifulSoup(response.text, 'lxml')

# print(soup)


from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By

df_month = pd.DataFrame(columns=['Title', 'Total', 'Price', 'Location'])
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/80.0.3987.132 Safari/537.36'
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.maximize_window()
# print("Input Keyword : ")
# keyword = input("Input Keyword : ")
# keyword = "celana kargo"

# #input KEYWORD
keywordlist = [ "celana cino panjang", "celana cino pendek", "celana kargo panjang", "celana kargo pendek",
               "celana pendek santai", "celana angkle pants", "celana jeans denim panjang", 
               "celana sweat pants panjang" , "celana sweat pants pendek" ,  
               "kemeja panjang lacoste" , "kemeja pendek lacoste", "kemeja panjang", "kemeja pendek", 
               "kemeja v neck", "kemeja panjang kerah atas", "flanel", "polo shirt", "kaos polos"
               , "kaos polos oversize", "hoodie polos", "crew neck", "outer pria"]
# keywordlist = ["Earphone Wireless" ]

for keyword in keywordlist:
    df_month = pd.DataFrame(columns=['Title', 'Total', 'Price', 'Location'])
    key = keyword.split()
    print(key)
    y, w = [] , []
    if len(key) < 2 :
        url = "https://shopee.co.id/search?keyword=" + keyword
        w.append(key[0])
    else:
        for x in key:
            y.append(x)
            w.append(x)
            y.append("%20")
            w.append("-")
        y.pop()
        w.pop()
        print(''.join(y))
        url = "https://shopee.co.id/search?keyword=" + ''.join(y)
    print(url)
    textdata = []
    driver.get(url)
    time.sleep(15)
    div_element = driver.find_element(By.XPATH, "//div[text()='Terlaris']")
    time.sleep(15)
    div_element.click()
    time.sleep(7)
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(1000, 2000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(2000, 3000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(3000, 4000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(4000, 5000);")
    time.sleep(4)
    div_elements = driver.find_elements(By.CLASS_NAME,"col-xs-2-4")


    x = 0
    for i in range(len(div_elements)):
        print(str(i) + "\n")
        print(div_elements[i].text + "\n")
        spl = div_elements[i].text.split("\n")
        # print(len(spl))
        # print(spl[0])
        if spl[0] == "Star":
            if spl[1] == "Ad":
                print("start > ad \n")
                print(spl[2])
                title = spl[2]
            elif spl[3] == "Ad":
                print("start > % > off > ad\n")
                print(spl[3])
                title = spl[4]
            else:
                print("start / start > % > off\n")
                if spl[2] == "OFF":
                    print(spl[3])
                    title = spl[3]
                else:
                    print(spl[1])
                    title = spl[1]
            # print("star######")
        elif len(spl) == 1:
            print("empty")
            x+=1
        elif spl[0] == "Ad":
            print("Ad\n")
            print(spl[1])
            title = spl[1]
        elif spl[1] == "OFF":
            if spl[2] == "Ad":
                print("% > off > ad\n ")
                print(spl[3])
                title = spl[3]
            else:
                print("% > off \n")
                print(spl[2])
                title = spl[2]
        else:
            print("clear#####\n")
            print(spl[0]) 
            title = spl[0]
        
        # print(spl[len(spl)-1])
        # print(spl[len(spl)-2])
        total = spl[len(spl)-2]
        location = spl[len(spl)-1]
        price = spl[len(spl)-3].split(" ")
        print(price)
        if len(price) < 2:
            # print(price[0])
            prc = price[0]
        elif len(price) == 2:
            prc = spl[len(spl)-4]
        else:
            # print(price[2])
            prc = price[2]
        
            
        df_month = df_month.append({'Title': title,'Total': total, 'Price': prc,'Location': location}, ignore_index=True)

    df_month.to_csv('G:/CrevHim/Code/software/test/testall/shopee/' + ''.join(w) + '.csv', encoding='utf-8')
    print(x)
    
driver.quit();