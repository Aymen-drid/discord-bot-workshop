import discord
import os
from dotenv import load_dotenv

# def the targets for access
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return 

    if message.content.lower() == 'hello': 
        await message.channel.send('Hello, world!');


load_dotenv()


TOKEN = os.getenv('TOKEN')

client.run(TOKEN)
