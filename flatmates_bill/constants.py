import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


ASSETS = Path("./assets")
BILLS = ASSETS / "pdf_bills"
IMAGES = ASSETS / "images"
BILL_LOGO = IMAGES / "house.png"

FILESTACK_API_KEY = os.getenv('FILESTACK_API_KEY')