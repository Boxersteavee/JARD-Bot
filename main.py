import discord
import os
from dotenv import load_dotenv
import logging
from discord.ext import commands
import contextlib
import datetime
import calendar


logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='pycord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

debug_guilds = [764981968579461130, 798180194049196032]

bot = commands.Bot()

date = datetime.datetime.utcnow()
utc_time = calendar.timegm(date.utctimetuple())

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

@bot.slash_command(debug_guilds=debug_guilds)
async def cogreload(
        ctx: discord.ApplicationContext,
        cog: discord.Option(str, "Which cog do you want to reload? (Only works for Boxersteavee)", default="all") # type: ignore
 ):
    if ctx.author.id != 543784934146441227:
        return await ctx.respond("You are not allowed to use this command.")
        
    global cogfiles
    
    new_cogfiles = cogfiles
    cog = f"cogs.{cog}"
    if cog != "all":
        if cog in cogfiles:
            new_cogfiles = [cog]

        else: return await ctx.respond("That cog doesn't exist")

    await ctx.respond("Reloading cog(s) and syncing commands")
    
    for cogfile in new_cogfiles:
        try:
            bot.reload_extension(cogfile)
        except Exception as err:
            logger.error(err)
    
    await ctx.interaction.edit_original_response(content="Reloaded cog(s), Syncing commands...")
    with contextlib.suppress(Exception):
        await bot.sync_commands()
    await ctx.interaction.edit_original_response(content="Reloaded cog(s) and synced commands")

@bot.slash_command(debug_guilds=debug_guilds)
async def uptime(
    ctx: discord.ApplicationContext
):
    embed = discord.Embed(
        title="JARD Bot's Uptime"
    )
    embed.set_footer(text="I am JARD-Bot, Just Another Random Discord Bot")
    embed.add_field(name="Startup of bot: ", value=f"<t:{utc_time}:R> (Since <t:{utc_time}:f>")
    await ctx.respond(embed=embed)
#Loads .env and uses token to login
load_dotenv()
bot.run(os.getenv('TOKEN'))
