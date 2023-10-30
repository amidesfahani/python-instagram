from instaloader import Instaloader
import os
from dotenv import load_dotenv
load_dotenv()

def login(loader: Instaloader):
    # Create an instance of the Instaloader class
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    # Login to Instagram (optional)
    try:
        loader.load_session_from_file(USER)
    except:
        loader.login(USER, PASSWORD)