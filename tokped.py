from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
import csv


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/80.0.3987.132 Safari/537.36'
driver = webdriver.Chrome()
driver.maximize_window()
# print("Input Keyword : ")
# keyword = input("Input Keyword : ")
# keyword = "kaos polos"
# keywordlist = ["Laptop", "Wireless Mouse", "Mouse Kabel", "Mouse Bluetooth", "Laptop Stand", 
#                "Webcam", "Meja Laptop", "Wired Keyboard", "Laptop Vacuum", "Cooling Pad", 
#                "Writing Tablet LCD", "Mouse Pad", "Mini Keyboard Wireless", "Tas Laptop", 
#                "Wireless Keyboard", "Gaming Chair", "Kursi Kerja", "Keyboard Gaming", 
#                "Mouse Gaming", "Headset Gaming", "Mini PC", "Laptop Gaming"]

keywordlist = ["film polaroid 600"]
datatokped = []


for keyword in keywordlist:
    df_month = pd.DataFrame(columns=['Title', 'Total', 'Price', 'Location'])
    key = keyword.split()
    print(key)
    y, w = [] , []
    if len(key) < 2 :
        url = "https://www.tokopedia.com/search?st=product&q=" + keyword
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
        url = "https://www.tokopedia.com/search?st=product&q=" + ''.join(y)
    print(url)
    textdata = []
    driver.get(url)
    time.sleep(10)
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
    driver.execute_script("window.scrollTo(5000, 6000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(6000, 7000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(7000, 8000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(8000, 9000);")
    time.sleep(4)
    button = driver.find_element(By.XPATH, '//*[@id="zeus-root"]/div/div[2]/div/div[2]/div[5]/nav/ul/li[3]/button')
    button.click()  
    time.sleep(6)
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
    driver.execute_script("window.scrollTo(5000, 6000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(6000, 7000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(7000, 8000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(8000, 9000);")
    time.sleep(4)
    div_elements = driver.find_elements(By.CLASS_NAME,"css-54k5sq")
    # # print(len(div_elements))
    # # print(div_elements[0].text + "\n")


    x = 0
    for i in range(len(div_elements)):
        print(len(div_elements)) 
        # print("Product No " + str(i) + "\n")
        spl = div_elements[i].text.split("\n")
        datatokped.append(spl)
        # print(spl)
    file_name = 'scraping_output_film polaroid 600 2.csv'
    with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(datatokped)
        
        # if len(spl) == 6 :
        #     # pass
        #     # print(div_elements[i].text + "\n")
        #     # print(spl)
        #     print("length desc " + str(len(spl)) + "\n")
            
            
            # if spl[0] == "Ad":
            #     print(spl[1])
            #     print(spl[len(spl)-3])
            #     print(spl[len(spl)-4])
            #     print(spl[len(spl)-1] + "\n")
                
            #     title = spl[1]
            #     location = spl[len(spl)-3]
            #     price = spl[len(spl)-4]
            #     total = spl[len(spl)-1]
            # else:
            #     print(spl[0])
            #     print(spl[len(spl)-4])
            #     print(spl[len(spl)-5])
            #     print(spl[len(spl)-1] + "\n")
                
            #     title = spl[0]
            #     location = spl[len(spl)-4]
            #     price = spl[len(spl)-5]
            #     total = spl[len(spl)-1]
                
    #     elif len(spl) == 7 :
    #         pass
    #         print("\n" + div_elements[i].text + "\n")
    #         print("length desc " + str(len(spl)) + "\n")
    #         x = spl[0].split(" ")
    #         print(len(x))
    #         if len(x) <= 3 :
    #             print(spl[1])
    #             print(spl[2])
    #             print(spl[3])
    #             print(spl[len(spl)-1] + "\n")
                
    #             title = spl[1]
    #             location = spl[3]
    #             price = spl[2]
    #             total = spl[len(spl)-1]
                
    #         else:
    #             print(spl[0])
    #             print(spl[1])
    #             print(spl[3])
    #             print(spl[len(spl)-1] + "\n") 
                
    #             title = spl[0]
    #             location = spl[3]
    #             price = spl[1]
    #             total = spl[len(spl)-1]
                
    #     elif len(spl) == 8 :
    #         pass
    #         print("\n" + div_elements[i].text + "\n")
    #         print("length desc " + str(len(spl)) + "\n")
    #         x = spl[0].split(" ")
            
    #         if len(x) <= 3 :
    #             print(len(x) ," <=3")
    #             x = spl[1].split(" ")
    #             if len(x) <= 3 :
    #                 print(x)
    #                 print(spl[2])
    #                 print(spl[3] )
    #                 print(spl[len(spl)-4] )
    #                 print(spl[len(spl)-1] + "\n")
                    
    #                 title = spl[2]
    #                 location = spl[len(spl)-4] 
    #                 price = spl[3]
    #                 total = spl[len(spl)-1]
    #             else:
    #                 print(x)
    #                 print(spl[1])
    #                 print(spl[2])
    #                 print(spl[len(spl)-4] )
    #                 print(spl[len(spl)-1] + "\n")
                    
    #                 title = spl[1]
    #                 location = spl[len(spl)-4] 
    #                 price = spl[2]
    #                 total = spl[len(spl)-1]
                    
    #         else:
    #             print(spl[1])
    #             print(spl[2] )
    #             print(spl[len(spl)-4] )
    #             print(spl[len(spl)-1] + "\n")
    #     elif len(spl) == 9 :
    #         pass
    #         print(div_elements[i].text + "\n")
    #         print("length desc " + str(len(spl)) + "\n")
    #         x = spl[0].split(" ")
            
    #         if len(x) <= 3:
    #             x = spl[1].split(" ")
    #             if len(x) <= 3:
    #                 print("<====3")
    #                 print(spl[2])
    #                 print(spl[3])
    #                 print(spl[len(spl)-4] )
    #                 print(spl[len(spl)-1] + "\n")
                    
    #                 title = spl[2]
    #                 location = spl[len(spl)-4] 
    #                 price = spl[3]
    #                 total = spl[len(spl)-1]
                    
                    
    #             else:
    #                 print(spl[1])
    #                 print(spl[4])
    #                 print(spl[len(spl)-4] )
    #                 print(spl[len(spl)-1] + "\n")
                    
    #                 title = spl[1]
    #                 location = spl[len(spl)-4] 
    #                 price = spl[4]
    #                 total = spl[len(spl)-1]
    #     else:
    #         print(div_elements[i].text + "\n")
    #         print("length desc " + str(len(spl)) + "\n")
    #         x = spl[0].split(" ")
    #         if len(x) <= 3:
    #             x = spl[1].split(" ")
    #             if len(x) <= 3:
    #                 print("<====3")
    #                 print(spl[2])
    #                 print(spl[len(spl)-5])
    #                 print(spl[len(spl)-4] )
    #                 print(spl[len(spl)-1] + "\n")
                    
    #                 title = spl[2]
    #                 location = spl[len(spl)-4] 
    #                 price = spl[len(spl)-5]
    #                 total = spl[len(spl)-1]
                    
               
        # print(title, total, price, location)        
        # df_month = df_month.append({'Title': title,'Total': total, 'Price': price,'Location': location}, ignore_index=True)
    # df_month.to_csv('G:/CrevHim/Code/software/test/testall/tokped/' + ''.join(w) + '.csv', encoding='utf-8')
    # print(df_month)
    
driver.quit();