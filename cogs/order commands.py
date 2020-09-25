import discord
from discord.ext import commands
#from classes.orders import order
import json
from classes.Cost import Cost



class order_commands(commands.Cog):

    def __init__ (self,client):
        self.client=client
   
    @commands.command()
    async def order(self,ctx,raw_number,*,element):
        with open(r'orders.txt') as json_file:
            orders_list = json.load(json_file)
        member=ctx.author
        member = str(member)
        number=int(raw_number)
        orders_list["orders"].append({"name":member,
                            "element":element,
                            "number":number
                            })  
        with open('orders.txt', 'w') as outfile:
            json.dump(orders_list, outfile)
        await ctx.send('order has been placed')
    
        

    @commands.command()
    async def newOrder(self,ctx):
        await ctx.author.send('place your order')
        #await client.send_message(member,'place your order')
        done=False
        while (done==False):
            pass

    @commands.Cog.listener()
    async def on_message(self,message):
        if (message.guild==None):
            content=message.content
            if (content=='Done'):
                done=True
            else:
                number=content[-1]
                await message.author.send('done')
                length=len(content)
                await message.author.send('done')
                element=content[0:(length-2)]
                await message.author.send('done')
                cost=Cost.get_cost(element,number)
                await message.author.send('done')    
   
    @commands.command()
    async def ordername(self,ctx):
        name=orders_list[0].get_player()
        await ctx.send(f'{name}') 
        
    @commands.command()
    async def test(self,ctx):
        await ctx.send(f'{test_number}')

def setup(client):
    client.add_cog(order_commands(client))


