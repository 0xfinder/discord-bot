import discord
from discord.ext import commands


class OwnerCog(commands.Cog):
    """Owner commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rules', hidden=True)
    @commands.guild_only()
    @commands.is_owner()
    async def rules(self, ctx):
        embed = discord.Embed(title="Rules", colour=discord.Colour(0x98FB98), description=":large_orange_diamond: Don't harass, bother, or be disrespectful to people of any race, belief, gender, etc. Treat each other better than you'd like to be treated. Keep it civil and chill. Block people if you have to, and inform the mods;\n\n:large_orange_diamond: Don't share invitations from other servers in chat, and don't advertise for any product, channel, or person;\n\n:large_orange_diamond: Follow Discord's Terms of Service, otherwise you will be banned;\n\n:large_orange_diamond: Use the channels for their intended purpose, and not any other;\n\n:large_orange_diamond: We are an English-speaking server but all languages are welcomed;\n\n:large_orange_diamond: Unnecessarily pinging/DMing Admins/Mods will not end well;\n\n:large_orange_diamond: Don't post NSFW pictures or talk about any NSFW topic;")

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/721640861510926357/827472539688370186/lewd.png")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='guildrules', hidden=True)
    @commands.guild_only()
    @commands.is_owner()
    async def guildrules(self, ctx):
        embed = discord.Embed(title="Guild Rules", colour=discord.Colour(0x98FB98), description=":large_orange_diamond: No illegal stuff - ban evading, autofarming etc;\n\n:large_orange_diamond: No leeching, your deposit will be forfeited and you will be kicked;\n\n:large_orange_diamond: No random invites (GE and GC);\n\n:large_orange_diamond: Toxicity will not be tolerated;\n\n:large_orange_diamond: Try to hit minimum within 2 days of clash starting;\n\n:large_orange_diamond: Leaving without claiming your deposit will result in a forfeit;\n\n:large_orange_diamond: Evidence for illegal activities of members should be strictly videos, long enough to substantiate a claim. Photo evidence will not be considered unless it’s strong enough to substantiate a claim, decided at the discretion of GCs/GL;")

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/721640861510926357/827472539688370186/lewd.png")

        embed.add_field(name="Deposit", value="20 WLs")
        embed.add_field(name="Minimum", value="See below")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(OwnerCog(bot))
