import discord
import os
from dotenv import load_dotenv
import logging
from discord.ext import commands


logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



bot = discord.Bot(debug_guilds=[798180194049196032])


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)

#Loads .env and uses token to login
load_dotenv()
bot.run(os.getenv('TOKEN'))