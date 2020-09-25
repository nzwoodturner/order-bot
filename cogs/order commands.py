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
        done=False
        cost=0
        while (done==False):
            msg = await client.wait_for('message', check=check)
            await ctx.author.send('order placed')
            if (msg.guild==None):
                   content=msg.content
                   if (content=='Done'):
                        done=True
                   else:
                        number=content[-1]
                        length=len(content)
                        element=content[0:(length-2)]
                        cost=cost+Cost.get_cost(element,number) 
        await ctx.author.send('order placed')

            #@commands.Cog.listener()
           # async def on_message(self,message):
               # if (message.guild==None):
                   # content=message.content
                   # if (content=='Done'):
                     #   done=True
                   # else:
                    #    number=content[-1]
                    #    length=len(content)
                     #   element=content[0:(length-2)]
                     #   cost=Cost.get_cost(element,number) 

 
   
    @commands.command()
    async def ordername(self,ctx):
        name=orders_list[0].get_player()
        await ctx.send(f'{name}') 
        
    @commands.command()
    async def test(self,ctx):
        await ctx.send(f'{test_number}')

def setup(client):
    client.add_cog(order_commands(client))


