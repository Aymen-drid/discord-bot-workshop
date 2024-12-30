import discord
from discord.ext import commands
import datetime
import os 
from dotenv import load_dotenv

# Setup bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
# Event: New member joins
@bot.event
async def on_member_join(member):
    # Send welcome message to a specific channel
    channel = discord.utils.get(member.guild.channels, name='welcome')
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}! 👋')

# Event: Member leaves
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    if channel:
        await channel.send(f'Goodbye {member.name}! We hope to see you again!')

# Event: Voice channel events
@bot.event
async def on_voice_state_update(member, before, after):
    log_channel = discord.utils.get(member.guild.channels, name='bot-logs')
    
    if not before.channel and after.channel:  # Member joined a voice channel
        if log_channel:
            await log_channel.send(f'🎤 {member.name} joined voice channel: {after.channel.name}')
    
    elif before.channel and not after.channel:  # Member left a voice channel
        if log_channel:
            await log_channel.send(f'👋 {member.name} left voice channel: {before.channel.name}')

# Event: Message deleted
@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
        
    log_channel = discord.utils.get(message.guild.channels, name='bot-logs')
    if log_channel:
        embed = discord.Embed(
            title="Message Deleted",
            description=f"Message by {message.author.name} was deleted in {message.channel.mention}",
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="Content", value=message.content or "No content")
        await log_channel.send(embed=embed)
# ping is the name of the cmd
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bot latency: {round(bot.latency * 1000)}ms')

# Define another command
@bot.command()
async def greet(ctx):
    await ctx.send("Hi there! I'm your friendly bot.")
load_dotenv()


TOKEN = os.getenv('TOKEN')

bot.run(TOKEN)