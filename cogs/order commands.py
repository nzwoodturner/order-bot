import discord
from discord.ext import commands
import orders

class order_commands(commands.Cog):

    def _init_ (self,client):
        self.client=client
   
    @commands.command()
    async def order2(self,ctx,element,number):
        member=ctx.author
        member = str(member)
        await ctx.send('order has been placed')
        print(f'ran{member}')
        new_order=orders.Order(element,number)
        await ctx.send('order has been placed')
        number=newOrder.number

        await ctx.send(f'order has been placed{number}')
    
    #@commands.command()
    #async def orderid(self,ctx):
        #id=newOrder.get_id()
        #await ctx.send(f'{id}') 
        
def setup(client):
    client.add_cog(order_commands(client))


