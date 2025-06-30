import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

# Audio Configuration
MICROPHONE_INDEX = 0  # Default microphone (change if needed)
SPEECH_RATE = 180     # Speech speed (words per minute)
VOLUME = 0.9          # Volume level (0.0 to 1.0)

# Chat Configuration
MAX_CONVERSATION_HISTORY = 6  # Number of messages to retain in memory