import os
from dotenv import load_dotenv

load_dotenv()

# Application Configuration
APP_NAME = "OmniRadar AI — Enterprise Hub"
APP_VERSION = "2.0.0"
APP_ICON = "💎"

# UI Configuration
UI_CONFIG = {
    "layout": "wide",
    "page_title": "OmniRadar AI — Pro Suite",
    "page_icon": "💎",
    "initial_sidebar_state": "expanded",
}

# Color Scheme
COLOR_SCHEME = {
    "primary": "#1f77b4",
    "secondary": "#4caf50",
    "accent": "#ff9800",
    "error": "#f44336",
    "success": "#4caf50",
    "warning": "#ff9800",
    "info": "#2196f3",
}

# Languages
LANGUAGES = {
    "ar": "العربية",
    "en": "English",
}

DEFAULT_LANGUAGE = "ar"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///omni_radar.db")
DATABASE_ECHO = os.getenv("DATABASE_ECHO", "False").lower() == "true"

# API Configuration
API_KEY = os.getenv("API_KEY", "")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/omni_radar.log")

# Feature Flags
FEATURES = {
    "enable_favorites": True,
    "enable_search": True,
    "enable_statistics": True,
    "enable_export": True,
    "enable_notifications": False,
}

# Pagination
ITEMS_PER_PAGE = 10

# Session Configuration
SESSION_TIMEOUT = 3600  # seconds

print(f"🚀 {APP_NAME} v{APP_VERSION} loaded successfully")
