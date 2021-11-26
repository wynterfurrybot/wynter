import discord
from discord.ext import commands
import http.client
import mimetypes
import json

class FoodAndDrink(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'menu', pass_context=True, help = 'Displays the menu of avalible items')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def menu(self, ctx):
        embed = discord.Embed(title = "Here is what is on the menu!", description = "Food: \n\nCookie\nSandwich\nBird Seed\nPineapples\nSteak\nPizza\nMuffin \n\nDrinks:\nCola\nPepsi\nBeer\nVodka\nWhiskey\nMartini\nPina Colada\nRum\nTea\nCoffee \n\nAt this time, only food is avalible to purchase, and you may only order for yourself. This will be fixed in the near future", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'cookie', pass_context=True, help = 'Order a cookie')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def cookie(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, 1 cookie. \n\nWith milk for dipping :)", color=0x00ff00)
            embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 cookie from {ctx.message.author.mention}. \n\nWith milk for dipping :)", color=0x00ff00)
            embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)


    @commands.command(name = 'sandwich', pass_context=True, help = 'Order a sandwich')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sandwich(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, 1 sandwich.", color=0x00ff00)
            embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 sandwich from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'seeds', pass_context=True, help = 'Order Bird seeds', aliases=['seed', 'birdseed', 'birdseeds'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def seeds(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a pile of birb seeds.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a pile of birb seeds from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'pineapple', pass_context=True, help = 'Order pineapple slices')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def pineapple(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a handful of pineapple chunks.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a handful of pineapple chunks from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'steak', pass_context=True, help = 'Order a steak')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def steak(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a juicy steak, cooked to perfection.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a juicy steak, cooked to perfection from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)


    @commands.command(name = 'pizza', pass_context=True, help = 'Order a pizza')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def pizza(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a 10\" pizza.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a 10\" pizza, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'muffin', pass_context=True, help = 'Order a muffin')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def muffin(self, ctx, user:discord.Member = None):
        if user == None:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a muffin.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a muffin, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

def setup(bot):
    bot.add_cog(FoodAndDrink(bot))