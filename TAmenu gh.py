import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/help", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is working now!")

@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=JOIN_ROLE_ID)
    channel = member.guild.system_channel
    
    embed = disnake.Embed(
        title="New member!",
        description = f"{member.name}#{member.discriminator}",
        color = 0x00ff00
    )
    
    await member.add_roles(role)
    await channel.send(embed=embed)
    
@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="No reason"):
    await ctx.send(f"{member.mention} was kicked")
    await member.kick(reason=reason)
    await ctx.massage.delite()

bot.run("APP_TOKEN")
