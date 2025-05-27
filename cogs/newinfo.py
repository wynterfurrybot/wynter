import discord
from discord.ext import commands, bridge
from discord.commands import Option
from discord.ui import Select, View
import time 
import math
import pymysql.cursors
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')

def connecttodb():
    # Connect to the database
    connection = pymysql.connect(host=DBHOST,
                                user=DBUSER,
                                password=DBPW,
                                db=DB,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command()
    async def commands(self,ctx):
        embed = discord.Embed(title = "List of commands", color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        global_commands = await self.bot.fetch_guild_commands(ctx.guild.id)
        for command in global_commands:
            embed.add_field(name= command.name, value = command.description)
        return await ctx.respond(embed = embed)
            
    
    @discord.slash_command()
    async def info(self, ctx):
        embed = discord.Embed(title = "Bot Information", description = "Thanks to: Jackdotmc for Linux help. \n\nLibraries used:\nPython v3.9.0 \nPy-Cord v2.5.0rc5 \nPyMySQL v0.10.1 \nOwOify v0.3.1  \n\nCheck bot uptime: https://uptime.furrybot.dev/ \n\nSupport Server: https://discord.gg/EG5pUEmnXb", color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def privacy(self, ctx):
        embed = discord.Embed(title = "Privacy Policy", description = "See our privacy policy here: \n\nhttps://docs.furrybot.dev/privacy", color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def ping(self, ctx):
        shard_id = ctx.guild.shard_id
        shard = self.bot.get_shard(shard_id)
        ping = math.floor(shard.latency * 1000)
        before = time.monotonic()
        embed = discord.Embed(title = "Ping!", description = 'Getting info, please wait...', color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        msg = await ctx.respond(embed = embed)
        latency = math.floor((time.monotonic() - before) * 1000)
        embed = discord.Embed(title = "Ping!", description = f'Pong! \n\nConnection to discord: \n{ping}ms\nMessage Latency:\n{latency}ms', color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        await msg.edit(embed=embed)
    
    @discord.slash_command()
    async def shard(self, ctx):
        shard_id = ctx.guild.shard_id
        shard = self.bot.get_shard(shard_id)
        ping = math.floor(shard.latency * 1000)
        before = time.monotonic()
        embed = discord.Embed(title = "Shard Info!", description = 'Getting info, please wait...', color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        msg = await ctx.respond(embed = embed)
        latency = math.floor((time.monotonic() - before) * 1000)
        embed = discord.Embed(title = "Shard Info", description = f'Shard ID: {shard_id}! \n\nConnection to discord: \n{ping}ms\nMessage Latency:\n{latency}ms', color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        await msg.edit(embed=embed)

    @discord.slash_command()
    async def invite(self, ctx):
        embed = discord.Embed(title = "Here ya go!", description = "My invite is https://furrybot.dev/add" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def get_pfp(self, ctx, user: discord.Member):
        embed = discord.Embed(title = f"{user.display_name}'s Profile Picture", color=0x00ff00)
        embed.set_image(url = user.avatar.url)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    
    @discord.slash_command()
    async def get_userinfo(self, ctx, user: discord.Member):
        rolelist = ''
        roles = 0
        for role in user.roles:
            roles +=1
            if role.name == "@everyone":
                continue
            rolelist = rolelist + role.mention + " "
        if roles == 1:
            rolelist = 'No roles set'
        embed = discord.Embed(description = str(user.name) + "#" +str(user.discriminator) , color = 0x00ff00)
        embed.set_thumbnail(url = user.avatar.url)
        embed.add_field(name = "Name:", value = user.display_name, inline = False)
        embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
        embed.add_field(name = "Date Joined:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
        embed.add_field(name = "Roles:", value=rolelist, inline = False)
        return await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))