# without this, the code will no be able to find the requests from the api key
import requests

api_key = "YOUR_API_KEY_HERE"
city = input("Enter the city name: ")

# the url to fetch weather data from the openweathermap api
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# execute the ping
print(f"Fetching weather data for {city}...")
response = requests.get(url)

if (response.status_code == 200):
    data = response.json()
    temp = data['main']['temp']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']

    with open("weather_data.txt", "a") as log_file:
        log_file.write(f"Location: {city}\n")
        log_file.write(f"Condition: {description}\n")
        log_file.write(f"Temperature: {temp} C\n")
        log_file.write(f"Wind Speed: {wind} meters/sec\n")
        log_file.write("----------------------------\n")
    
    print("--- TRANSMISSION SECURED ---")
    print(f"Location: {city}")
    print(f"Condition: {description}")
    print(f"Temperature: {temp} C")
    print(f"Wind Speed: {wind} meters/sec")
    print("----------------------------")

else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")
