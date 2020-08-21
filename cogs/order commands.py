import discord
from discord.ext import commands
from classes.orders import order

class order_commands(commands.Cog):

    def __init__ (self,client):
        self.client=client
   
    @commands.command()
    async def order(self,ctx,element,number):
        member=ctx.author
        member = str(member)
        new_order=order(member,element,number)
        await ctx.send('order has been placed')
    
    @commands.command()
    async def ordername(self,ctx):
        name=new_order.get_player()
        await ctx.send(f'{name}') 
        
def setup(client):
    client.add_cog(order_commands(client))


