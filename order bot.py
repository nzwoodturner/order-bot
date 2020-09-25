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
with open(r"recipes.JSON") as json_file:
    recipes=json.load(json_file)
price_list={"Bauxite":20,"Coal":20,"Quartz":20,"Hematite":20,
            "Chromite":20,"Malachite":20,"Limestone":20,"Natron":20,
            "Petalite":20,"Garnierite":20,"Acanthite":20,"Pyrite":20,
            "Cobaltite":20,"Cryolite":20,"Kolbeckite":20,"Gold Nuggets":20,
            "Rhodonite":20,"Columbite":20,"Illmenite":20,"Vanadinite":20}        

    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')   

for filename in os.listdir(r'D:\documents\discord bots\discord bot py\order bot\order bot\order-bot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token=read_token()

client.run(token)