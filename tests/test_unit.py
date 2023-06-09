"""Unit tests for the package."""

from steamship import Steamship

from src.api import TelegramBuddy
from utils import use_local_with_ngrok


def test_greeting():
    """You can test your app like a regular Python object."""
    client = Steamship()
    use_local_with_ngrok(client, TelegramBuddy, config={
        "botName": "ted",
        "botPersonality": "happy",
        "botToken": "5720939969:AAEQTYUatOLJz2t6mpR7kkYqlE2850DSFMg"
    })


