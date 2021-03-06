import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help("Deletes the specified number of chats. Default is 2 messages."))
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount_to_delete=2):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount_to_delete)

    @clear.error
    async def clear_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a number?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

    @ban.error
    async def ban_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}#{user.discriminator}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member = None):
        """Mute a member."""
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(member.mention + " You have been muted. Please reflect on what you said or did and come back "
                                        "refreshed and ready to do better.")

    @mute.error
    async def mute_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member = None):
        """Unmute a member."""
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(member.mention + " You have been unmuted. Enjoy your new freedom!.")

    @unmute.error
    async def unmute_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, member: discord.Member, role=None):
        await ctx.message.delete()
        discord_role = discord.utils.get(ctx.guild.roles, name=role)
        await member.add_roles(discord_role)
        await ctx.send(member.mention + f' You have been added to the role: {role}. Enjoy your new role!')

    @add_role.error
    async def add_role_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user and a role?')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_role(self, ctx, member: discord.Member, role=None):
        await ctx.message.delete()
        discord_role = discord.utils.get(ctx.guild.roles, name=role)
        await member.remove_roles(discord_role)
        await ctx.send(member.mention + f' You have been removed from the role: {role}.')

    @remove_role.error
    async def remove_role_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you type a user and a role?')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
