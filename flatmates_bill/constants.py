import os
from dotenv import load_dotenv


load_dotenv()

FILESTACK_API_KEY = os.getenv('FILESTACK_API_KEY')
