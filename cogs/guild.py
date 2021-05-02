import discord
from discord.ext import commands

def check_if_it_is_lewd(ctx):
    return ctx.guild.id == 797443315607273502

class GuildCog(commands.Cog):
    """Guild Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='min', aliases=['minimums', 'minimum', 'mins', 'contri'])
    @commands.check(check_if_it_is_lewd)
    async def minimum(self, ctx, *args: str):
        """Check guild clash minimum contribution"""
        
        embed = discord.Embed(title='Minimum Contribution',
                              description='**Easy [Min #17]:**\nBlock Bashers\nHarvest Heroes\nFishing Fanatics\nBlock Builders\n\n**Moderate [Min #14]**\nCooking Conquerors\nSpeedy Splicers\n\n**Hard [Min: #12]:**\nSuper Startopians\nSurgery Stars',
                              colour=0x98FB98)
        embed.set_footer(text="Forfeit for skipping hard events is 10 WLs")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/721640861510926357/827472539688370186/lewd.png")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @minimum.error
    async def minimum_handler(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            if check_if_it_is_lewd(ctx) != 797443315607273502:
                await ctx.send("You must be in **Lewd Guild** to use this command...")


    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event

        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban

        Check above for a list of events.
        """

        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(GuildCog(bot))
