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

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
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
    
    @commands.command(name = 'buddybox', help = "only works in Rusted Rover")
    async def buddybox(self, ctx):
        await ctx.reply("Please check your dms.")
        user = ctx.message.author
        await user.send("Hi there, may I get your feedback?")
        def check(m):
            return m.author.id == user.id
        msg = await self.bot.wait_for('message', check = check)
        feedback = msg.content
        await user.send("Would you like your query to be anonymous? YES/NO")
        msg = await self.bot.wait_for('message', check = check)
        anon = msg.content.lower()
        if anon == "yes":
            embed = discord.Embed(title = "Anonymous message", description = f"{feedback}", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
        elif anon== "no":
            embed = discord.Embed(title = f"Message from {user.display_name}", description = f"{feedback}", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
        await user.send("Would you consider your query to be urgent? (This should only be used if your query is absolutely urgent) YES/NO")
        msg = await self.bot.wait_for('message', check = check)
        urgent = msg.content.lower()
        try:
            mod = discord.utils.get(ctx.message.guild.text_channels, id = 976927282679668747)
            if urgent == "yes":
                await mod.send("<@&882820973928284180> ", embed = embed)
            elif urgent == "no":
                await mod.send(embed = embed)
        except Exception as e:
            await user.send(f"Exception: {e}")
        await user.send("Your query has been sent. :)")
    
    @commands.command(name= 'send')
    async def send(self, ctx, channel):
        ip = ""
        def check(m):
            return m.author.id == user.id


        await ctx.reply("Please say the title of the embed")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        title = msg.content
        print(title)

        embed = discord.Embed(title = f"{title}", color=0x00ff00)
        
        await ctx.reply("Do you want this embed to contain fields?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        ip = msg.content

        if inpiput.lower() == "yes":
            while True:
                await ctx.reply("Please enter the tile of the field, or enter continue to stop.")
                await asyncio.sleep(1)
                msg = await self.bot.wait_for('message', check = check)
                etitle = msg.content
                if etitle.lower() == "continue":
                    break
               

                await ctx.reply("Please enter the content of the field")
                await asyncio.sleep(1)
                msg = await self.bot.wait_for('message', check = check)
                econtent = msg.content
                embed.add_field(title = etitle, value = econtent)
        elif ip.lower() == "no":
            await ctx.reply("Please enter the content of the embed")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            ip = msg.content
            embed.description = ip

        await ctx.reply("Please enter the footer of the embed")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        ip = msg.content
        embed.footer = ip
        await channel.send(embed = embed)
        

    @commands.command(name = 'approve', help = "only works in Brumal Cafe")
    @commands.has_guild_permissions(kick_members = True)
    async def approve(self, ctx, user:discord.Member):
        guild = user.guild
        role = discord.utils.get(guild.roles, id = 931359323186135041)
        await user.add_roles(role)
        userchan = discord.utils.get(user.guild.text_channels, name = str(user.id))
        await userchan.delete()
        gen = discord.utils.get(user.guild.text_channels, id = 945009832598061126)
        await gen.send(f"<@&932054177717293096> please welcome {user.mention}! \n\nFeel free to grab some roles in <#995762026280407162> and make yourself at home!")
    
    @commands.command(name = 'restart-reg', help = "only works in Fennecs Den and Brumal Cafè")
    @commands.has_guild_permissions(kick_members = True)
    async def rereg(self, ctx, user:discord.Member, *, reason = None):
        userchan = discord.utils.get(user.guild.text_channels, name = str(user.id))
        await userchan.send(f"Hey {user.mention} -- Your registration is in the process of being restarted. Please proceed in the new channel (This will be created in 10 seconds)")
        await ctx.message.delete()
        await asyncio.sleep(10)
        await userchan.delete()
        if user.guild.id == 931357551768002610:
            if reason == None:
                reason = "no reason given"
            guild = user.guild
            category = discord.utils.get(user.guild.categories, name = 'verification')
            channel = await guild.create_text_channel(str(user.id), category=category)
            def check(m):
                return m.author.id == user.id
            await channel.set_permissions(user, read_messages=True)
            role = discord.utils.get(guild.roles, name="@everyone")
            staff = discord.utils.get(guild.roles, name="Staff")
            await channel.set_permissions(role, read_messages=False)
            await channel.set_permissions(staff, read_messages=True, manage_channels= True)

            await channel.send(f"Hey, {user.mention}. \n\nYour registration was restarted by {ctx.message.author.mention} with the reason below: \n{reason}. \n\nTo proceed through verification, I just need you to answer a few questions.")
            await channel.send("First, what would you prefer to be called in this server?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            await channel.send("Next, may I get your age? (Please provide a whole number)")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            try:
                age = int(msg.content)
            except:
                await channel.send("That is an invalid age. \n\nYour registration has been aborted. Please contact staff to continue.")
            if age < 13:
                await user.send("You are underaged. According to discord TOS, users under 13 are not allowed to use the application. Read more here \n\nhttps://discord.com/terms")
                await user.guild.ban(user, reason = "Underaged user, banned due to TOS violation.")
                await channel.delete()
            await channel.send("Thank you, next, may I know what gender and pronouns you identify as?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            await channel.send("Great, may I ask your preference on DMs? ALLOW/DENY/ASK FIRST")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            if msg.content.lower() != "allow" or msg.content.lower() != "deny" or msg.content.lower() != "ask" or msg.content.lower() != "ask first":
                channel.send("That is an invalid answer. Your registration has been aborted. Please contact staff to continue.")
            await channel.send("Great, may I ask your preference on mentions? YES/NO")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            if msg.content.lower() != "yes" or msg.content.lower() != "no":
                channel.send("That is an invalid answer. Your registration has been aborted. Please contact staff to continue.")
            await channel.send("Finally, tell me about your fursona. \n\nWhat species are they? What's their favourite activites? What gender are they? Do they like sleeping all day? Anything! \n\nNote: if you don't have a fursona, tell us info of what you imagine your fursona to be!")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            await channel.send("All done! \n\n<@&931367540289060915> will now review your application. Please wait. \n\nShould you need any further assistance, please type here and a member of staff will get to you ASAP.")
            await channel.send("Also, may I ask you, what did you think of this registration process? All feedback is welcome, including any suggestions for improvements.")
        
        if user.guild.id == 986242703866081320:
            if reason == None:
                reason = "no reason given"
            category = discord.utils.get(user.guild.categories, name = '『📃』Welcome')
            channel = await guild.create_text_channel(str(user.id), category=category)
            def check(m):
                return m.author.id == user.id
            await channel.set_permissions(user, read_messages=True, read_message_history= True, send_messages= True)
            role = discord.utils.get(guild.roles, name="@everyone")
            goobs = discord.utils.get(guild.roles, id = 990655069387100170) 
            staff = discord.utils.get(guild.roles, id = 990671590217908224) 
            wynter = discord.utils.get(guild.roles, id = 1003063184564944909)
        
            await channel.set_permissions(role, read_messages=False)
            await channel.set_permissions(goobs, read_messages=False)
            await channel.set_permissions(staff, read_messages=True, manage_channels = True)
            await channel.set_permissions(wynter, send_messages=True)
        

            await channel.send(f"Hey, {user.mention}. \n\nYour registration was restarted by {ctx.message.author.mention} with the reason below: \n{reason}. \n\nTo proceed through verification, I just need you to answer a few questions.")
            await channel.send("First, what made you join the server?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            join = msg.content
            await channel.send("Next, may I get your date of birth? (DD/MM/YYYY please)")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            dob = msg.content
            await channel.send("Thank you, next, may I know what country you reside in?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            country = msg.content
            await channel.send("Great, Now, may I ask what species is your fursona, if you have one? Or what species is your OC (original character)?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            species = msg.content
            await channel.send("Great, Now, if your friends could describe you in a few sentences, what would they say?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            you = msg.content
            await channel.send("Great, Now, in your own words, what is a furry?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            furry = msg.content
            await channel.send("Great, how has the fandom benefitted you, and how has it not?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            benefits = msg.content
            
            

            intros = discord.utils.get(user.guild.text_channels, id = 990660754841698325)
            embed = discord.Embed(title = "Introduction!", description = f"{user.mention}'s Introduction" , color=0x00ff00)
            if user.avatar:
                    embed.set_thumbnail(url = user.avatar.url) 
            embed.add_field(name='What made you join the server?', value=f"{join}", inline=False)
            embed.add_field(name='DOB', value=f"{dob}", inline=False)
            embed.add_field(name='Resides in', value=f"{country}", inline=False)
            embed.add_field(name='Fursona details', value=f"{species}", inline=False)
            embed.add_field(name='Friends describe them as', value=f"{you}", inline=False)
            embed.add_field(name='In own words, what is a furry', value=f"{furry}", inline=False)
            embed.add_field(name='How was the fandom benefitted you?', value=f"{benefits}", inline=False)
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            await intros.send(embed = embed)
            await channel.send("Great, finally, have you made sure to read the <#990656415687389325> and do you agree to them? \n\n(If you answer yes and have not read the rules, it will be assumed that you have and that you understand them)")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            await channel.send("All done! \n\n<@&990671590217908224> will now review your application. Please wait. \n\nShould you need any further assistance, please type here and a member of staff will get to you ASAP.")
            await channel.send("Also, may I ask you, what did you think of this registration process? All feedback is welcome, including any suggestions for improvements.")
            
        
    @commands.command(name = 'register', pass_context=True, help = 'Register for Floof Paradise! (only works in guild)')
    async def register(self, ctx):
        if not ctx.message.guild.id == 754816860133916822:
            return
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        a = ctx.message.author
        await a.send("Hi there, welcome to the Floof Paradise registration. \n\nDuring this process, please do not send any messages to servers Wynter is in, or it may see it as answers to your questions.\n\nTo start, I get your fursona name or a name you prefer to be called?")
        def check(m):
            return m.author.id == a.id
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        name = msg.content
        await a.send(f"Hi {name} - May I next get your age?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        age = 0
        agebracket = ""
        try:
            age = int(msg.content)
        except:
            await ctx.message.author.send("That is an invalid age. \n\nPlease try again or your registration will be aborted.")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            try:
                age = int(msg.content)
            except:
                await ctx.message.author.send("That is an invalid age. \n\nYour registration has been aborted")
        if age < 13:
            await a.send("You are underaged. According to discord TOS, users under 13 are not allowed to use the application. Read more here \n\nhttps://discord.com/terms")
            await ctx.message.guild.ban(a, reason = "Underaged user, banned due to TOS violation.")
            return
        if age >= 18:
            agebracket = "Adult"
        if age < 18:
            agebracket = "Minor"
        await a.send(f"Thanks, to protect your age, you will be shown as a {agebracket} in the server. \n\nNext, may I know what gender you identify as and your preferred pronouns?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        gender = msg.content
        await a.send(f"Got it, you refer to yourself as {gender} \n\nNext, would you like to be mentioned in the server for things such as important announcements? (YES/NO)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        announcementpref = msg.content
        await a.send("Got it, next, may I ask if it's okay for users to DM you? (YES/NO/ASK)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        dmpref = msg.content
        await a.send("Finally, tell me about your fursona. \n\nWhat species are they? What's their favourite activites? What gender are they? Do they like sleeping all day? Anything! \n\nNote: if you don't have a fursona, tell us info of what you imagine your fursona to be!")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        fursonainfo = msg.content

        embed = discord.Embed(title = "Registration!", description = f"{a.mention}'s Registration" , color=0x00ff00)
        embed.set_thumbnail(url = a.avatar.url)
        embed.add_field(name='Preferred Name', value=f"{name}", inline=False)
        embed.add_field(name='Age', value=f"{agebracket}", inline=False)
        embed.add_field(name='Gender and Pronouns', value=f"{gender}", inline=False)
        embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        embed.add_field(name='Okay to mention?', value=f"{announcementpref}", inline=False)
        embed.add_field(name='Okay to DM?', value=f"{dmpref}", inline=False)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='introductions')
        await channel.send("<@&754817901428604929>")
        await channel.send(embed=embed)
        await a.send("Thank you! Your registration has been sent to a staff member for review. \n\nThey'll accept you as soon as possible!")



    @commands.command(name = 'kick', pass_context=True, help = 'Kicks a user')
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"KICK", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Kicked!", description = f"You have been kicked from {ctx.message.guild.name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
        except Exception as e:
            print(e)
        await user.kick()
        embed = discord.Embed(title = "Kicked!", description = f"{ctx.message.author.display_name} has kicked {user.display_name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
        

    @commands.command(name = 'ban', pass_context=True, help = 'Bans a user')
    @commands.has_guild_permissions(ban_members= True)
    async def ban(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"BAN", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Banned!", description = f"You have been banned from {ctx.message.guild.name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed, file = discord.File("./saygoodbye.mp4"))
        except Exception as e:
            print(e)
        await user.ban(reason = reason)
        embed = discord.Embed(title = "Banned!", description = f"{ctx.message.author.display_name} has banned {user.display_name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
    
    @commands.command(name = 'remind', pass_context=True, help = 'Set a reminder')
    @commands.cooldown(1,120, commands.BucketType.user)
    async def remind(self, ctx, minutes: float, *, reminder):
        embed = discord.Embed(title = f"{minutes} minute reminder!", description = f"I have set a reminder to remind you about {reminder} - check your DMs soon!" , color=0x00ff00)
        minutes = minutes * 60
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(embed= embed, reference = ctx.message)
        await asyncio.sleep(minutes)
        embed = discord.Embed(title = "Your Reminder", description = f"{reminder}" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.message.author.send(embed = embed)
    
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
        
    
    @commands.command(name = 'warn', pass_context=True, help = 'Warns a user')
    @commands.has_guild_permissions(kick_members = True)
    async def warn(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"WARN", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Warned!", description = f"You have been warned on {ctx.message.guild.name}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await user.send(embed=embed)
        embed = discord.Embed(title = "Warned!", description = f"{ctx.message.author.display_name} has warned {user.mention}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
       
    
    @commands.command(name = 'purge', pass_context=True, help = 'Purges x amount of messages', aliases = ['clear', 'clean'])
    @commands.has_guild_permissions(kick_members = True)
    async def purge(self, ctx, amount: int):
        amount = amount + 1
        if amount > 100:
            amount = 100
        await ctx.message.channel.purge(limit = amount, check = lambda msg: not msg.pinned)
        embed = discord.Embed(title = "Messages Purged!", description = f"{ctx.message.author.display_name} has deleted {amount} messages from {ctx.message.channel.mention}!" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='message_logs')
        await channel.send(embed=embed)
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
    
    @commands.command(name = 'lookup', pass_context=True, help = 'see a user\'s punishments')
    @commands.has_guild_permissions(kick_members = True)
    async def lookup(self, ctx):
        def check(m):
            return m.author.id == ctx.message.author.id
        await ctx.reply("As a reply to this message, please either mention a user or give me an ID of a user to see their current punishment history. \n\nNote: any punishments not recorded via Wynter will not show here!")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        try:
            id = int(msg.content)
            await ctx.send(f"ID: {id}")
        except ValueError:
            id = msg.mentions[0].id
            await ctx.send(f"ID: {id}")
        user = await self.bot.fetch_user(id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `punishments` WHERE `offenderid`=%s AND serverid = %s"
                cursor.execute(sql, (user.id, ctx.message.guild.id))
                result = cursor.fetchall()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                punishments = ""
                pcount = 0
                for p in result:
                    pcount = pcount +1 
                    punishments = punishments + "**" + p['type'] + "**" + ": " + p['reason'] + "\n\nGiven by: \n" + p['moderator'] + "\n\n"
            embed = discord.Embed(title = f"{user.display_name}'s punishments!", description = punishments , color=0x00ff00)
            embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069 | {pcount} total punishments')
            connection.close()
            return await ctx.send(embed=embed)
        except Exception as err:
            print(err)
            return await ctx.send(f"an error occured - {err} - this user may have no punishments recorded")
    
        
    
    @commands.command(name = 'mute', pass_context=True, help = 'Mutes a user', aliases=["timeout"])
    @commands.has_guild_permissions(kick_members = True)
    async def mute(self, ctx, user:discord.Member,time = None,*, data:str):
        data = str(data)
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"MUTE", data, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Muted!", description = f"You have been muted on {ctx.message.guild.name}! \n\nReason given: \n{data}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
            try:
                time = humanfriendly.parse_timespan(time)
                await user.timeout_for(duration = timedelta(seconds=time), reason = data)
            except Exception as e:
                await ctx.message.channel.send(f"Error: {e}")
                print(traceback.format_exc())
                
            embed = discord.Embed(title = "Muted!", description = f"{ctx.message.author.display_name} has muted {user.mention}! \n\nReason given: \n{data}" , color=0x00ff00)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
       
    @commands.command(name = 'unmute', pass_context=True, help = 'Mutes a user', aliases=["rem-timeout"])
    @commands.has_guild_permissions(kick_members = True)
    async def unmute(self, ctx, user:discord.Member,*, data:str):
        data = str(data)
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"UNMUTE", data, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Unmuted!", description = f"You have now been unmuted on {ctx.message.guild.name}! \n\nReason given: \n{data}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
            try:
                await user.remove_timeout(reason = data)
            except Exception as e:
                await ctx.message.channel.send(f"Error: {e}")
                print(traceback.format_exc())
                
            embed = discord.Embed(title = "Unmuted!", description = f"{ctx.message.author.display_name} has unmuted {user.mention}! \n\nReason given: \n{data}" , color=0x00ff00)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
       


def setup(bot):
    bot.add_cog(Moderation(bot))