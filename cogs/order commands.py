import discord
from discord.ext import commands
from classes.order import Order

class order_commands(commands.Cog):

    def _init_ (self,client):
        self.client=client
   
    @commands.command()
    async def order(self,ctx):
        member=ctx.author.nick
        await ctx.send('order has been placed')
        newOrder=Order(element,number)
        await ctx.send('order has been placed')
        number=newOrder.number

        await ctx.send(f'order has been placed{number}')
    
    #@commands.command()
    #async def orderid(self,ctx):
        #id=newOrder.get_id()
        #await ctx.send(f'{id}') 
        
def setup(client):
    client.add_cog(order_commands(client))
