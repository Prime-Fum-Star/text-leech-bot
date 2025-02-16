import os

API_ID    = os.environ.get("API_ID", "25645046")
API_HASH  = os.environ.get("API_HASH", "568c366b5573c5c349f0f0f25c3a4ccd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8177990799:AAGFyMi4DQ3Sc41GVqKt8-3XY-E2iinWuH8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
