from pyrogram import Client, filters
from pyrogram.types import Message
from keep_alive import keep_alive  # agar foydalanayotgan bo‘lsang

import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

app = Client(session_name, api_id=api_id, api_hash=api_hash)

# ✅ Start qilamiz
@app.on_message(filters.command("on", prefixes=".") & filters.me)
async def turn_on(_, message: Message):
    await message.edit("✅ *Bot ishga tushdi!*")

@app.on_message(filters.command("off", prefixes=".") & filters.me)
async def turn_off(_, message: Message):
    await message.edit("⛔ *Bot o‘chirildi*")
    await app.stop()

if __name__ == "__main__":
    keep_alive()  # agar ishlatmasang, bu qatorni olib tashla
    app.run()
