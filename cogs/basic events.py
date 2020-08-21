import discord
from discord.ext import commands, tasks



class basic_events(commands.Cog):
    
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')
        #channel = client.get_channel(742356885927231491)
        #await channel.send('hello')


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('command does not exist')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f'{member} has joined the server')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f'{member} has left the server')

def setup(client):
    client.add_cog(basic_events(client))
