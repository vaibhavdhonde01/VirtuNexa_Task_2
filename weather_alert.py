import requests
import smtplib
import ssl
from email.message import EmailMessage

# --- CONFIGURATIONS ---
API_KEY = 'Add_your_API_key'  # add your API key 
CITY_NAME = 'Mumbai'  # Change as needed
ALERT_CONDITION = {
    'temp_min': 30,  # Minimum temp to trigger alert
    'weather': 'Rain'  # Weather condition to alert
}

EMAIL_SENDER = 'email of sender' # add email adress for sending alerts 
EMAIL_PASSWORD = 'Add app password'  # Use app password for Gmail
EMAIL_RECEIVER = 'add reciver mail addredd' # add an email id of reciever 


def get_weather_data(city):
    print(f"Fetching weather data for {city}...")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return {
        'temp': data['main']['temp'],
        'condition': data['weather'][0]['main'],
        'description': data['weather'][0]['description']
    }


def send_email(subject, body):
    print("Sending email alert...")
    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = EMAIL_RECEIVER
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(em)
    print("Email sent successfully!")


def check_conditions_and_alert(weather):
    if weather['temp'] >= ALERT_CONDITION['temp_min'] or ALERT_CONDITION['weather'].lower() in weather['condition'].lower():
        subject = f"Weather Alert: {weather['condition']} in {CITY_NAME}"
        body = f"Current temperature is {weather['temp']}°C with {weather['description']}."
        send_email(subject, body)
    else:
        print("No alert conditions met. All good! 🌞")


if __name__ == "__main__":
    weather_data = get_weather_data(CITY_NAME)
    check_conditions_and_alert(weather_data)
