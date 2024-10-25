import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('402338208c7d67bb2f535d3acc7486e3')
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes in seconds
TEMP_THRESHOLD = 35  # Celsius
ALERT_EMAIL = 'shivamgupta0097@gmail.com'

# Create directories for storing data and logs if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('logs', exist_ok=True)