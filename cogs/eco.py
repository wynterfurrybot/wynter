import discord
from discord.ext import commands, bridge
from discord.ext.commands import cooldown, BucketType
import asyncio
import random 
from dotenv import load_dotenv
import pymysql.cursors
import os
import json

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

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(aliases=['bal'])
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(user_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {user_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {user_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(user_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
                await ctx.reply(f"Your current balance is {money} peanuts")
        except Exception as err:
            print(err)
    
    @bridge.bridge_command()
    @commands.cooldown(1,3600, commands.BucketType.user)
    async def work(self, ctx):
        ran = [5, 15, 20, 25, 50, 75, 100]
        mon = random.choice(ran)
        await ctx.reply("You went to work.. check back in an hour")
        await asyncio.sleep(3600)
        user_id = str(ctx.author.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(user_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {user_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {user_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `eco` SET `money` = `money` + %s WHERE `user_id`=%s"
                cursor.execute(sql, (mon,str(user_id)))
                connection.commit()
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(user_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
                await ctx.reply(f"You went to work and made {mon} peanuts, your current balance is {money} peanuts")
        except Exception as err:
            print(err)
    
    

    @bridge.bridge_command(aliases=['transfer'])
    async def pay(self, ctx, user: discord.User, amount: int):
        user_id = str(ctx.author.id)
        rep_id = str(user.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(user_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {user_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {user_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(user_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
        except Exception as err:
            print(err)
        
        if amount >= money:
            user_id = str(ctx.author.id)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    # Read a single record
                    guild = ctx.author.guild
                    sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (str(rep_id),str(guild.id),100))
                    connection.commit()
                    print(f"Sucess! Added a eco account for {rep_id}")
                    connection.close()
            except Exception as err:
                print(f"{err}! Error occured adding a eco account for {rep_id}")
            
            await asyncio.sleep(1)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "UPDATE `eco` SET `money` = `money` - %s WHERE `user_id`=%s"
                    cursor.execute(sql, (amount,str(user_id)))
                    connection.commit()
                    sql = "UPDATE `eco` SET `money` = `money` + %s WHERE `user_id`=%s"
                    cursor.execute(sql, (amount,str(rep_id)))
                    connection.commit()
                    sql = "SELECT `money` from `eco` WHERE `user_id`=%s"
                    cursor.execute(sql, (str(rep_id),))
                    result = cursor.fetchone()
                    result = json.dumps(result,sort_keys=True)
                    result = json.loads(result)
                    money = result['money']
                    connection.close()
                    await ctx.reply(f"Success, gave {amount} peanuts to {user.mention} -- they now have {money} peanuts.")
            except Exception as err:
                print(err)
        else:
            await ctx.reply("You do not have the correct amount of peanuts to do this action.")
                
    

    @bridge.bridge_command()
    @commands.has_permissions(administrator=True)
    async def give(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(recipient_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {recipient_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {recipient_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `eco` SET `money` = `money` + %s WHERE `user_id`=%s"
                cursor.execute(sql, (amount,str(recipient_id)))
                connection.commit()
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(recipient_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
                await ctx.reply(f"Gave {amount} peanuts to {user.mention} - their current balance is {money} peanuts")
        except Exception as err:
            print(err)

    @bridge.bridge_command()
    @commands.has_permissions(administrator=True)
    async def take(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(recipient_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {recipient_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {recipient_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `eco` SET `money` = `money` - %s WHERE `user_id`=%s"
                cursor.execute(sql, (amount,str(recipient_id)))
                connection.commit()
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(recipient_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
                await ctx.reply(f"Took {amount} peanuts from {user.mention} - their current balance is {money} peanuts")
        except Exception as err:
            print(err)
    
    @bridge.bridge_command()
    @commands.cooldown(1,3600, commands.BucketType.user)
    async def steal(self, ctx, user: discord.User):
        user_id = ctx.author.id
        recipient_id = user.id
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(user_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {user_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {user_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(user_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                p1money = result['money']
                print(f"P1 Money: {p1money}")
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(recipient_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                p2money = result['money']
                print(f"P2 Money: {p2money}")
                connection.close()
        except Exception as err:
            print(err)

        if random.randint(1, 20) == 1:
            if p2money <= 4:
                await ctx.reply("You can't steal from someone with so little money!")
                return

            amount_stolen = random.randint(1, p2money // 2)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "UPDATE `eco` SET `money` = `money` - %s WHERE `user_id`=%s"
                    cursor.execute(sql, (amount_stolen, str(recipient_id),))
                    connection.commit()
                    sql = "UPDATE `eco` SET `money` = `money` + %s WHERE `user_id`=%s"
                    cursor.execute(sql, (amount_stolen, str(user_id),))
                    connection.commit()
                    sql = "SELECT `money` from `eco` WHERE `user_id`=%s"
                    cursor.execute(sql, (str(user_id),))
                    result = cursor.fetchone()
                    result = json.dumps(result,sort_keys=True)
                    result = json.loads(result)
                    money = result['money']
                    connection.close()
                    await ctx.reply(f"Success, you stole {amount_stolen} peanuts from {user.name} - you now have {money} peanuts.")
            except Exception as err:
                print(err)
        else:
            if p1money <= 4:
                await ctx.reply(f"You failed to steal from {user.name} and are now on the run from the police!")
                return
            amount_lost = random.randint(1, p1money // 4)
            try:
                connection = connecttodb()
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "UPDATE `eco` SET `money` = `money` - %s WHERE `user_id`=%s"
                    cursor.execute(sql, (amount_lost, str(user_id),))
                    connection.commit()
                    sql = "SELECT `money` from `eco` WHERE `user_id`=%s"
                    cursor.execute(sql, (str(user_id),))
                    result = cursor.fetchone()
                    result = json.dumps(result,sort_keys=True)
                    result = json.loads(result)
                    money = result['money']
                    connection.close()
                    await ctx.reply(f"You failed to steal from {user.name} and lost {amount_lost} peanuts in bail to the police - you now have {money} peanuts.")
            except Exception as err:
                print(err)
    
    @steal.error
    async def steal_error(error, interaction):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = round(error.retry_after)
            em = discord.Embed(title="Don't be stupid!", description=f"You tried to steal for the second time in one hour. The cops are now on high alert for the next {remaining_time} seconds.")
            await interaction.repsonse.send_message(embed=em)


    @bridge.bridge_command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, user: discord.User, amount: int):
        recipient_id = str(user.id)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.author.guild
                sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(recipient_id),str(guild.id),100))
                connection.commit()
                print(f"Sucess! Added a eco account for {recipient_id}")
                connection.close()
        except Exception as err:
            print(f"{err}! Error occured adding a eco account for {recipient_id}")
        
        await asyncio.sleep(1)
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `eco` SET `money` = %s WHERE `user_id`=%s"
                cursor.execute(sql, (amount,str(recipient_id)))
                connection.commit()
                sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
                cursor.execute(sql, (str(recipient_id),))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                money = result['money']
                connection.close()
                await ctx.reply(f"Set {user.mention}'s cash to £{amount} - their current balance is £{money}")
        except Exception as err:
            print(err)

def setup(bot):
    bot.add_cog(Economy(bot))
