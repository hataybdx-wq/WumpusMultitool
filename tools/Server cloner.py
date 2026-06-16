import discord
import asyncio
import time
import colorama
from colorama import Fore, Style
import os
from datetime import datetime
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

os.system('cls')
os.system("title XClone - By Adwares x Ace")
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                          
"""))
token = input(Colorate.Horizontal(Colors.blue_to_cyan,"Discord Account Token: "))
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
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Welcome {self.user}")
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Type !help in Discord") 
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Type !clone <source_guild_id> <destination_guild_id> in Discord") 

    async def on_message(self, message):
        if message.author.id != self.user.id:
            return

        if message.content.startswith("!help"):
            await message.channel.send("Usage of commands:\n"
                                       "`!clone <source_guild_id> <destination_guild_id>` - Clones a server's setup to another server.\n"
                                       "`!ping` - Check the bot's latency.\n"
                                       "`!rate_limit` - Check if the bot is under rate limit.")

        elif message.content.startswith("!ping"):
            latency = round(self.latency * 1000)
            await message.channel.send(f"Bot latency: {latency}ms")

        elif message.content.startswith("!rate_limit"):
            try:
                await message.channel.send("Checking rate limit status...")
                async with self.http.get("/gateway") as response:
                    if response.status == 429:
                        await message.channel.send("The bot is currently rate-limited!")
                    else:
                        await message.channel.send("The bot is not rate-limited.")
            except Exception as e:
                await message.channel.send(f"Error checking rate limit: {str(e)}")


        if message.content.startswith("!clone"):
            parts = message.content.split()
            if len(parts) != 3:
                await message.channel.send("Invalid format use : `!clone <source_guild_id> <destination_guild_id>`")
                return

            source_id = int(parts[1])
            dest_id = int(parts[2])

            source_guild = self.get_guild(source_id)
            dest_guild = self.get_guild(dest_id)

            if not source_guild or not dest_guild:
                await message.channel.send("Source or destination guild not found.")
                return

            try:
                member = await source_guild.fetch_member(self.user.id)
                if not member:
                    await message.channel.send("You are not in the source guild!")
                    return
            except:
                await message.channel.send("You are not admin in the source guild!")
                return

            try:
                member = await dest_guild.fetch_member(self.user.id)
                if not member:
                    await message.channel.send("You are not in the destination guild!")
                    return
            except:
                await message.channel.send("You are not admin in the destination guild!")
                return

            await message.channel.send("Starting the clone!")
            now = datetime.now()
            heure = now.strftime("%H:%M:%S")
            print(f"{Fore.GREEN}[{Fore.RESET}{heure}{Fore.GREEN}]{Fore.RESET} Cloning started: [{source_id}] ⮕ [{dest_id}] {Fore.GREEN}[]{Fore.RESET}")
            try:
                await dest_guild.edit(name=source_guild.name)
            except:
                print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Cannot rename the server.")

            for ch in dest_guild.channels:
                try:
                    await ch.delete()
                    now = datetime.now()
                    heure = now.strftime("%H:%M:%S")
                    print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Deleted channel: {ch.name}")

                except Exception as e:
                     now = datetime.now()
                     heure = now.strftime("%H:%M:%S")
                     print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Failed to delete channel: {ch.name} - {e}")

                role_map = {}
                for role in source_guild.roles[::-1]:
                    if role.name == "@everyone":
                        role_map[role.id] = dest_guild.default_role
                        continue

                    existing_role = discord.utils.get(dest_guild.roles, name=role.name)
                    if existing_role:
                        try:
                            await existing_role.delete()
                            await asyncio.sleep(1)
                            print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Deleted duplicate role: {role.name}")
                        except discord.errors.HTTPException as e:
                            print(f"{Fore.YELLOW}[{Fore.RESET}{heure}{Fore.YELLOW}]{Fore.RESET} Failed to delete role: {role.name} - {e}")
                        continue

                    try:
                        await asyncio.sleep(1)
                        new_role = await dest_guild.create_role(
                            name=role.name,
                            permissions=role.permissions,
                            colour=role.colour,
                            hoist=role.hoist,
                            mentionable=role.mentionable
                        )
                        role_map[role.id] = new_role
                        print(f"{Fore.GREEN}[{Fore.RESET}{heure}{Fore.GREEN}]{Fore.RESET} Created role: {role.name}")
                    except discord.errors.HTTPException as e:
                        print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Failed to create role: {role.name} - {e}")
                    else:
                        continue

            for category in source_guild.categories:
                try:
                    new_cat = await dest_guild.create_category(
                        name=category.name,
                        overwrites={role_map.get(k.id): v for k, v in category.overwrites.items() if k.id in role_map}
                    )

                    for channel in category.channels:
                        overwrites = {
                            role_map.get(k.id): v for k, v in channel.overwrites.items() if k.id in role_map
                        }

                        if isinstance(channel, discord.TextChannel):
                            await dest_guild.create_text_channel(
                                name=channel.name,
                                category=new_cat,
                                topic=channel.topic,
                                position=channel.position,
                                slowmode_delay=channel.slowmode_delay,
                                nsfw=channel.nsfw,
                                overwrites=overwrites
                            )
                            print(f"{Fore.GREEN}[{Fore.RESET}{heure}{Fore.GREEN}]{Fore.RESET} Created text channel: {channel.name}")

                        elif isinstance(channel, discord.VoiceChannel):
                            await dest_guild.create_voice_channel(
                                name=channel.name,
                                category=new_cat,
                                position=channel.position,
                                bitrate=channel.bitrate,
                                user_limit=channel.user_limit,
                                overwrites=overwrites
                            )
                            print(f"{Fore.GREEN}[{Fore.RESET}{heure}{Fore.GREEN}]{Fore.RESET} Created voice channel: {channel.name}")
                except Exception as e:
                    print(f"{Fore.RED}[{Fore.RESET}{heure}{Fore.RED}]{Fore.RESET} Error when copying a category or a channel: {e}")
                else:
                    continue

                print(f"{Fore.GREEN}[{Fore.RESET}{heure}{Fore.GREEN}]{Fore.RESET} Cloning finished.")
                


intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(token, bot=False)
