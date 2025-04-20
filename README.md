# VirtuNexa_Task_2
# WeatherMate


# 1. 🌦️ Weather Alert Email Notification Script

## 💡 Overview
This Python-based application fetches real-time weather data for a specified location using the OpenWeatherMap API. It checks for specific weather conditions (like high temperature or rain), and if those conditions are met, it sends an automatic **email alert** to the user.

---

## 🚀 Features

- ✅ Real-time weather monitoring using OpenWeatherMap
- ✅ Customizable alert conditions (e.g., temperature, rain)
- ✅ Automatic email alerts when conditions are met
- ✅ Easy to configure and run
- ✅ Can be compiled into an executable (.exe)

---

## 🔧 Setup Instructions

###  Install Required Libraries

Make sure you have Python 3 installed. Then run:
python weather_alert.py

# 2. Get OpenWeatherMap API Key

• Sign up at https://openweathermap.org/api

• Go to your dashboard and copy your API key  
if you dont want to create an account you can directly use this key😉(bd5e378503939ddaee76f12ad7a97608)

# 3. 📧 Configure Email Alerts (Gmail Recommended)

➤ Step 1: Enable 2-Step Verification
Go to your Google Account Security and turn on 2-Step Verification.

➤ Step 2: Generate App Password
Visit App Passwords, select Mail, and generate a 16-character app password.

# 4. 🛠️ Edit Configuration in weather_alert.py
Open the script and update these values:

API_KEY = 'your_openweathermap_api_key'
CITY_NAME = 'Your_City_Name'

EMAIL_SENDER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
EMAIL_RECEIVER = 'receiver_email@gmail.com'

ALERT_CONDITION = {
    'temp_min': 30,  # Temperature in °C to trigger alert
    'weather': 'Rain'  # Keyword to match in weather condition
}


# How to Run
python weather_alert.py

If the weather conditions match the alert thresholds, you'll receive an email alert. Otherwise, the script will display:
No alert conditions met. All good! 🌞


# Optional: Create Executable
To make it a portable app:
pip install pyinstaller
pyinstaller --onefile weather_alert.py
→ The .exe file will be created inside the /dist folder.

# Sample Alert Email
Subject: Weather Alert: Rain in Mumbai
Body:
Current temperature is 32°C with light rain.


# Author
Developed by: Vaibhav Dhonde 

# License
This project is free to use and modify for personal or educational purposes.
