import discord
from discord.ext import commands
import random
from datetime import datetime
import asyncio
import re
class Christmas(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @discord.slash_command()
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def advent_calendar(self,ctx):
        items = ["Chocolate Reindeer", "Chocolate Snowflake", "Chocolate Elf", "Chocolate Santa", "Chocolate Christmas Tree"]
        today = datetime.today()
        if today.month == 12 and today.day <= 25:
            days = 25 - int(today.day)
            await ctx.author.send("There is " + str(days) + " day(s) left until christmas!")
            await ctx.author.send("You got a " + str(random.choice(items)))
            await ctx.respond(f":e_mail: {ctx.author.mention} Check your DMs!")

        else:
            await ctx.author.send("It is not december yet - or is past christmas!")
            await ctx.respond(f":e_mail: {ctx.author.mention} Check your DMs!")
    
    @discord.slash_command()
    async def snowball(self,ctx, user:discord.Member):
        if ctx.author.id == user.id:
            channel = ctx.channel
            embed = discord.Embed(title = "Brrr.. cold!", description = f"{ctx.author.mention} forgot how to make snowballs and instead faceplanted right into the snow!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)
        if self.bot.user.id == user.id:
            channel = ctx.channel
            embed = discord.Embed(title = "Snowball Fight!", description = f"I'll get you back for that one, just you wait!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            await ctx.respond(embed = embed)

            rn = random.randint(5, 15)

            await asyncio.sleep(rn)

            embed = discord.Embed(title = "Snowball Fight!", description = f"{self.bot.user.mention} throws a snowball directly at {ctx.author.mention}. \nGotcha!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await channel.send(ctx.author.mention, embed = embed)
        else:
            embed = discord.Embed(title = "Snowball Fight!", description = f"{ctx.author.mention} throws a snowball directly at {user.mention}. \nGotcha!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(Christmas(bot))

