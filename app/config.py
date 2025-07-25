import os
from dotenv import load_dotenv

load_dotenv()  # Make sure this is called only once

EURI_API_KEY = os.getenv("EURI_API_KEY")
if not EURI_API_KEY:
    raise ValueError("EURI_API_KEY environment variable is not set.")