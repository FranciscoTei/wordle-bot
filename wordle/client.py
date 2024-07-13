from pyrogram import Client
from wordle.settings import settings

wordle_bot = Client(
    "wordle",
    api_hash=settings.API_HASH,
    api_id=settings.API_ID,
    bot_token=settings.BOT_TOKEN,
    plugins=dict(root="wordle/plugins"),
)

