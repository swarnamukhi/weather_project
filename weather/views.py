import requests
from django.shortcuts import render
from .models import City  # Ensure City is imported

def home(request):
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8d1ce897ab239abf2204a1b3585bfa55&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'main' in data:
            # Save to DB if not already saved
            if not City.objects.filter(name__iexact=city).exists():
                City.objects.create(name=city)
        else:
            error = f"City '{city}' not found. Please try again."

    # Get weather for all saved cities
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid=8d1ce897ab239abf2204a1b3585bfa55&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'main' in data:
            weather = {
                'city': city.name.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'windspeed': data['wind']['speed'],
            }
            weather_data.append(weather)

    return render(request, 'home.html', {'weather_data': weather_data, 'error': error})
