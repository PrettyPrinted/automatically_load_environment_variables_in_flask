#run.py
from demo import create_app
from dotenv import load_dotenv

load_dotenv('.env') #the path to your .env file (or any other file of environment variables you want to load)

app = create_app()