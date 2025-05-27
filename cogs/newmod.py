from ast import alias
import sys, traceback
import discord
from discord.ext import commands
from discord.utils import get
import time
import random
import os
from dotenv import load_dotenv
import json
import asyncio
import pymysql.cursors
from datetime import datetime, timedelta
import humanfriendly

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

punisheduser = None
punishmenttype = None

class PurgeModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Number", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        amount = int(self.children[0].value)
        amount = amount + 1
        if amount > 100:
            amount = 100
        await interaction.channel.purge(limit = amount, check = lambda msg: not msg.pinned)
        embed = discord.Embed(title = "Messages Purged!", description = f"{interaction.user.display_name} has deleted {amount} messages from {interaction.channel.mention}!" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(interaction.guild.text_channels, name='message_logs')
        await channel.send(embed=embed)
        channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
        await interaction.send_response(content = "Succesfully purged messages", ephemeral = True)

class ReasonModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Reason", style=discord.InputTextStyle.long))
        if punishmenttype == "mute":
            self.add_item(discord.ui.InputText(label="Punishment time", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        reason = self.children[0].value
        if punishmenttype == "kick":
            embed = discord.Embed(title = "Kicked!", description = f"You have been kicked from {interaction.guild.name}! \n\nReason given:\n{reason}" , color=0x00ff00)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            try:
                await punisheduser.send(embed = embed)
            except Exception as e:
                pass
            await punisheduser.kick(reason = self.children[0].value)
            embed = discord.Embed(title = "Kicked!", description = f"{interaction.user.display_name} has kicked {punisheduser.display_name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
            await interaction.response.send_message(content = "Succesfully kicked user", ephemeral = True)
        if punishmenttype == "ban":
            embed = discord.Embed(title = "Banned!", description = f"You have been banned from {interaction.guild.name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            try:
                await punisheduser.send(embed = embed)
            except Exception as e:
                pass
            await punisheduser.ban(reason = self.children[0].value)
            embed = discord.Embed(title = "Banned!", description = f"{interaction.user.display_name} has kicked {punisheduser.display_name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
            await interaction.response.send_message(content = "Succesfully banned user", ephemeral = True)
        if punishmenttype == "warn":
            embed = discord.Embed(title = "Warned!", description = f"You have been warned on {interaction.guild.name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            try:
                await punisheduser.send(embed = embed)
            except Exception as e:
                pass
            embed = discord.Embed(title = "Warned!", description = f"{interaction.user.display_name} has warned {punisheduser.display_name}! \n\nReason given:\n{reason}" , color=0xf08f07)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
            await interaction.response.send_message(content = "Succesfully warned user", ephemeral = True)
        if punishmenttype == "mute":
            embed = discord.Embed(title = "Muted!", description = f"You have been muted on {interaction.guild.name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            try:
                await punisheduser.send(embed = embed)
            except Exception as e:
                pass
            try:
                time = self.children[1].value
                time = humanfriendly.parse_timespan(time)
                await punisheduser.timeout_for(duration = timedelta(seconds=time), reason = reason)
            except Exception as e:
                return await interaction.response.send_response(f"Uh oh, you encoutred an error: \n{e} \n\nPlease report this to the devs!")
            embed = discord.Embed(title = "Muted!", description = f"{interaction.user.display_name} has muted {punisheduser.display_name}! \n\nReason given:\n{reason}" , color=0xf08f07)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
            await interaction.response.send_message(content = "Succesfully muted user", ephemeral = True)
        if punishmenttype == "unmute":
            embed = discord.Embed(title = "Unmuted!", description = f"You have been unmuted on {interaction.guild.name}! \n\nReason given:\n{reason}" , color=0xf03907)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            try:
                await punisheduser.send(embed = embed)
            except Exception as e:
                pass
            try:
                await punisheduser.remove_timeout(reason = reason)
            except Exception as e:
                return await interaction.response.send_message(f"Uh oh, you encoutred an error: \n{e} \n\nPlease report this to the devs!")
            embed = discord.Embed(title = "Unmuted!", description = f"{interaction.user.display_name} has unmuted {punisheduser.display_name}! \n\nReason given:\n{reason}" , color=0xf08f07)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(interaction.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
            await interaction.response.send_message(content = "Succesfully removed user's timeout", ephemeral = True)
       
class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
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
            
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f"cogs.{extension}")
        except Exception as e:
            embed = discord.Embed(title='Reload', description=f'Problem whilst reloading {extension}. \n\n{e}', color=0xFFA500)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0x00FF00)
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            embed = discord.Embed(title='Unload', description=f'Problem whilst unloading {extension}. \n\n{e}', color=0xFFA500)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Reload', description=f'{extension} successfully unloaded', color=0x00FF00)
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            embed = discord.Embed(title='Load', description=f'Problem whilst loading {extension}. \n\n{e}', color=0xFFA500)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Load', description=f'{extension} successfully loaded', color=0x00FF00)
            await ctx.send(embed=embed)

    @discord.user_command(name = "Kick user")
    @commands.has_guild_permissions(kick_members = True)
    async def akick(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "kick"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.user_command(name = "Ban user")
    @commands.has_guild_permissions(ban_members= True)
    async def aban(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "ban"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @commands.command(name = 'hackban', pass_context=True, help = 'Bans user(s) that aren\'t in the guild.')
    @commands.has_guild_permissions(ban_members= True)
    @commands.cooldown(1,120, commands.BucketType.user)
    async def hackban(self, ctx,*ids):
        try:
            await ctx.message.delete()
        except Exception as e:
            await ctx.send("Failed deleting the command message. It is strongly reccomended to give the bot manage messages permission to do this.")
        if len(ids) > 50:
            embed = discord.Embed(title = "Lol no.", description = "Try mentioning less than 50 IDs. (Austin, i'm looking at you)" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        
        bannedusers = 0
        bannedlist = ""
        for user in ids:
            if user == "!hackban":
                print("no user")
            else:
                try:
                    bannedlist = bannedlist + user + ", "
                    bannedusers = bannedusers +1
                    print(user)
                    u = await self.bot.fetch_user(int(user))
                    await ctx.message.guild.ban(u, reason = f"Hackbanned by {ctx.message.author.display_name}")
                except Exception as e:
                    print(f"Exception: {e}")
                    await ctx.send("Error banning {user} - " + e)

        await ctx.send(f"Banned IDS: \n\n{bannedlist}")
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        embed = discord.Embed(title = "Hackbanned, get out of here, ya dirty trolls.", description = f"{ctx.message.author.display_name} Hackbanned {bannedusers} user(s)" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await channel.send(embed=embed)

    
    @discord.user_command(name = "Warn user")
    @commands.has_guild_permissions(kick_members = True)
    async def awarn(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "warn"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.user_command(name = "Mute user")
    @commands.has_guild_permissions(kick_members = True)
    async def amute(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "mute"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.user_command(name = "Unmute user")
    @commands.has_guild_permissions(kick_members = True)
    async def aunmute(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "unmute"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "kick"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(ban_members= True)
    async def ban(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "ban"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(kick_members = True)
    async def warn(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "warn"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(kick_members = True)
    async def mute(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "mute"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member):
        global punisheduser
        global punishmenttype
        punishmenttype = "unmute"
        if ctx.author.id == member.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
            return await ctx.send(embed=embed)
        else:
            modal = ReasonModal(title="Please enter a reason.")
            punisheduser = member
            await ctx.send_modal(modal)
    
    @discord.slash_command()
    @commands.has_guild_permissions(kick_members = True)
    async def purge(self, ctx):
        modal = PurgeModal(title="How many to delete?")
        await ctx.send_modal(modal)

        
            


def setup(bot):
    bot.add_cog(Moderation(bot))