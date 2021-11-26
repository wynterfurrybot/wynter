import discord
from discord.ext import commands
import random
from datetime import datetime
import asyncio

class Christmas(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'advent', pass_context=True, help = 'Get a random item from the advent calander.')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def advent(self, ctx):
        items = ["Chocolate Reindeer", "Chocolate Snowflake", "Chocolate Elf", "Chocolate Santa", "Chocolate Christmas Tree"]
        today = datetime.today()
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        if today.month == 12 and today.day <= 25:
            days = 25 - int(today.day)
            await ctx.message.author.send("There is " + str(days) + " day(s) left until christmas!")
            await ctx.message.author.send("You got a " + str(random.choice(items)))

        else:
            await ctx.message.author.send("It is not december yet - or is past christmas!")
    
    @commands.command(name = 'snowball', pass_context=True, help = 'Throw a snowball at someone else')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def snowball(self, ctx, *, user):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Snowball Fight!", description = f"{self.bot.user.mention} throws a snowball directly at {user}. \nGotcha!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Snowball Fight!", description = f"{ctx.message.author.mention} throws a snowball directly at {user}. \nGotcha!", color=0x00ff00)
        embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'present', pass_context=True, help = 'Try running it and seeing what happens ;)')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def present(self, ctx):
        items = ["PS5", "Xbox Series X", "Gaming Computer", "Gaming Laptop", "Oculus Quest 2 Headset", "NVIDIA RTX 3080", "Ugly Sweater", "Pair of socks", "Sealed copy of Cyberpunk 2077 - collecters edition"]
        today = datetime.today()
        christmas = datetime(2021, 12, 25, 7, 0)
        duration = christmas - today
        print(f"It is {duration.total_seconds()} seconds 'till christmas!")
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        if today.month == 12 and today.day <= 31:
            await ctx.message.author.send("I wonder what Santa Paws will bring! \n\nCheck back at 8AM UTC on Christmas Day to find out!")
            await asyncio.sleep(duration.total_seconds())
            await ctx.message.author.send(f"*You wake up on Christmas morning, a smile on your face as you check underneath the tree, finding a present labeled from Santa Paws! \n\nExcited, you open it, revealing what's inside: A brand new {random.choice(items)} - just for you!")

        else:
            await ctx.message.author.send("It is not december yet - or is past christmas!")

def setup(bot):
    bot.add_cog(Christmas(bot))