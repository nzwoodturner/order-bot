import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '~')  
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')
       
#@client.event
#async def on_member_join(member):
    #channel = client.get_channel(742356885927231491)
    #await channel.send(f'{member} has joined the server')

#@client.event
#async def on_member_remove(member):
    #channel = client.get_channel(742356885927231491)
    #await channel.send(f'{member} has left the server')

for filename in os.listdir(r'D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzQwODQ0NzA5NDU0NTQ0OTM3.Xyu7Zg._vEYs72F9nugczP2pomoC_cyqZw')