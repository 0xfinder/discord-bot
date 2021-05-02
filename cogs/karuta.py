import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()

authcodes = {}
accounts = 110
for i in range(0,accounts):
    authcodes['auth{}'.format(i)] = os.getenv(f'AUTH{str(i)}')

class KarutaCog(commands.Cog):
    """Karuta commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kdaily', hidden=True)
    @commands.is_owner()
    async def kdaily(self, ctx):
        for i in range(0,accounts):
            header = {
                'authorization': authcodes[f'auth{str(i)}']
            }

            channel = 'https://discord.com/api/v9/channels/721640861510926357/messages'

            payload = {
            'content': 'kdaily' 
            }

            r = requests.post(channel, data=payload, headers=header)

    @commands.command(name='say', hidden=True)
    @commands.is_owner()
    async def say(self, ctx, *args):
        channelid = args[-1]
        args = list(args)
        del args[-1]
        for i in range(0,accounts):
            header = {
                'authorization': authcodes[f'auth{str(i)}']
            }

            channel = f'https://discord.com/api/v9/channels/{channelid}/messages'

            payload = {
            'content': " ".join(args)
            }

            r = requests.post(channel, data=payload, headers=header)

def setup(bot):
    bot.add_cog(KarutaCog(bot))
