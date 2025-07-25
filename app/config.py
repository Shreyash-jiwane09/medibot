import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # Make sure this is called only once

# First try Streamlit secrets, then fallback to env variable
EURI_API_KEY = st.secrets.get("EURI_API_KEY", os.getenv("EURI_API_KEY"))
if not EURI_API_KEY:
    raise ValueError("EURI_API_KEY environment variable is not set.")