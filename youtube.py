import pandas as pd 

df = pd.read_csv("Content 2023-01-01_2023-04-02 Cretivox - Table data.csv")
datayt = []
# content = df['Content']
# print(df)
total = df.iloc[0]
# print(len(df.index))

for i in range(1,len(df.index)):
    x = df.iloc[i]
    jsyt = {
        "Content":x["Content"],
        "Video_title":x["Video title"],
        "Video_publish":x["Video title"],
        "Shares": x["Shares"],
        "Subscribers_lost": x["Subscribers lost"],
        "Subscribers_gain":x["Subscribers gained"],
        "Views":x["Views"],
        "Watch_time":x["Watch time (hours)"],
        "Subscribers":x["Subscribers"],
        "Impression":x["Impressions"],
        "impressions_click" : x["Impressions click-through rate (%)"]
    }
    datayt.append(jsyt)





jstotal = [{
    "id" : 1,
    "total_share" : total["Shares"],
    "total_sub_lost" : total["Subscribers lost"],
    "total_sub_gained" : total["Subscribers gained"],
    "total_views" : total["Views"],
    "total_watch_time" : total["Watch time (hours)"],
    "total_sub" : total["Subscribers"],
    "total_impressions" : total["Impressions"],
    "total_impressions_click" : total["Impressions click-through rate (%)"],
    "notes" : "noted",
    "data" : datayt
    
}]

print(jstotal)

