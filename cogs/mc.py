import discord
from discord.ext import commands
import requests

debug_guilds = [798180194049196032, 764981968579461130]

class mc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def mcping(self, 
        ctx: discord.ApplicationContext,
        ip: discord.Option(str, "Enter an IP/Server Address"),  # type: ignore
        ):
        embed=discord.Embed(
        title = f'Loading Status for {ip}'
        )
        await ctx.respond(embed=embed)

        r = requests.get(f'https://api.mcsrvstat.us/2/{ip}')

        API_Response = r.json()

        if API_Response["online"] == False:
            finalrespond = discord.Embed(
                title = f'Status of {ip}'
            )
            finalrespond.set_footer(text='Information from https://api.mcsrvstat.us')
            finalrespond.add_field(name='IP', value=f"`{API_Response['ip']}`", inline=True)
            finalrespond.add_field(name='Port', value=f"`{API_Response['port']}`", inline=True)
            finalrespond.add_field(name='Online', value=f"`{API_Response['online']}`", inline=True)
            finalrespond.add_field(name='Hostname', value=f"`{API_Response['hostname']}`", inline=True)
            await ctx.interaction.edit_original_response(embed=finalrespond)

        else:
            finalrespondon = discord.Embed(
                title = f'Status of{ip}'
            )
            finalrespondon.set_footer(text='Information from https://api.mcsrvstat.us')
            finalrespondon.add_field(name='IP', value=f"`{API_Response['ip']}`", inline=True)
            finalrespondon.add_field(name='Port', value=f"`{API_Response['port']}`", inline=True)
            finalrespondon.add_field(name='Online', value=f"`{API_Response['online']}`", inline=True)
            finalrespondon.add_field(name='Hostname', value=f"`{API_Response['hostname']}`", inline=True)
            finalrespondon.add_field(name='Version', value=f"`{API_Response['version']}`", inline=True)
            finalrespondon.add_field(name='Player Count', value=f"`{API_Response['players']['online']}/{API_Response['players']['max']}`", inline=True)
            finalrespondon.add_field(name='MOTD', value="```" + '\n'.join(API_Response['motd']['clean']) + "```" , inline=True)
            finalrespondon.set_image(url=f"https://api.mcsrvstat.us/icon/{ip}")
            await ctx.interaction.edit_original_response(embed=finalrespondon)
        
def setup(bot):
    bot.add_cog(mc(bot))