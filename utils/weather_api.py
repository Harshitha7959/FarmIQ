import random

def get_weather(city):
    city = city.lower()

    if "bangalore" in city:
        temp = random.randint(22, 30)
        humidity = random.randint(60, 80)

    elif "delhi" in city:
        temp = random.randint(30, 42)
        humidity = random.randint(30, 50)

    elif "mumbai" in city:
        temp = random.randint(25, 33)
        humidity = random.randint(70, 90)

    else:
        temp = random.randint(20, 40)
        humidity = random.randint(40, 90)

    condition = random.choice(["Sunny", "Cloudy", "Rainy"])

    return {
        "temperature": temp,
        "humidity": humidity,
        "condition": f"{condition} in {city.title()}"
    }
