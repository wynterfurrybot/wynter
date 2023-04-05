import discord
from discord.ext import commands, bridge
import random
from datetime import datetime
import asyncio
import re
class Christmas(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @bridge.bridge_command(pass_context=True, help = 'Get a random item from the advent calander.', description = 'Get a random item from the advent calander')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def advent(self, ctx: bridge.BridgeContext):
        await ctx.defer()
        try:
            if "cm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        items = ["Chocolate Reindeer", "Chocolate Snowflake", "Chocolate Elf", "Chocolate Santa", "Chocolate Christmas Tree"]
        today = datetime.today()
        if isinstance(ctx, bridge.BridgeApplicationContext):
            if today.month == 12 and today.day <= 25:
                days = 25 - int(today.day)
                await ctx.interaction.user.send("There is " + str(days) + " day(s) left until christmas!")
                await ctx.interaction.user.send("You got a " + str(random.choice(items)))
                await ctx.respond(f":e_mail: {ctx.interaction.user.mention} Check your DMs!")

            else:
                await ctx.interaction.user.send("It is not december yet - or is past christmas!")
            
        else:
            if today.month == 12 and today.day <= 25:
                days = 25 - int(today.day)
                await ctx.message.author.send("There is " + str(days) + " day(s) left until christmas!")
                await ctx.message.author.send("You got a " + str(random.choice(items)))
                await ctx.respond(f":e_mail: {ctx.message.author.mention} Check your DMs!")

            else:
                await ctx.message.author.send("It is not december yet - or is past christmas!")
                await ctx.respond(f":e_mail: {ctx.message.author.mention} Check your DMs!")
    
    @bridge.bridge_command(pass_context=True, help = 'Throw a snowball at someone else', description = 'Throw a snowball at someone else')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def snowball(self, ctx: bridge.BridgeContext, *, users:str):
        memcount = 0
        members = []
        for user in users.split(" "):
            members.append(await ctx.guild.fetch_member(int(user.strip('<@!>'))) for mention in re.findall(r'(<@)?!?[0-9]{17,18}>?', user))
        for member in members:
            memcount = memcount+1
        try:
            if "cm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if isinstance(ctx, bridge.BridgeApplicationContext):
            if memcount > 3:
                embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
                embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.respond(ctx.interaction.user.mention, embed = embed) 
            if str(ctx.interaction.user.id) in users:
                embed = discord.Embed(title = "Snowball Fight!", description = f"{self.bot.user.mention} throws a snowball directly at {users}. \nGotcha!", color=0x00ff00)
                embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.respond(f"{users}", embed = embed)

            embed = discord.Embed(title = "Snowball Fight!", description = f"{ctx.interaction.user.mention} throws a snowball directly at {users}. \nGotcha!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(f"{users}",embed = embed)
        else:
            if memcount > 3:
                embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
                embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.respond(ctx.message.author.mention, embed = embed) 
        
            if str(ctx.message.author) in users:
                embed = discord.Embed(title = "Snowball Fight!", description = f"{self.bot.user.mention} throws a snowball directly at {users}. \nGotcha!", color=0x00ff00)
                embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.respond(embed = embed)

            embed = discord.Embed(title = "Snowball Fight!", description = f"{ctx.message.author.mention} throws a snowball directly at {users}. \nGotcha!", color=0x00ff00)
            embed.set_image(url = "https://media3.giphy.com/media/xUySTqYAa9n6awCiSk/giphy.gif")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)
    
    @bridge.bridge_command(pass_context=True, help = 'Get a easter present (only works on eater sunday, until Easter Monday)', description= 'Get a easter present (only works on eater sunday, until Easter Monday)')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def egg(self, ctx: bridge.BridgeContext):
        try:
            if "cm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if isinstance(ctx, bridge.BridgeApplicationContext):
            items = ["large Malteasers easter egg", "large Mini Egg Easter Egg", "A huge easter egg only sold in costco", "large Galaxy Easter Egg"]
            today = datetime.today()
            christmas = datetime(2022, 4, 17, 7, 0)
            duration = christmas - today
            print(f"It is {duration.total_seconds()} seconds 'till easter!")
            if today.month == 4 and today.day <= 18:
                await ctx.interaction.user.send("I wonder what the easter bunny will bring! \n\nCheck back at 8AM UTC on Easter Sunday to find out!")
                await asyncio.sleep(duration.total_seconds())
                await ctx.interaction.user.send(f"*You wake up early on easter morning, a smile on your face as you check underneath your bed, finding a gift labeled from the Easter Bunny! \n\nExcited, you open it, revealing what's inside: A  {random.choice(items)} - just for you!")

            else:
                await ctx.interaction.user.send("It is not easter yet - or is past easter!")
            await ctx.respond(f":e_mail: {ctx.interaction.user.mention} Check your DMs!")
        else:
            items = ["large Malteasers easter egg", "large Mini Egg Easter Egg", "A huge easter egg only sold in costco", "large Galaxy Easter Egg"]
            today = datetime.today()
            christmas = datetime(2022, 4, 17, 7, 0)
            duration = christmas - today
            print(f"It is {duration.total_seconds()} seconds 'till easter!")
            if today.month == 4 and today.day <= 18:
                await ctx.author.send("I wonder what the easter bunny will bring! \n\nCheck back at 8AM UTC on Easter Sunday to find out!")
                await asyncio.sleep(duration.total_seconds())
                await ctx.author.send(f"*You wake up early on easter morning, a smile on your face as you check underneath your bed, finding a gift labeled from the Easter Bunny! \n\nExcited, you open it, revealing what's inside: A  {random.choice(items)} - just for you!")

            else:
                await ctx.author.send("It is not easter yet - or is past easter!")
            await ctx.respond(f":e_mail: {ctx.author.mention} Check your DMs!")

    @bridge.bridge_command(pass_context=True, help = 'Get a christmas present (only works on christmas day, until the 31st December)', description= 'Get a christmas present (only works on christmas day, until the 31st December)')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def present(self, ctx: bridge.BridgeContext):
        try:
            if "cm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if isinstance(ctx, bridge.BridgeApplicationContext):
            items = ["PS5", "Xbox Series X", "Gaming Computer", "Gaming Laptop", "Oculus Quest 2 Headset", "NVIDIA RTX 3080", "Ugly Sweater", "Pair of socks", "Sealed copy of Cyberpunk 2077 - collecters edition"]
            today = datetime.today()
            christmas = datetime(2022, 12, 25, 7, 0)
            duration = christmas - today
            print(f"It is {duration.total_seconds()} seconds 'till christmas!")
            if today.month == 12 and today.day <= 31:
                await ctx.interaction.user.send("I wonder what Santa Paws will bring! \n\nCheck back at 8AM UTC on Christmas Day to find out!")
                await ctx.respond(f":e_mail: {ctx.interaction.user.mention} Check your DMs!")
                await asyncio.sleep(duration.total_seconds())
                await ctx.interaction.user.send(f"*You wake up on Christmas morning, a smile on your face as you check underneath the tree, finding a present labeled from Santa Paws! \n\nExcited, you open it, revealing what's inside: A brand new {random.choice(items)} - just for you!")

            else:
                await ctx.interaction.user.send("It is not december yet - or is past christmas!")
                await ctx.respond(f":e_mail: {ctx.interaction.user.mention} Check your DMs!")
        else:
            items = ["PS5", "Xbox Series X", "Gaming Computer", "Gaming Laptop", "Oculus Quest 2 Headset", "NVIDIA RTX 3080", "Ugly Sweater", "Pair of socks", "Sealed copy of Cyberpunk 2077 - collecters edition"]
            today = datetime.today()
            christmas = datetime(2022, 12, 25, 7, 0)
            duration = christmas - today
            print(f"It is {duration.total_seconds()} seconds 'till christmas!")
            if today.month == 12 and today.day <= 31:
                await ctx.message.author.send("I wonder what Santa Paws will bring! \n\nCheck back at 8AM UTC on Christmas Day to find out!")
                await ctx.respond(f":e_mail: {ctx.message.author.mention} Check your DMs!")
                await asyncio.sleep(duration.total_seconds())
                await ctx.message.author.send(f"*You wake up on Christmas morning, a smile on your face as you check underneath the tree, finding a present labeled from Santa Paws! \n\nExcited, you open it, revealing what's inside: A brand new {random.choice(items)} - just for you!")

            else:
                await ctx.message.author.send("It is not december yet - or is past christmas!")
                await ctx.respond(f":e_mail: {ctx.message.author.mention} Check your DMs!")
            

def setup(bot):
    bot.add_cog(Christmas(bot))