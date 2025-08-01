# Django Weather App 🌦️

This is a simple Django-based weather application that allows users to add cities and check current weather data using the OpenWeatherMap API.

## 🚀 Features
- Add cities and view current weather (temperature, description, icons).
- Weather data fetched from OpenWeatherMap API.
- Admin panel for managing cities.

## 🛠️ Tech Stack
- Python
- Django
- HTML, CSS
- Bootstrap (for UI)
- SQLite (default Django DB)

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
2.Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3.Install dependencies:pip install -r requirements.txt
4.Set up .env file with your OpenWeatherMap API key:

WEATHER_API_KEY=your_api_key_here
5.Run migrations and start the server:
python manage.py migrate
python manage.py runserver
6.Access app at:http://127.0.0.1:8000/

Project Structure

project/
│
├── weather_app/
│   ├── models.py
│   ├── views.py
│   └── ...
├── templates/
├── static/
├── manage.py
├── db.sqlite3
└── .env

📄 License
MIT License – feel free to use or modify.

👩‍💻 Author
B Swarnamukhi
Data Analyst | Aspiring Python Developer
