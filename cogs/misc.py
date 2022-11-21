import discord
from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(guild_ids=[881207955029110855])
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.send(
            embed=discord.Embed(
                title="Ping",
                description=f"The ping to discord is: '{round(self.bot.latency * 100, 2)}' ms"
            )
        )


def setup(bot):
    bot.add_cog(misc(bot))