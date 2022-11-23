import discord
from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def ping(self, ctx: discord.ApplicationContext):
        embed=discord.Embed(
            title="Ping",
            description=f"The ping to discord is: '{round(self.bot.latency * 100, 2)}' ms")
        await ctx.respond(embed=embed)




def setup(bot):
    bot.add_cog(misc(bot))