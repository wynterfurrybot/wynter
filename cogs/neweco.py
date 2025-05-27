import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import asyncio
import random 
from dotenv import load_dotenv
import pymysql.cursors
import os
import json
import time

load_dotenv()
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')

def format_time(seconds: float, format_code: str = 'R') -> str:
    """
    Converts seconds into a Discord timestamp.
    
    Parameters:
        seconds (float): The number of seconds until the event.
        format_code (str): Discord format code, e.g. 'R' for relative.
    
    Returns:
        str: Formatted Discord timestamp string.
    """
    unlock_timestamp = int(time.time() + seconds)
    return f"<t:{unlock_timestamp}:{format_code}>"

def connecttodb():
    # Connect to the database
    connection = pymysql.connect(host=DBHOST,
                                user=DBUSER,
                                password=DBPW,
                                db=DB,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wagesdocked = {}
        self.userwanted = {}
    
    @discord.slash_command(aliases=['bal'])
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        server_id = str(ctx.guild.id) # Get the server ID
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, server_id, 10000))
                connection.commit()
                print(f"Success! Added an eco account for {user_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred adding an eco account for {user_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT money, server_currency FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (user_id, server_id))
                result = cursor.fetchone()
                print(f"[DEBUG] Fetched result for user {user_id} in server {server_id}: {result}")  # <-- Log here
                if result:
                    money = result['money']
                    currency = result['server_currency']
                    await ctx.respond(f"Your current balance is {money} {currency}")
                else:
                    await ctx.respond("Your economy data could not be retrieved. Please try again.")
                connection.close()
        except Exception as err:
            print(err)

    @discord.slash_command()
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def bribe(self, ctx):
        user = ctx.author
        user_id = ctx.author.id
        server_id = ctx.author.guild.id
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT in_jail, wages_docked, server_currency, money FROM eco WHERE user_id = %s AND server_id = %s"
                cursor.execute(sql, (user_id, server_id))
                result = cursor.fetchone()
                if result:
                    jail = result['in_jail']
                    currency = result['server_currency']
                    money = result['money']
                    if jail:
                        money = money / 2
                        sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id = %s"
                        cursor.execute(sql, (money, user_id, server_id))
                        connection.commit()
                        if random.randint(1,5) == 1:
                            sql = "UPDATE eco SET in_jail = 0 WHERE user_id=%s AND server_id = %s"
                            cursor.execute(sql, (user_id, server_id))
                            connection.commit()
                            connection.close()
                            return await ctx.respond(f"{user.mention} You succesfully bribed the police, they will now look the other way.", ephemeral=True)
                        else:
                            connection.close()
                            return await ctx.respond(f"{user.mention} You were unsuccessful in bribing the police, and they pocketed your bribe,", ephemeral=True)
                    else:
                        return await ctx.respond(f"{user.mention} You are not on the run from the police, therefore, there is no need to bribe them.", ephemeral=True)
                    
                connection.close()
        except Exception as err:
            print(err)

    
    @discord.slash_command()
    @commands.cooldown(1,3600, commands.BucketType.user)
    async def work(self, ctx):
        channel = ctx.channel
        user = ctx.author
        user_id = str(ctx.author.id)
        server_id = str(ctx.guild.id) # Get the server ID
        mon = 0
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT in_jail, wages_docked FROM eco WHERE user_id = %s AND server_id = %s"
                cursor.execute(sql, (user_id, server_id))
                result = cursor.fetchone()
                docked = result['wages_docked'] if result else False
                if docked:
                    ran = [5, 10, 12]
                else: 
                    ran = [17, 25, 30, 60, 80, 120, 150]
                mon = random.choice(ran)
                connection.close()
        except Exception as err:
            print(err)

        await ctx.respond("You went to work, check back in an hour...")
        await asyncio.sleep(3600)

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, server_id, 10000))
                connection.commit()
                print(f"Success! Added an eco account for {user_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred adding an eco account for {user_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT in_jail, wages_docked, server_currency, money FROM eco WHERE user_id = %s AND server_id = %s"
                cursor.execute(sql, (user_id, server_id))
                result = cursor.fetchone()
                if result:
                    jail = result['in_jail']
                    docked = result['wages_docked']
                    currency = result['server_currency']
                    money = result['money']
                    if jail:
                        if money < mon:
                            connection.close()
                            return await channel.send(f"{user.mention} Well, well, well. Going to work broke and whilst on the run from the police. \n\nDon't expect your employer to pay you this time.")
                        sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id = %s"
                        cursor.execute(sql, (mon, user_id, server_id))
                        connection.commit()
                        connection.close()
                        return await channel.send(f"{user.mention} You are currently on the run from the police, as a result, your pay has gone to help pay bail! \n\nYou have lost {mon} {currency}")
                    
                    sql = "UPDATE eco SET money = money + %s WHERE user_id=%s AND server_id = %s"
                    cursor.execute(sql, (mon, user_id, server_id))
                    connection.commit()
                    sql = "SELECT money, server_currency FROM eco WHERE user_id=%s AND server_id = %s"
                    cursor.execute(sql, (user_id, server_id))
                    result = cursor.fetchone()
                    if result:
                        money = result['money']
                        if docked:
                            await channel.send(f"{user.mention} You went to work and made {mon} {currency}, your current balance is {money} {currency} \n\n-# Your wages were docked this session.")
                        else:
                            await channel.send(f"{user.mention} You went to work and made {mon} {currency}, your current balance is {money} {currency}")
                connection.close()
        except Exception as err:
            print(err)
    
    @discord.slash_command(aliases=['transfer'])
    async def pay(self, ctx, user: discord.User, amount: int):
        user_id = str(ctx.author.id)
        rep_id = str(user.id)
        server_id = str(ctx.guild.id) # Get the server ID

        if user_id == rep_id:
            message = f"Money you pay yourself doesn't make you any richer. \n\nPlus, it's disallowed."
            embed = discord.Embed(title="Look, I know you want to be rich, but..", description=message)
            return await ctx.respond(embed = embed, ephemeral=True)

        if amount <= 0:
            return await ctx.respond("You can only pay positive amounts.", ephemeral=True)

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, server_id, 10000))
                cursor.execute(sql, (rep_id, server_id, 10000))
                connection.commit()
                print(f"Success! Ensured eco accounts exist for {user_id} and {rep_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred ensuring eco accounts for {user_id} and {rep_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT money FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (user_id, server_id))
                sender_result = cursor.fetchone()
                
                if not sender_result or sender_result['money'] < amount:
                    connection.close()
                    return await ctx.respond("You do not have enough money to do this action.", ephemeral=True)
                
                sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (amount, user_id, server_id))
                sql = "UPDATE eco SET money = money + %s WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (amount, rep_id, server_id))
                connection.commit()
                
                sql = "SELECT money, server_currency from eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (rep_id, server_id))
                receiver_result = cursor.fetchone()
                
                if receiver_result:
                    currency = receiver_result['server_currency']
                    await ctx.respond(f"Success, gave {amount} {currency} to {user.mention} -- they now have {receiver_result['money']} {currency}.")
                connection.close()
        except Exception as err:
            print(err)
                
    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def give(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        server_id = str(ctx.guild.id) # Get the server ID

        if amount <= 0:
            return await ctx.respond("You can only give positive amounts.", ephemeral=True)

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (recipient_id, server_id, 10000))
                connection.commit()
                print(f"Success! Ensured eco account exists for {recipient_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred ensuring eco account for {recipient_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "UPDATE eco SET money = money + %s WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (amount, recipient_id, server_id))
                connection.commit()
                sql = "SELECT money, server_currency FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (recipient_id, server_id))
                result = cursor.fetchone()
                if result:
                    money = result['money']
                    currency = result['server_currency']
                    await ctx.respond(f"Gave {amount} {currency} to {user.mention} - their current balance is {money} {currency}")
                connection.close()
        except Exception as err:
            print(err)

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def take(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        server_id = str(ctx.guild.id) # Get the server ID

        if amount <= 0:
            return await ctx.respond("You can only take positive amounts.", ephemeral=True)

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (recipient_id, server_id, 10000))
                connection.commit()
                print(f"Success! Ensured eco account exists for {recipient_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred ensuring eco account for {recipient_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (amount, recipient_id, server_id))
                connection.commit()
                sql = "SELECT money, server_currency FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (recipient_id, server_id))
                result = cursor.fetchone()
                if result:
                    money = result['money']
                    currency = result['server_currency']
                    await ctx.respond(f"Took {amount} {currency} from {user.mention} - their current balance is {money} {currency}")
                connection.close()
        except Exception as err:
            print(err)
    
    @discord.slash_command()
    @commands.cooldown(1,3600, commands.BucketType.user)
    async def steal(self, ctx, user: discord.User):
        user_id = str(ctx.author.id)
        recipient_id = str(user.id)
        server_id = str(ctx.guild.id) # Get the server ID

        if user.id == ctx.author.id:
            message = f"You cannot steal from yourself, no matter how hard you try. \n\nOh, and now you can't steal again for another hour."
            embed = discord.Embed(title="Well that was a waste..", description=message)
            return await ctx.respond(embed=embed, ephemeral=True)
        
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT in_jail, money FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (user_id, server_id))
                result = cursor.fetchone()
                jail = result['in_jail'] if result else False
                money = result['money'] if result else False
                if jail:
                    if money < 100:
                        connection.close()
                        return await ctx.respond(f"An onlooker noticed you have a warrant out for your arrest and handed you in to the police. \n\nAs you had no money to pay the bail, someone else paid for you this time.")
                    sql = "UPDATE eco SET money = money - 100 WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    return await ctx.respond(f"An onlooker noticed you have a warrant out for your arrest and handed you in to the police. \n\nThe police have demanded £100 as bail to let you go. \nYou have lost £100 in bail.")
                connection.close()
        except Exception as err:
            print(err)
           
        # Specific user checks
        if (user_id == "808620409963544578" and recipient_id in ["802354019603185695", "281486361947668481"]) or recipient_id == "548269826020343809":
            await ctx.respond(content = f"Stealing from your employer? \n\nYour pay will be docked for this.", ephemeral = True)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET wages_docked = 1 WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    connection.commit()
                    connection.close()
            except Exception as err:
                print(err)
            await asyncio.sleep(9000)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET wages_docked = 0 WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    connection.commit()
                    connection.close()
            except Exception as err:
                print(err)
            return # Exit after docking wages

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, server_id, 10000))
                cursor.execute(sql, (recipient_id, server_id, 10000))
                connection.commit()
                print(f"Success! Ensured eco accounts exist for {user_id} and {recipient_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred ensuring eco accounts for {user_id} and {recipient_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        p1money = 0
        p2money = 0
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "SELECT money FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (user_id, server_id))
                p1_result = cursor.fetchone()
                p1money = p1_result['money'] if p1_result else 0
                
                sql = "SELECT money FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (recipient_id, server_id))
                p2_result = cursor.fetchone()
                p2money = p2_result['money'] if p2_result else 0
                connection.close()
        except Exception as err:
            print(err)
        
        rich = random.randint(1, 3)
        if p2money >= 18000 and rich == 1:
            amount_stolen = random.randint(1, p2money // 2)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (amount_stolen, recipient_id, server_id))
                    sql = "UPDATE eco SET money = money + %s WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (amount_stolen, user_id, server_id))
                    connection.commit()
                    sql = "SELECT money, server_currency from eco WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    result = cursor.fetchone()
                    if result:
                        money = result['money']
                        currency = result['server_currency']
                        if p2money - amount_stolen <= 17999:
                            await ctx.respond(f"Stealing from the rich is always morally right. You gained {amount_stolen} {currency} from this player, making them no longer rich. \n\nThey won't know unless you reveal it", ephemeral=True)
                        else:
                            await ctx.respond(f"Stealing from the rich is always morally right. You gained {amount_stolen} {currency} from this player. \n\nThey won't know unless you reveal it.", ephemeral=True)
                    connection.close()
            except Exception as err:
                print(err)
        elif p2money >= 18000 and rich != 1:
            await ctx.respond("Whilst stealing from the rich is always morally right, you were caught this time. \n\nHowever, the police are on your side, just.. try again in an hour, okay?", ephemeral=True)

        elif random.randint(1, 10) == 1:
            if p2money <= 4:
                await ctx.respond("You can't steal from someone with so little money!")
                return

            amount_stolen = random.randint(1, p2money // 2)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (amount_stolen, recipient_id, server_id))
                    sql = "UPDATE eco SET money = money + %s WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (amount_stolen, user_id, server_id))
                    connection.commit()
                    sql = "SELECT money, server_currency from eco WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    result = cursor.fetchone()
                    if result:
                        money = result['money']
                        currency = result['server_currency']
                        await ctx.respond(f"Shh, you stole {amount_stolen} {currency} from {user.name} - They won't know unless you reveal it! \n\nYou now have {money} {currency}.", ephemeral=True)
                    connection.close()
            except Exception as err:
                print(err)
        else:
            if p1money <= 4:
                await ctx.respond(f"You failed to steal from {user.name} and are now on the run from the police!")
                try:
                    connection = connecttodb()
                    with connection.cursor() as cursor:
                        sql = "UPDATE eco SET in_jail = 1 WHERE user_id=%s AND server_id=%s"
                        cursor.execute(sql, (user_id, server_id))
                        connection.commit()
                        connection.close()
                except Exception as err:
                    print(err)
                await asyncio.sleep(9000)
                try:
                    connection = connecttodb()
                    with connection.cursor() as cursor:
                        sql = "UPDATE eco SET in_jail = 0 WHERE user_id=%s AND server_id=%s"
                        cursor.execute(sql, (user_id, server_id))
                        connection.commit()
                        connection.close()
                except Exception as err:
                    print(err)
                return
            await ctx.respond(f"You were caught trying to steal from {user.name} and are now on the run from the police, better stay low for the next few hours!")
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET in_jail = 1 WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    connection.commit()
                    connection.close()
            except Exception as err:
                print(err)
            print(f"{user.id} is now wanted")
            await asyncio.sleep(9000)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    sql = "UPDATE eco SET in_jail = 0 WHERE user_id=%s AND server_id=%s"
                    cursor.execute(sql, (user_id, server_id))
                    connection.commit()
                    connection.close()
            except Exception as err:
                print(err)
           
    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        server_id = str(ctx.guild.id) # Get the server ID

        if amount < 0:
            return await ctx.respond("You cannot set a negative amount.", ephemeral=True)

        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO eco (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (recipient_id, server_id, 10000))
                connection.commit()
                print(f"Success! Ensured eco account exists for {recipient_id} in server {server_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occurred ensuring eco account for {recipient_id} in server {server_id}")
        
        await asyncio.sleep(1) # Small delay to ensure data is committed
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                sql = "UPDATE eco SET money = %s WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (amount, recipient_id, server_id))
                connection.commit()
                sql = "SELECT money, server_currency FROM eco WHERE user_id=%s AND server_id=%s"
                cursor.execute(sql, (recipient_id, server_id))
                result = cursor.fetchone()
                if result:
                    money = result['money']
                    currency = result['server_currency']
                    await ctx.respond(f"Set {user.mention}'s balance to {amount} {currency} - they currently have {money} {currency}.")
                connection.close()
        except Exception as err:
            print(err)
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            command_name = ctx.command.name
            retry_after = format_time(error.retry_after)

            if command_name == "steal":
                message = f"You tried to steal again too soon! Try again {retry_after}.. or the cops might catch you!"
                embed = discord.Embed(title="Are you trying to get caught?!", description=message)
            elif command_name == "work":
                message = f"You're still at work, you get off shift {retry_after}."
                embed = discord.Embed(title="No! We can't give you a double shift, stop asking!", description=message)
            elif command_name == "bribe":
                user = ctx.author
                user_id = ctx.author.id
                server_id = ctx.author.guild.id
                try:
                    connection = connecttodb()
                    with connection.cursor() as cursor:
                        sql = "SELECT in_jail, wages_docked, server_currency, money FROM eco WHERE user_id = %s AND server_id = %s"
                        cursor.execute(sql, (user_id, server_id))
                        result = cursor.fetchone()
                        if result:
                            jail = result['in_jail']
                            money = result['money']
                            if jail:
                                money = money / 2
                                sql = "UPDATE eco SET money = money - %s WHERE user_id=%s AND server_id = %s"
                                cursor.execute(sql, (money, user_id, server_id))
                                connection.commit()
                                connection.close()
                                message = f"Brbing that often only loses you money, the police won't accept your bribe. Maybe you should try again {retry_after}."
                                embed = discord.Embed(title="The police liked that bribe..", description=message)
                                return await ctx.respond(embed = embed, ephemeral=True)
                            else:
                                message = f"You're not even wanted! You can use the command again {retry_after}."
                                embed = discord.Embed(title="Why are you trying to bribe?", description=message)
                                return await ctx.respond(embed = embed, ephemeral=True)
                            
                        connection.close()
                except Exception as err:
                        print(err)
            else:
                message = f"You're on cooldown! Try again in {retry_after}."
                embed = discord.Embed(title="Cooldown Active", description=message)
            
            await ctx.respond(embed=embed, ephemeral=True)

        else:
            raise error

def setup(bot):
    bot.add_cog(Economy(bot))