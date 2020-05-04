import requests
import tkinter as tk
from PIL import Image, ImageTk
import json 

app = tk.Tk()
app.title('Corona Tracker')
app.wm_iconbitmap('icon.ico')
HEIGHT = 500
WIDTH = 600

def format_response(weather_json):
    try:
        country = weather_json["data"]['covid19Stats'][0]["country"]
        lastUpdate = weather_json["data"]['covid19Stats'][0]["lastUpdate"]
        confirmed = weather_json["data"]['covid19Stats'][0]["confirmed"]
        deaths = weather_json["data"]['covid19Stats'][0]["deaths"]
        recovered = weather_json["data"]['covid19Stats'][0]["recovered"]
        final_str = 'Country: %s \nLastUpdated: %s \nConfirmed : %s \nDeaths : %s \nRecovered: %s ' % (country,lastUpdate, confirmed,deaths,recovered)
    
    except:
        final_str = 'There was a problem retrieving that information'
    #final_str = 'hello'
    return final_str

def get_details(ans):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats" 
    ans2= ans.capitalize()
    querystring = {"country":ans2,"format":"undefined"}


    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "d09ecb5585mshbf1cb6dfd23f20cp143727jsn1e892a16518b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    weather_json = response.json()
    results['text'] = format_response(response.json())


C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image= tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()


frame = tk.Frame(app,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#frame_window = C.create_window(100, 40, window=frame)


textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Check', font=40,command=lambda:get_details(textbox.get()) )
#submit.config(font=)
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)




app.mainloop()



""" def get_details():
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats" 
    ans = input("Enter the country name")
    ans2= ans.capitalize()
    querystring = {"country":ans2,"format":"undefined"}


    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "d09ecb5585mshbf1cb6dfd23f20cp143727jsn1e892a16518b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = json.loads(str(response.text))
    country = res["data"]['covid19Stats'][0]["country"]
    lastUpdate = res["data"]['covid19Stats'][0]["lastUpdate"]
    confirmed = res["data"]['covid19Stats'][0]["confirmed"]
    deaths = res["data"]['covid19Stats'][0]["deaths"]
    recovered = res["data"]['covid19Stats'][0]["recovered"]
    #print(res)
    print(country ,lastUpdate,confirmed,deaths,recovered)

get_details()

 """

