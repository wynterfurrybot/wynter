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

class MyView(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Vote in the poll", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Yes",
                description="Vote yes in the poll"
            ),
            discord.SelectOption(
                label="No",
                description="Vote no in the poll"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        if select.values:
            await interaction.response.edit_message(content = f"{interaction.message.content} \n\n{interaction.user.mention} voted {select.values[0]}!", view=self)
        else:
            await interaction.response.send_message("No vote was selected.")

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(pass_context=True, help = 'See the full list of commands (including those ones not shown as slash commands)', description = 'See the full list of commands (including those ones not shown as slash commands)')
    async def help(self, ctx):
        prefix = await self.bot.get_prefix(ctx.message)
        prefix = prefix[2]
        await ctx.respond(f"Please run `{prefix}help` on the bot for a full list of commands. \n\nSome commands are not yet implemented as slash commands, so this command will give you a full list of the bot's commands!")

   


    @commands.command(name='poll', help='Make a poll')
    async def poll(self, ctx, *, question):
        await ctx.send(f"{ctx.author.display_name} asks: {question}", view=MyView())

    @commands.command(name = 'info', pass_context=True, help = 'Shows bot info')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def info(self, ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title = "Bot Information", description = "Libraries used:\nPython v3.9.0 \nPy-Cord v2.3.2 \nPyMySQL v0.10.1 \nOwOify v0.3.1  \n\nAdditional Credits:\njackdotmc - Linux server help.\nNanofaux#0621 - for helping aide me into Python. \nMurdecoi#3541 - for aiding with moderation command testing. \nSkipper:tm:#6968 - for their suggestion of the RP scenario generator. \nAll the beta testers listed in the `testers` command \n\nCheck bot uptime: https://uptime.furrybot.dev/ \n\nSupport Server: https://discord.gg/EG5pUEmnXb", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'privacy', pass_context=True, help = 'Shows bot privacy policy')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def privacy(self, ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title = "Privacy Policy", description = "See our privacy policy here: \n\nhttps://docs.furrycentr.al/privacy", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'testers', pass_context=True, help = 'Shows a list of beta testers')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def testers(self, ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title = "Thank you to everyone listed here!", description = "BETA TESTERS: \n\nBananaBoopCrackers#2002 \nFinnick The Fennec Fox#4334 \nMurdecoi#3541 \nNexivis#8546 \nNootTheNewt#0060 \nSia#3027 \n:six_pointed_star:Mrs-copper-pp:scorpius:#2688 \nMay The Red Panda Cat#8986 \nNitrax#8972 \nRag Darkheart#5080 \nruby_rose_wolf#0568 \nSkipper#6968 \nSugerrion#4086 \nTyler Furrison#2454", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'ping', pass_context=True, help= 'Shows the bot latency connecting to discord.')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def ping(self,ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        shard_id = ctx.guild.shard_id
        shard = self.bot.get_shard(shard_id)
        ping = math.floor(shard.latency * 1000)
        before = time.monotonic()
        embed = discord.Embed(title = "Ping!", description = 'Getting info, please wait...', color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        msg = await ctx.send(embed = embed)
        latency = math.floor((time.monotonic() - before) * 1000)
        embed = discord.Embed(title = "Ping!", description = f'Pong! \n\nConnection to discord: \n{ping}ms\nMessage Latency:\n{latency}ms', color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        await msg.edit(embed=embed)
    
    @commands.command(name = 'Shard', pass_context=True, help= 'Shows the current shard information')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def shard(self,ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        shard_id = ctx.guild.shard_id
        shard = self.bot.get_shard(shard_id)
        ping = math.floor(shard.latency * 1000)
        before = time.monotonic()
        embed = discord.Embed(title = "Shard Info!", description = 'Getting info, please wait...', color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        msg = await ctx.send(embed = embed)
        latency = math.floor((time.monotonic() - before) * 1000)
        embed = discord.Embed(title = "Shard Info", description = f'Shard ID: {shard_id}! \n\nConnection to discord: \n{ping}ms\nMessage Latency:\n{latency}ms', color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        await msg.edit(embed=embed)



    @commands.command(name = 'invite', pass_context=True, help= 'Shows the bot\'s invite.')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self,ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title = "Here ya go!", description = "My invite is https://furrycentr.al/add" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'avatar', pass_context=True, help= 'Shows the profile picture of a mentioned user.', aliases=["pfp"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    async def avatar(self,ctx, user : discord.Member):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title = f"{user.display_name}'s Profile Picture", color=0x00ff00)
        embed.set_image(url = user.avatar.url)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'serverinfo', pass_context= True, help='Shows information about the current guild')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def serverinfo(self,ctx):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        embed = discord.Embed(title=ctx.message.guild.name, color=0x00ff00)
        embed.add_field(name="Owner", value=ctx.message.guild.owner, inline=False)
        embed.add_field(name="Date of creation", value=ctx.message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Region", value=ctx.message.guild.region, inline=False)
        m = ctx.guild.members
        u = 0
        b = 0
        for m in m:
            if m.bot:
                b +=1
            else:
                u +=1
        embed.add_field(name="Members", value = f"users: {u} bots: {b}", inline = False)
        embed.set_thumbnail(url = ctx.message.guild.icon.url)
        return await ctx.message.channel.send(embed=embed)
    
    @commands.command(name = 'mass', pass_context= True, help='Send a mass message', aliases = ['mm'])
    @commands.is_owner()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def mm(self,ctx, *, message: str):
        for guild in self.bot.guilds:
            owner = guild.owner
            count = 0
            try:
                await owner.send(f"**This is an important message from the developers of Wynter:** \n\n{message}")
                count = count + 1
                print(f"sent mass message {count}")
            except Exception as e:
                print(f"Failed mass message - {e}")
            await asyncio.sleep(1)

    
    @commands.command(name = 'userinfo', pass_context= True, help='Shows information about the current guild', aliases = ['profile'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def userinfo(self,ctx, user: discord.Member):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
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
        return await ctx.message.channel.send(embed=embed)

    @commands.command(name='report', pass_context = True, help='Report a bug to the bot\'s developers')
    @commands.guild_only()
    @commands.cooldown(1,120, commands.BucketType.user)
    async def report(self, ctx, *report):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        return await ctx.message.channel.send("To report a bug or an issue with our bot - please raise a ticket at https://github.com/wynterfurrybot/wynter/issues")
    
    @commands.command(name='feedback', pass_context = True, help='Send feedback to the bot\'s developers')
    @commands.guild_only()
    @commands.cooldown(1,120, commands.BucketType.user)
    async def feedback(self, ctx, *report):
        try:
            if "im:0" in ctx.channel.topic:
                return
        except Exception as e:
            print (e)
        return await ctx.message.channel.send("To report a bug or an issue with our bot - please raise a ticket at https://github.com/wynterfurrybot/wynter/issues")

async def setup(bot):
    await bot.add_cog(Info(bot))