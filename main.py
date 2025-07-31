from pyrogram import Client
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

app = Client("auto_name_updater", api_id=api_id, api_hash=api_hash)

async def update_name():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        new_name = f" {current_time}"
        try:
            await app.update_profile(first_name=new_name)
            print(f"Yangilandi: {new_name}")
        except Exception as e:
            print(f"Xatolik: {e}")
        await asyncio.sleep(60)

async def main():
    async with app:
        await update_name()

asyncio.run(main())
