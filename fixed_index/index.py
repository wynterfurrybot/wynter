# bot.py
import os
from this import d

import discord
from discord import Embed
from discord.ext import commands
from dotenv import load_dotenv
import math
import pymysql.cursors
import json
import sys, traceback
import time
import random
import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')

bumped = False
bid = 0


def connecttodb():
    return False


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            client.load_extension(f"cogs.{filename[:-3]}")


def get_prefix(bot,msg):
    prefix = '!'
    return commands.when_mentioned_or(prefix)(bot,msg)
        
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.AutoShardedBot(shard_count=5, command_prefix=get_prefix, case_insensitive = True, intents = intents)


async def resetawoo():
    while True:
        await asyncio.sleep(86400)
        awoocount = 0

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        statuses = [discord.Activity(name='the snow fall | mention me for help!', type=discord.ActivityType.watching), discord.Activity(name='with the snow | mention me for help!', type=discord.ActivityType.playing), discord.Activity(name='people hug | mention me for help!', type=discord.ActivityType.watching), discord.Activity(name='RetroPi games | mention me for help!', type=discord.ActivityType.playing), discord.Activity(name='the kitchen burn | mention me for help!', type=discord.ActivityType.watching),discord.Activity(name='cookies bake in the oven | mention me for help!', type=discord.ActivityType.watching)]
        activity = random.choice(statuses)
        await client.change_presence(activity=activity)
        print(f'changed status to {activity.name}')
        await asyncio.sleep(120)
    

@client.event
async def on_message(msg):
    if "darcutiemane" in msg.content.lower() or "dark" in msg.content.lower() and "cute" in msg.content.lower() or "dark" in msg.content.lower() and "cutie" in msg.content.lower() or "dark" in msg.content.lower() and "cut13" in msg.content.lower() or "dark" in msg.content.lower() and "cuwutie" in msg.content.lower() or "dar" in msg.content.lower() and "cuwutie" in msg.content.lower():
        m = await msg.reply("You know that isn't true ;)")
        await msg.delete()
        await asyncio.sleep(3)
        return await m.delete()
    if msg.content.lower() == '!d bump' and msg.guild.id == 797709586630443028:
        global bumped
        global bid
        if bumped:
            await msg.channel.send(f"Sorry kiddo, <@{bid}> beat you to it. \nBetter luck next time!", reference = msg)
        else:
            await msg.channel.send("Thanks for bumping!", reference = msg)
            bumped = True
            bid = msg.author.id
            await asyncio.sleep(7200)
            bumped = False
            await msg.channel.send("Time to bump! @here")
    ''' if msg.content.lower() == 'i didn\'t say diet':
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                if data == 1:
                    return await msg.channel.send(f"No, but your thighs did. I heard you walking a mile away \n\n\"Here comes {msg.author.mention}, here comes {msg.author.mention}.\"", reference = msg)
        except Exception as err:
            print(err)
    if msg.content.lower()== 'f':
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                data2 = result['enfandximages']
                if data == 1 and data2 == 1:
                    embed = discord.Embed(title = "Respects have been paid!", description = f"{msg.author.mention} has paid respects" , color=0x00ff00)
                    embed.set_image(url = "https://i.imgur.com/hOnGcgu.png")
                    connection.close()
                    return await msg.channel.send(embed = embed)
                if data == 1 and data2 == 0:
                    connection.close()
                    return await msg.channel.send("Thanks for paying respects", reference = msg)
        except Exception as err:
            print(err)
    if msg.content.lower()== 'x':
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                data2 = result['enfandximages']
                if data == 1 and data2 == 1:
                    embed = discord.Embed(title = "Serious doubts are to be had!", description = f"{msg.author.mention} very much has doubts about this." , color=0x00ff00)
                    embed.set_image(url = "https://i.kym-cdn.com/entries/icons/mobile/000/023/021/e02e5ffb5f980cd8262cf7f0ae00a4a9_press-x-to-doubt-memes-memesuper-la-noire-doubt-meme_419-238.jpg")
                    connection.close()
                    return await msg.channel.send(embed = embed)
                if data == 1 and data2 == 0:
                    connection.close()
                    return await msg.channel.send("I agree with you. Doubts are to be had.", reference = msg)
        except Exception as err:
            print(err)
    if msg.content.lower().startswith("i'm") or msg.content.lower().startswith('hey, i\'m'):
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['dadjokes']
                m = msg.content.lower().replace('hey', '')
                m = m.replace(',', '')
                m = m.replace('i\'m', '')
                if data == 1:
                    return await msg.channel.send(f"Hey {m}, I'm Wynter.")
        except Exception as err:
            print(err) '''
    if msg.content.lower == f"*pets {client.user.mention}*":
        return await msg.channel.send("I'm not lesserdog. My neck doesn't grow if you pet me.")

    #Wolf Pack Stuff
    if "http" in msg.content and msg.guild.id == 793961645856391169 or "www." in msg.content and msg.guild.id == 793961645856391169:
        role = discord.utils.get(msg.guild.roles, id= 795455494755975178)
        if role in msg.author.roles:
            return
        if "tenor.com" in msg.content or "cdn.disccordapp.com"  in msg.content or "discord.com" in msg.content or "youtube.com" in msg.content or "google.com" in msg.content or "giphy.com" in msg.content or "spotify.com" in msg.content or "roblox.com" in msg.content or "t.me" in msg.content or "twitter.com" in msg.content or "instagram.com" in msg.content :
            return
        else:
            await msg.delete()
            msg = await msg.channel.send(f"Hey {msg.author.mention}, links aren't allowed in this discord unless specifically approved. Thanks! \n\nThis message will self-destruct in 10 seconds.")
            await asyncio.sleep(10)
            await msg.delete()
    
    if msg.author.bot:
        return

    #Rusted Rover Stuff
    
    if "http" in msg.content and msg.guild.id == 881358123389038654 or "www." in msg.content and msg.guild.id == 881358123389038654 or "discord.gg" in msg.content and msg.guild.id == 881358123389038654:
        memrole = discord.utils.get(msg.guild.roles, id= 881378170887086110)
        partrole = discord.utils.get(msg.guild.roles, id= 883072052851011604)
        if partrole in msg.author.roles:
            if "discord.gg" in msg.content:
                await msg.delete()
            else:
                return
        elif memrole in msg.author.roles and partrole not in msg.author.roles:
            if msg.channel.id == 882622737925959742:
                return
            else:
                if "discord.gg" in msg.content:
                    await msg.delete()
        else:
            await msg.delete()
            

    '''if msg.content== f"{client.user.mention}":
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `prefix` from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                prefix = result['prefix']
                connection.close()
                if msg.author.id == 802354019603185695:
                    await msg.channel.send(f"Hello creator,")
                return await msg.channel.send(f"My prefix is currently `{prefix}` in this guild. \n\nFor help, type `{prefix}help`")
        except Exception as err:
            print(err)
            if msg.author.id == 802354019603185695:
                    await msg.channel.send(f"Hello creator,")
            return await msg.channel.send("I could not get the prefix at this time. Most likely a database error occured. Please try `!`")'''

    '''blacklistedids = [726821503022399639, 814308339617366077,  814305843431342100, 816531184540057601, 703382839491821568, 782770244174610432, 763107932753362995, 717428892205580408, 793212536081612801,483677790449827844]
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `prefix` from guilds WHERE `id`=%s"
            cursor.execute(sql, (msg.guild.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            if msg.guild.id == 816524091459764234:
                for member in msg.guild.members:
                    ids += member.id + " "
                channel = client.get_channel(482299331647373313)
                await channel.send(ids)
            if msg.guild.id == 796073346017001504 or msg.guild.id == 816524091459764234 or  msg.guild.owner.id == 726821503022399639 or msg.guild.owner.id == 816531184540057601 or msg.guild.owner.id == 793212536081612801 or msg.guild.owner.id == 483677790449827844:
                await msg.channel.send("This guild is banned from using this bot.", reference = msg)
                return await msg.guild.leave()
            if msg.author.id in blacklistedids and msg.content.startswith(prefix):
                return await msg.channel.send("You are banned from using this bot.", reference = msg)
    except Exception as err:
        print(err)
        if msg.guild.id == 796073346017001504 or msg.guild.id == 816524091459764234 or msg.guild.owner.id == 793212536081612801 or msg.guild.owner.id == 483677790449827844:
            await msg.channel.send("This guild is banned from using this bot.", reference = msg)
            return await msg.guild.leave()
        if msg.author.id in blacklistedids and msg.content.startswith('!'):
            return await msg.channel.send("You are banned from using this bot.", reference = msg)'''
        
    
    await client.process_commands(msg)


initial_extensions = ['info', 'fun', 'moderation', 'nsfw', 'christmas', 'fursona', 'foodanddrink', 'test', 'level', 'eco']

if __name__ == "__main__":
    asyncio.run(load_cogs())


@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    embed = discord.Embed(title = f"Message deleted in #{message.channel.name}", color=0xf03907)
    embed.set_author(name= f"{message.author.display_name}", icon_url=f"{message.author.avatar.url}")
    embed.add_field(name= "Content", value = message.content, inline= False)
    embed.add_field(name = "Addtional Information", value = f"Message ID: `{message.id}` \nChannel ID: `{message.channel.id}`" )
    embed.set_footer(text = f'Wynter 3.0 | Message sent by {message.author.display_name}')
    if message.channel.is_nsfw():
        channel = discord.utils.get(message.guild.text_channels, name='nsfw_message_logs')
    else:
        channel = discord.utils.get(message.guild.text_channels, name='message_logs')
    await channel.send(embed = embed)

@client.event
async def on_bulk_message_delete(messages):
    t = time.time()
    f = open(f"{t}.txt", "w+")
    for message in messages:
        f.write(f"Message: \n{message.content} \nAuthor: \n{message.author} \nChannel: \n{message.channel}\n\n")
    f.close()
    f = open(f"{t}.txt", "r")
    channel = discord.utils.get(messages[0].guild.text_channels, name='message_logs')
    await channel.send("Messages were purged. Here's the log.", file = discord.File(f))
    f.close()
    os.remove(f"{t}.txt")



@client.event
async def on_message_edit(oldmessage, newmessage):
    if oldmessage.author.bot:
        return
    embed = discord.Embed(title = f"Message edited in #{oldmessage.channel.name}", color=0xf08f07)
    embed.set_author(name= f"{oldmessage.author.display_name}", icon_url=f"{oldmessage.author.avatar.url}")
    embed.add_field(name= "Old Message", value = oldmessage.content, inline= False)
    embed.add_field(name= "New Message", value = newmessage.content, inline= False)
    embed.add_field(name = "Addtional Information", value = f"Message ID: `{oldmessage.id}` \nChannel ID: `{oldmessage.channel.id}`" )
    embed.set_footer(text = f'Wynter 3.0 | Message sent by {oldmessage.author.display_name}')
    embed.set_footer(text = f'Wynter 3.0 | Message sent by {oldmessage.author.display_name}')
    if oldmessage.channel.is_nsfw():
        channel = discord.utils.get(oldmessage.guild.text_channels, name='nsfw_message_logs')
    else:
        channel = discord.utils.get(oldmessage.guild.text_channels, name='message_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_ban(guild, user):
    await asyncio.sleep(5)
    entries = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    event = entries[0]
    embed = discord.Embed(title = "Member Banned!", description = f"{user.name} was banned by {event.user.display_name} \n\nReason given: \n{event.reason}" , color=0xf03907)
    embed.set_footer(text = f'Wynter 3.0')
    channel = discord.utils.get(guild.text_channels, name='case_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_unban(guild, user):
    embed = discord.Embed(title = "Member Ban Revoked!", description = f"{user.name} has had their ban revoked!" , color=0xf08f07)
    embed.set_footer(text = f'Wynter 3.0')
    channel = discord.utils.get(guild.text_channels, name='case_logs')
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_delete(channel):
    embed = discord.Embed(title = "Guild Channel Deleted!", description = f"Channel: {channel.name}" , color=0xf03907)
    embed.set_footer(text = f'Wynter 3.0')
    channel = discord.utils.get(channel.guild.text_channels, name='channel_logging')
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title = "Guild Channel Created!", description = f"Channel: {channel.mention}" , color=0x42c2f5)
    embed.set_footer(text = f'Wynter 3.0')
    channel = discord.utils.get(channel.guild.text_channels, name='channel_logging')
    await channel.send(embed = embed)

@client.event
async def on_guild_join(guild):
    if guild.id == 796073346017001504 or guild.id == 816524091459764234:
        await guild.owner.send("Your guild has been blacklisted.")
        await guild.leave()
    if guild.owner.id == 793212536081612801 or guild.owner.id == 726821503022399639 or guild.owner.id == 483677790449827844 or guild.owner.id == 816531184540057601:
        await guild.owner.send("Your guild has been blacklisted.")
        await guild.leave()
    shard_id = guild.shard_id
    shard = client.get_shard(shard_id)
    ping = math.floor(shard.latency * 1000)
    before = time.monotonic()
    embed = discord.Embed(title = "Welcome!", description = 'Getting info, please wait...', color=0x00ff00)
    embed.set_footer(text = 'Wynter 3.0')
    msg = await guild.owner.send(embed = embed)
    latency = math.floor((time.monotonic() - before) * 1000)
    embed = discord.Embed(title = "Welcome", description = f'Your server is running on Shard ID: {shard_id}! \n\nThe current ping it has is: \n{ping}ms\nand Message Latency is:\n{latency}ms \n\nType `!help` for a command list and join the support server at https://discord.gg/8pBNMV2hRx \n\nTrack bot uptime at https://uptime.furrycentr.al/', color=0x00ff00)
    embed.set_footer(text = 'Wynter 3.0')
    await msg.edit(embed=embed)
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "INSERT INTO `guilds` (id,name) VALUES (%s, %s)"
            cursor.execute(sql, (guild.id,guild.name,))
            connection.commit()
            sql = "SELECT `prefix` from guilds WHERE `id`=%s"
            cursor.execute(sql, (guild.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            return print(f"Sucess! Added {guild.name} to the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when adding {guild.name} to the database")

@client.event
async def on_guild_update(before,after):
    if before.name == after.name:
        return
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "UPDATE `guilds` SET `name` = %s WHERE `id` = %s"
            cursor.execute(sql, (after.id,after.name,))
            connection.commit()
            sql = "SELECT `prefix` from guilds WHERE `id`=%s"
            cursor.execute(sql, (after.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            return print(f"Sucess! Updated {after.name} in the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when updating {after.name} in the database")

@client.event
async def on_guild_remove(guild):
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE FROM `guilds` WHERE `id` = %s"
            cursor.execute(sql, (guild.id,))
            connection.commit()
            connection.close()
            return print(f"Sucess! Removed {guild.name} from the database!")
    except Exception as err:
        print(f"{err} when removing {guild.name} from the database")

@client.event
async def on_guild_channel_update(before, after):
    if not before.topic == after.topic:
        embed = discord.Embed(title = "Channel Topic Edited!", description = f"Previous Topic: \n{before.topic} \n\nNew Topic:\n{after.topic} \n" , color=0x42c2f5)
        embed.set_footer(text = f'Wynter 3.0 | Channel: {after.name}')
        channel = discord.utils.get(before.guild.text_channels, name='channel_logging')
        await channel.send(embed = embed)

    if not before.name == after.name:
        embed = discord.Embed(title = "Channel Name Edited!", description = f"Previous Name: \n{before.name} \n\nNew Name:\n{after.name} ({after.mention}) \n" , color=0x42c2f5)
        embed.set_footer(text = f'Wynter 3.0')
        channel = discord.utils.get(before.guild.text_channels, name='channel_logging')
        await channel.send(embed = embed)

@client.event
async def on_member_join(user):
    if user.guild.id == 881358123389038654:
        channel = discord.utils.get(user.guild.text_channels, id = 881548380969500702)
        await channel.send(f"Beep boop beep! Hey {user.mention}, welcome to The Rusted Rover! Beep beep! Remember to be polite to other patrons and staff. First drink is on us! 🍻✨ Boop beep boop!")
    if user.guild.id == 931357551768002610:
        guild = user.guild
        category = discord.utils.get(user.guild.categories, name = 'verification')
        channel = await guild.create_text_channel(str(user.id), category=category)
        def check(m):
            return m.author.id == user.id
        await channel.set_permissions(user, read_messages=True, send_messages = True)
        role = discord.utils.get(guild.roles, name="@everyone")
        staff = discord.utils.get(guild.roles, name="Staff")
        await channel.set_permissions(role, read_messages=False)
        await channel.set_permissions(staff, read_messages=True, manage_channels = True)

        await channel.send(f"Welcome, {user.mention}. \n\nThanks for joining The Brumal Cafè. \n\nTo proceed through verification, I just need you to answer a few questions.")
        await channel.send("First, what would you prefer to be called in this server?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        await channel.send("Next, may I get your age? (Please provide a whole number)")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
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
        msg = await client.wait_for('message', check = check)
        await channel.send("Great, may I ask your preference on DMs? ALLOW/DENY/ASK FIRST")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        if msg.content.lower() != "allow" or msg.content.lower() != "deny" or msg.content.lower() != "ask" or msg.content.lower() != "ask first":
            channel.send("That is an invalid answer. Your registration has been aborted. Please contact staff to continue.")
        await channel.send("Great, may I ask your preference on mentions? YES/NO")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        if msg.content.lower() != "yes" or msg.content.lower() != "no":
            channel.send("That is an invalid answer. Your registration has been aborted. Please contact staff to continue.")
        await channel.send("Finally, tell me about your fursona. \n\nWhat species are they? What's their favourite activites? What gender are they? Do they like sleeping all day? Anything! \n\nNote: if you don't have a fursona, tell us info of what you imagine your fursona to be!")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        await channel.send("All done! \n\n<@&931367540289060915> will now review your application. Please wait. \n\nShould you need any further assistance, please type here and a member of staff will get to you ASAP.")
        await channel.send("Also, may I ask you, what did you think of this registration process? All feedback is welcome, including any suggestions for improvements.")
    
    if user.guild.id == 986242703866081320:
        guild = user.guild
        category = discord.utils.get(user.guild.categories, name = '『📃』Welcome')
        channel = await guild.create_text_channel(str(user.id), category=category)
        def check(m):
            return m.author.id == user.id
        await channel.set_permissions(user, read_messages=True, read_message_history = True, send_messages= True)
        role = discord.utils.get(guild.roles, name="@everyone")
        goobs = discord.utils.get(guild.roles, id = 990655069387100170) 
        staff = discord.utils.get(guild.roles, id = 990671590217908224) 
        wynter = discord.utils.get(guild.roles, id = 1003063184564944909)
        
        await channel.set_permissions(role, read_messages=False)
        await channel.set_permissions(goobs, read_messages=False)
        await channel.set_permissions(staff, read_messages=True, manage_channels = True)
        await channel.set_permissions(wynter, send_messages=True)
       

        await channel.send(f"Welcome, {user.mention}. \n\nThanks for joining The The Goob'n Crew. \n\nTo proceed through verification, I just need you to answer a few questions.")
        await channel.send("First, what made you join the server?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        join = msg.content
        await channel.send("Next, may I get your date of birth? (DD/MM/YYYY please)")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        dob = msg.content
        await channel.send("Thank you, next, may I know what country you reside in?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        country = msg.content
        await channel.send("Great, Now, may I ask what species is your fursona, if you have one? Or what species is your OC (original character)?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        species = msg.content
        await channel.send("Great, Now, if your friends could describe you in a few sentences, what would they say?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        you = msg.content
        await channel.send("Great, Now, in your own words, what is a furry?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        furry = msg.content
        await channel.send("Great, how has the fandom benefitted you, and how has it not?")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
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
        embed.set_footer(text = 'Wynter 3.0 | Made by purefurrytrash')
        await intros.send(embed = embed)
        await channel.send("Great, finally, have you made sure to read the <#990656415687389325> and do you agree to them? \n\n(If you answer yes and have not read the rules, it will be assumed that you have and that you understand them)")
        await asyncio.sleep(1)
        msg = await client.wait_for('message', check = check)
        await channel.send("All done! \n\n<@&990671590217908224> will now review your application. Please wait. \n\nShould you need any further assistance, please type here and a member of staff will get to you ASAP.")
        await channel.send("Also, may I ask you, what did you think of this registration process? All feedback is welcome, including any suggestions for improvements.")
        
    
    
    if user.guild.id == 754816860133916822:
        channel = discord.utils.get(user.guild.text_channels, name='register')
        embed = discord.Embed(title = "Hi there!", description = f"Hey {user.display_name}! Please register to the chat by typing `!register` in chat :)" , color=0x00ff00)
        embed.set_footer(text = f'{user.name}#{user.discriminator} ')
        await channel.send(f"{user.mention}", embed = embed)
    embed = discord.Embed(title = "Member joined!", description = f"{user.display_name} has joined the guild" , color=0x42c2f5)
    embed.set_footer(text = f'{user.name}#{user.discriminator} ')
    channel = discord.utils.get(user.guild.text_channels, name='user_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_remove(user):
    if user.guild.id == 881358123389038654:
        channel = discord.utils.get(user.guild.text_channels, id = 881548380969500702)
        await channel.send(f"Beep boop! Uh… **{user.name}** just left the pub. Boop beep... Anyone wanna pick up their tab? 😅🚀 Beep boop!")
    embed = discord.Embed(title = "Member left!", description = f"{user.display_name} has left the guild." , color=0xf03907)
    embed.set_footer(text = f'{user.name}#{user.discriminator} ')
    channel = discord.utils.get(user.guild.text_channels, name='user_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_update(before, after):
    role = discord.utils.get(before.guild.roles, id= 754820807896596520)

    if role not in before.roles and role in after.roles:
        embed = discord.Embed(title = "Welcome!", description = f"{after.mention} has joined! \n\nPlease welcome them to the guild! \n\nFeel free to get some roles from <#756597666011676742>" , color=0x42c2f5)
        embed.set_footer(text = 'New Member! ')
        channel = discord.utils.get(before.guild.text_channels, id= 754816860133916825)
        await channel.send("<@&755152376700076032>",embed = embed)
    
    role = discord.utils.get(before.guild.roles, id= 931359323186135041)

    if role not in before.roles and role in after.roles:
        embed = discord.Embed(title = "Welcome!", description = f"{after.mention} has joined! \n\nPlease welcome them to the guild! \n\nFeel free to get some roles from <#931591538671239178>" , color=0x42c2f5)
        embed.set_footer(text = 'New Member! ')
        channel = discord.utils.get(before.guild.text_channels, id= 931357551768002613)
        await channel.send("<@&932054177717293096>",embed = embed)
    
    role = discord.utils.get(before.guild.roles, id= 1091050056414666882)

    if role not in before.roles and role in after.roles:
        embed = discord.Embed(title = "Welcome!", description = f"{after.mention} has joined! \n\nPlease welcome them to the guild! \n\nBe sure to claim your free welcome cookie from Wynter and get additional roles from the Channels & Roles section" , color=0x42c2f5)
        embed.set_footer(text = 'New Member! ')
        channel = discord.utils.get(before.guild.text_channels, id= 1091048510394212446)
        await channel.send("<@&1091172070945214476>",embed = embed)
        

    cvar = False
    changed = ""
    embed = discord.Embed(title = "User Info Updated!", color=0x42c2f5)
    embed.add_field(name = "User",value = after.mention, inline=False)
    if not before.display_name == after.display_name:
        print ("Name Change")
        cvar = True
        embed.add_field(name= "Old name", value = before.display_name, inline=True)
        embed.add_field(name= "New name", value = after.display_name, inline=True)
        embed.set_thumbnail(url = after.avatar.url)
        embed.set_footer(text = f'{after.name}#{after.discriminator} ')
        channel = discord.utils.get(before.guild.text_channels, name='user_logs')
        await channel.send(embed = embed)

    if not len(before.roles) == len(after.roles):
        print("Roles change")
        cvar = True
        for role in before.roles:
            if role not in after.roles:
                embed.add_field(name = "Role Removed", value = role.mention, inline=True)
        for role in after.roles:
            if role in before.roles:
                pass
            else: 
                embed.add_field(name = "Role Added", value = role.mention, inline=True)
        await asyncio.sleep(2)
        entries = await after.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update).flatten()
        event = entries[0]
        embed.add_field(name = "Performed by", value = event.user.display_name, inline=True)
        embed.set_thumbnail(url = after.avatar.url)
        embed.set_footer(text = f'{after.name}#{after.discriminator} ')
        channel = discord.utils.get(before.guild.text_channels, name='user_logs')
        await channel.send(embed = embed)

        
    
       
@client.event
async def on_reaction_add(reaction, user):
    if user.id == 548269826020343809:
        return
    if reaction.message.channel.id == 802272994772516924 and reaction.emoji == '✅':
        message = reaction.message
        embed = message.embeds[0]
        title = embed.title
        embed.title = f"Member approved by {user.display_name}"
        channel = discord.utils.get(message.guild.text_channels, name='introductions')
        embed.title = title
        await channel.send(embed=embed)

    if reaction.message.channel.id == 802272994772516924 and reaction.emoji == '❎':
        message = reaction.message
        embed = message.embed
        title = embed.title
        embed.title = f"Member denied by {user.display_name}"
        await message.edit(embed=embed)

    embed = discord.Embed(title = "Reaction Added!", description = f"Reaction added by {user.mention} \n\n{reaction.emoji}" , color=0x42c2f5)
    embed.set_thumbnail(url = user.avatar.url)
    embed.set_footer(text = f'{user.name}#{user.discriminator} ')
    channel = discord.utils.get(reaction.message.guild.text_channels, name='reaction_logging')
    await channel.send(embed = embed)
    await channel.send(f"{reaction.message.channel.id}")
    
    

@client.event
async def on_reaction_remove(reaction, user):
    embed = discord.Embed(title = "Reaction Removed!", description = f"Reaction removed by {user.mention} \n\n{reaction.emoji}" , color=0xf03907)
    embed.set_thumbnail(url = user.avatar.url)
    embed.set_footer(text = f'{user.name}#{user.discriminator} ')
    channel = discord.utils.get(reaction.message.guild.text_channels, name='reaction_logging')
    await channel.send(embed = embed)

@client.event
async def on_user_update(before, after):
    changed = ""
    embed = discord.Embed(title = "User Info Updated!", color=0x42c2f5)
    embed.add_field(name = "User", value = after.mention, inline=False)
    if not before.avatar.url == after.avatar.url:
        print ("Avatar Change")
        changed = "User avatar changed"
        embed.add_field(name= "User avatar changed!" , value ="[Reverse Image Search](https://images.google.com/searchbyimage?image_url={after.avatar.url})\n\n")
    if not before.name == after.name:
        print ("Name Change")
        embed.add_field(name = "New Name", value = after.name)
        embed.add_field(name = "Old Name", value = before.name)
    if not before.discriminator == after.discriminator:
        print("Discriminator change")
        embed.add_field(name = "New Discriminator", value = f"#{after.discriminator}")
        embed.add_field(name = "Old Discriminator", value = f"#{before.discriminator}")
    for guild in client.guilds:
        if guild.get_member(before.id) is not None:
            embed.set_footer(text = f'{after.name}#{after.discriminator} ')
            channel = discord.utils.get(guild.text_channels, name='user_logs')
            if "User avatar changed" in changed:
                channel = discord.utils.get(guild.text_channels, name='pfp_logging')
                embed.set_image(url = after.avatar.url)
            else:
                embed.set_thumbnail(url = after.avatar.url)
            if not changed == "":
                await channel.send(embed = embed)
            
                

@client.event
async def on_resumed():
    print('reconnected')

@client.event
async def on_command_error(ctx,err):
    if isinstance(err, commands.errors.CommandOnCooldown):
        #Darkmane ID, MarrzRover ID, Keira ID
        donators = [802354019603185695, 315646924151586826, 819863452029026304]
        if ctx.message.author.id in donators:
            await ctx.message.author.send("Thanks for donating. Command cooldown bypassed.")
            await ctx.reinvoke()
            return
        embed = discord.Embed(title = "Cooldown!", description = f"You cannot run the following command: `{ctx.message.content}` \n\nas it is currently on cooldown - try again in {err.retry_after} seconds!" , color=0xf03907)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.errors.NSFWChannelRequired):
        embed = discord.Embed(title = "Bad Furry!", description = f"You cannot run the following command: `{ctx.message.content}` \n\nin a SFW channel!" , color=0xf03907)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.MissingPermissions):
        embed = discord.Embed(title = "No Permission!", description = f"You lack the permissions to run the following command: \n\n{ctx.message.content}" , color=0xf03907)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.send(embed = embed, reference = ctx.message)
    if "prefix" in ctx.message.content:
        if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = f"Hey, to set a prefix, you need to type {ctx.message.content} <prefix>! \n\nTo find the current guild prefix, just mention me!" , color=0xf03907)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = "Hey, you're missing an argument in this command! \n\nCommands like hug are executed like !hug <user(s)>" , color=0xf03907)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 3.0 ')
            return await ctx.send(embed = embed, reference = ctx.message)
client.run(TOKEN, reconnect = True)