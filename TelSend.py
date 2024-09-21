import pandas as pd
from telegram import Bot
import asyncio


bot_token = '7542895270:AAHfzzrElJbYl0ak-7h_NwwI_mnEM9AKAAE'  # Replace with your bot token
chat_id = '@Techiedeals9'  # Replace with your channel's username or chat_id

# Path to CSV file
csv_file_path = 'deals.csv'  # Path to your CSV file

# Load CSV data
deals_df = pd.read_csv(csv_file_path)

# Initialize the bot
bot = Bot(token=bot_token)

# Define an async function to send the messages
async def send_deals():
    # Iterate over each deal and send to Telegram channel
    for index, row in deals_df.iterrows():
        sno = row['sno']
        deal_image = row['Deals image']  # Image file path (local in this case)
        deal_description = row['Deal Description']
        deal_link = row['Deal Link']

        # Prepare the message with the description and the link
        message = f"Grab FAAst 🔥🔥\n\n{deal_description} \n\n {deal_link}"

        # Send image with the message
        with open(deal_image, 'rb') as img_file:
            await bot.send_photo(chat_id=chat_id, photo=img_file, caption=message)

    print("Deals sent to Telegram channel successfully!")

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_deals())
