from dotenv import load_dotenv
import os

load_dotenv()

FLASK_KEY = os.environ.get("FLASK_KEY")
DB_NAME = os.environ.get("DB_NAME")
ADMIN_LOGIN = os.environ.get("ADMIN_LOGIN")
ADMIN_PASS = os.environ.get("ADMIN_PASS")