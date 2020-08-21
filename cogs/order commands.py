import discord
from discord.ext import commands
from classes.orders import Order

class order_commands(commands.Cog):

    def __init__ (self,client):
        self.client=client
   
    @commands.command()
    async def order(self,ctx,element,number):
        global new_order
        member=ctx.author
        member = str(member)
        await ctx.send('order has been placed')
        print(f'ran{member}')
        #Order.create('h',1)
        new_order=Order(element,number)
        await ctx.send('order has been placed')
        #number=newOrder.number

        await ctx.send(f'order has been placed{number}')
    
    #@commands.command()
    #async def orderid(self,ctx):
        #id=newOrder.get_id()
        #await ctx.send(f'{id}') 
        
def setup(client):
    client.add_cog(order_commands(client))


