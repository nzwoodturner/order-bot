import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client =commands.Bot(command_prefix = '~')
status = cycle(['status 1','status 2'])
@client.event
async def on_ready():
    print('Bot is ready.')
    change_status.start()

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('command does not exist')
    
    

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
   responses=['It is certain.', 'maybe','no']
   await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))




for filename in os.listdir(r'D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run('NzQwODQ0NzA5NDU0NTQ0OTM3.Xyu7Zg._vEYs72F9nugczP2pomoC_cyqZw')