import discord
from discord.ext import commands
import random

"""A simple cog example with simple commands. Showcased here are some check decorators, and the use of events in cogs.

For a list of inbuilt checks:
http://dischttp://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checksordpy.readthedocs.io/en/rewrite/ext/commands/api.html#checks

You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689

For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class SimpleCog(commands.Cog):
    """Simple Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats your input."""

        await ctx.send(our_input)
    
    @commands.command(name='math', aliases=['eval'])
    @commands.guild_only()
    async def do_math(self, ctx, *args):
        """Command to evaluate mathematical expressions"""

        arg = "".join(args)
        code = compile(str(arg), "<string>", "eval")
        await ctx.send(eval(code))

    @commands.command(name='choose', aliases=['decide', 'pick'])
    @commands.guild_only()
    async def choose(self, ctx, *args):
        """Command which randomly chooses argumments delimited by spaces
        E.g .choose 1 2 3 4 5"""

        await ctx.send(f'I choose...\n{args[random.randrange(0,len(args))]}')

    @commands.command(aliases=['nuke', 'purge', 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg):
        """Command to purge messages
        Requires Manage Messages permissions"""

        await ctx.channel.purge(limit=int(arg) + 1)
        await ctx.send('Cleared '+ str(arg) + ' messages!')
        await ctx.channel.purge(limit=1)
        
    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        """A simple command which only responds to the owner of the bot."""

        await ctx.send(f'Hello {ctx.author.mention}!')

    @commands.command(name='embeds', hidden=True)
    @commands.guild_only()
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.

        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)

    @commands.command(name='members')
    @commands.guild_only()
    async def member_count(self, ctx):
        """Simple command to get number of members"""
        a=ctx.guild.member_count
        b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0x98FB98)))
        await ctx.send(embed=b)
            
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

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command...')
            return
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('This command cannot be used in private messages...')
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permissions to use this command...')
            return
        raise error

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SimpleCog(bot))
