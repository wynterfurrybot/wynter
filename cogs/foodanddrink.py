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
        embed = discord.Embed(title = "Here is what is on the menu!", description = "**__Food:__** \n\nCookie\nSandwich\nBird Seed\nPineapples\nSteak\nPizza\nMuffin \n\n**__Drinks:__**\nCola\nPepsi\nBeer\nVodka\nWhiskey\nMartini\nPina Colada\nRum\nTea\nCoffee", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'cookie', pass_context=True, help = 'Order a cookie')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def cookie(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
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
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a muffin.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a muffin, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'cola', pass_context=True, help = 'Order a cola')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def cola(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of cola.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of cola, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'pepsi', pass_context=True, help = 'Order a cola', aliases = ['bepis'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def pepsi(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of pepsi.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of pepsi, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'beer', pass_context=True, help = 'Order a beer')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def beer(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of beer.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of beer, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'vodka', pass_context=True, help = 'Order a vodka')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def vodka(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of vodka.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of vodka, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'whiskey', pass_context=True, help = 'Order a whiskey', aliases = ['whisky'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def whiskey(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of whiskey.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of whiskey, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'martini', pass_context=True, help = 'Order a whiskey')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def martini(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a martini.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a martini, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'rum', pass_context=True, help = 'Order a rum')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def rum(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of rum.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of rum, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(name = 'pinacolada', pass_context=True, help = 'Order a pina colada')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def pinacolada(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a pina colada.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a pina colada, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'tea', pass_context=True, help = 'Order a mug of tea')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def tea(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a mug of tea.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of tea, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(name = 'coffee', pass_context=True, help = 'Order a mug of coffee')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def coffee(self, ctx, user:discord.Member = None):
        if user == None or user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a mug of coffee.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
        else:
            embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of coffee, from {ctx.message.author.mention}.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
            embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
            return await ctx.send(embed = embed, reference = ctx.message)
def setup(bot):
    bot.add_cog(FoodAndDrink(bot))