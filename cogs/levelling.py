import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv
import pymysql.cursors

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

class Levelling(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'level', pass_context=True, help = 'Get your current level')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def level(self, ctx):
        connection = connecttodb()
        try:
             with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from `xp` WHERE `user_id`=%s"
                cursor.execute(sql, (ctx.message.author.id))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                xp = result['xp']
                level = 0
                if xp < 100:
                    level = 1
                elif xp < 250:
                    level = 2
                else:
                    level = 3
                embed = discord.Embed(title = "Current Level", description = f"Not fully implemented yet. \n\nYour Level: `{level}`", color=0x00ff00)
                embed.set_thumbnail(url = ctx.message.author.avatar_url)
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.send(embed = embed)
        except Exception as err:
            err = str(err)
            if "NoneType" in err:
                with connection.cursor() as cursor:
                    # Insert a single record
                    sql = "INSERT INTO `xp` (user_id, guild_id, xp) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (ctx.message.author.id, ctx.message.guild.id , 1))
                    connection.commit()
                    print(f"Sucess! Added a levelling profile for {ctx.message.author.id}")
                    connection.close()
                    embed = discord.Embed(title = "Current Level", description = f"Not fully implemented yet. \n\nYour Level: `1`", color=0x00ff00)
                    embed.set_thumbnail(url = ctx.message.author.avatar_url)
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Levelling(bot))