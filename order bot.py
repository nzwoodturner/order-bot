import discord
import os
from discord.ext import commands, tasks
from classes.orders import Order

client = commands.Bot(command_prefix = '~')  

def read_token():
    with open(r"D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def order2(ctx,element,number):
    member=ctx.author
    member = str(member)
    await ctx.send('order has been placed')
    print(f'ran {member}')
    new_order=Order(element,number)
    await ctx.send('order has been placed')
    number=newOrder.number      

for filename in os.listdir(r'D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token=read_token()

client.run(token)