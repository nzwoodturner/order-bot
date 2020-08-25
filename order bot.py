import discord
import os
from discord.ext import commands, tasks
import json

client = commands.Bot(command_prefix = '~')  

#orders_list={"orders":[
#   {"name":"test",
#     "element":"test",
#     "number":1
#     }]
#      }

#with open('orders.txt', 'w') as outfile:
#     json.dump(orders_list, outfile)

def read_token():
    with open(r"D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()


    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')   

for filename in os.listdir(r'D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token=read_token()

client.run(token)