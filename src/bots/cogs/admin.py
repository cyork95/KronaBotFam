import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help("Deletes the specified number of chats. Default is 2 messages."))
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount_to_delete=2):
        """Clears an amount of Messages."""
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount_to_delete)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member."""
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for {reason}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member."""
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        """Unban a member."""
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}#{user.discriminator}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member = None):
        """Mute a member."""
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(member.mention + " You have been muted. Please reflect on what you said or did and come back "
                                        "refreshed and ready to do better.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member = None):
        """Unmute a member."""
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(member.mention + " You have been unmuted. Enjoy your new freedom!.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, member: discord.Member, role=None):
        """Add a role to a member."""
        await ctx.message.delete()
        discord_role = discord.utils.get(ctx.guild.roles, name=role)
        await member.add_roles(discord_role)
        await ctx.send(member.mention + f' You have been added to the role: {role}. Enjoy your new role!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_role(self, ctx, member: discord.Member, role=None):
        """Remove role from member."""
        await ctx.message.delete()
        discord_role = discord.utils.get(ctx.guild.roles, name=role)
        await member.remove_roles(discord_role)
        await ctx.send(member.mention + f' You have been removed from the role: {role}.')


def setup(client):
    client.add_cog(Admin(client))
