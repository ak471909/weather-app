import requests # send HTTP requests to interact with OpenWeatherMap API
import tkinter as tk # GUI
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")

# Create and configure labels and entry fields
city_label = tk.Label(root, text="City:")
city_label.pack() # organizes the widget in blocks before placing them in the parent widget
city_entry = tk.Entry(root) # entry widget for user input (root)
city_entry.pack()

# Create a button to fetch weather data
fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    # Add your API key here
    api_key = "ecf2b63d423f06e56d9af293da58da40"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json() # parse JSON response from the API into a Python dictionary
        temperature = data["main"]["temp"] # retrieves the temperature in Kelvin from the API response
        weather = data["weather"][0]["description"] # retrieves the whether response
        weather_label.config(text=f"Temperature: {round(temperature-273,2)}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

# Associating the fetch_weather() function with the button
fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()