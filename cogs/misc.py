import discord
from discord.ext import commands

debug_guilds = [798180194049196032, 764981968579461130]

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def ping(self, ctx: discord.ApplicationContext):
        embed=discord.Embed(
            title="Ping",
            description=f"The ping to discord is: {round(self.bot.latency * 100, 2)} ms")
        await ctx.respond(embed=embed)
    
    @commands.slash_command()
    async def cheese(self, ctx: discord.ApplicationContext):
        embed=discord.Embed(
            title="Cheese",
            description="Cheese is a dairy product, derived from milk and produced in wide ranges of flavors, textures and forms by coagulation of the milk protein casein. It comprises proteins and fat from milk, usually the milk of cows, buffalo, goats, or sheep. During production, the milk is usually acidified, and adding the enzyme rennet causes coagulation. The solids are separated and pressed into final form. Some cheeses have molds on the rind, the outer layer, or throughout. Most cheeses melt at cooking temperature.")
        await ctx.respond(embed=embed)

    @commands.slash_command()
    async def pointless(self, ctx: discord.ApplicationContext):
         await ctx.respond("This is literally pointless, why did you do this?")

    @commands.slash_command(debug_guilds=debug_guilds)
    async def kill(self,
    ctx: discord.ApplicationContext,
    user: discord.Option(str, "Who do you want to kill?", default="You")  # type: ignore
    ):
        await ctx.respond(f"{user} is dead.")



def setup(bot):
    bot.add_cog(misc(bot))
