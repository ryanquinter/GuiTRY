import tkinter as tk
from tkinter import font
import requests

# 9c0304f30d0d55f7d0d81c09e628a82b
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the Entry:", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = (weather['main']['temp'])

        final_str =  'City: %s \nConditions: %s \nTempature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def get_weather(City):
    weather_key = '9c0304f30d0d55f7d0d81c09e628a82b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': City, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='RedTree.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3,)

Lower_Frame = tk.Frame(root, bg='blue', bd=10)
Lower_Frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(Lower_Frame, font=('Noto Sans Javanese', '30'))
label.place(relwidth=1, relheight=1)


print(tk.font.families())

root.mainloop()
