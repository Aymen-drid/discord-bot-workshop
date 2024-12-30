import discord

# Creating the client without specifying intents
client = discord.Client()

# when the bot successfully connects to the server
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# when the bot get a new message
@client.event
async def on_message(message):
    # client user is the user who creates the bot 
    if message.author == client.user:
        await message.channel.send("You are admin !")

    if message.content == 'hello':
        await message.channel.send('Hello, world!')

# Run the bot with the token
client.run('YOUR_BOT_TOKEN')
