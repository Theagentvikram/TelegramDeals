from telegram import Bot
import asyncio

bot_token = '7542895270:AAHfzzrElJbYl0ak-7h_NwwI_mnEM9AKAAE'  # Replace with your bot token
chat_id = '@Techiedeals9'  # Replace with your channel's username or chat_id

bot = Bot(token=bot_token)

async def send_message():
    await bot.send_message(chat_id=chat_id, text="Test message from bot!")

if __name__ == "__main__":
    asyncio.run(send_message())
