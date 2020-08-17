import discord
from discord.ext import commands, tasks

class admin_commands(commands.Cog):
    
    def _init_(self,client):
        self.client=client
        
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an ammount of messages to delete')

    @commands.command()
    async def kick(self,ctx, member : discord.Member, *,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked from the server')
    
    @commands.command()
    async def ban(self,ctx, member : discord.Member, *,reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator =member.split('#')
        for ban_entry in banned_users:
            user=ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned{user.mention}')
                return

    @commands.command()
    async def load(self,ctx, extention):
        client.load_extension(f'cogs.{extention}')

    @commands.command()
    async def unload(self,ctx, extention):
        client.unload_extension(f'cogs.{extention}')

def setup(client):
    client.add_cog(admin_commands(client))
