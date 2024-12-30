import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('!status'):
        await message.channel.send(f'Server: {message.guild.name}\nMembers: {message.guild.member_count}')

@client.event
async def on_member_join(member):
    # the default channel that u set ur bot to work in 
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Welcome {member.mention} to the server!')

@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'{member.name} has left the server.')
# Load the .env file
load_dotenv()

# Get the token from the .env file
TOKEN = os.getenv('TOKEN')
client.run('YOUR_TOKEN_HERE')