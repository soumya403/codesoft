import tkinter as tk
import requests
import time


def get_weather():
    city=entry.get()
    api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bcc5a75c89211cb11819488b51410117'

    try:
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main'] if 'weather' in json_data and json_data['weather'] else 'Unknown'
        temp=int(json_data['main']['temp'] - 273.15)
        min_temp=int(json_data['main']['temp_min'] - 273.15)
        max_temp=int(json_data['main']['temp_max'] - 273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        sunrise=time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset=time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info=f"{condition}\n{temp}°C"
        final_data=f"Min Temp: {min_temp}°C\nMax Temp: {max_temp}°C\nPressure: {pressure}\nHumidity: {humidity}\nWind Speed: {wind}\nSunrise: {sunrise}\nSunset: {sunset}"

        label_condition.config(text=final_info)
        label_details.config(text=final_data)
    except Exception:
        label_condition.config(text='Unknown')
        label_details.config(text='Weather information unavailable')


# GUI setup
root=tk.Tk()
root.geometry("600x500")
root.title("Weather App")

font_big=("Arial", 35, "bold")
font_small=("Arial", 15, "bold")

# Entry for city
entry=tk.Entry(root, justify='center', width=20, font=font_big)
entry.pack(pady=20)
entry.focus_set()  # Set initial focus

# Button to get weather
button_get_weather=tk.Button(root, text="Get Weather", command=get_weather, font=font_small, bg='#4CAF50', fg='white')
button_get_weather.pack(pady=10)

# Labels for displaying weather information
label_condition=tk.Label(root, font=font_big, bg='#f0f0f0')
label_condition.pack(pady=10)

label_details=tk.Label(root, font=font_small, bg='#f0f0f0')
label_details.pack(pady=10)

root.mainloop()
