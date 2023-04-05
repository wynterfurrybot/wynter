import discord
from discord.ext import commands, bridge
import http.client
import mimetypes
import json
import asyncio

class FoodAndDrink(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @bridge.bridge_command(name = 'menu', pass_context=True, help = 'Displays the menu of avalible items')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def menu(self, ctx: bridge.BridgeContext):
        try:
            if "fdm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        embed = discord.Embed(title = "Here is what is on the menu!", description = "**__Food:__** \n\nCookie\nSandwich\nBird Seed\nPineapples\nSteak\nPizza\nMuffin \n\n**__Drinks:__**\nCola\nPepsi\nBeer\nVodka\nWhiskey\nMartini\nPina Colada\nRum\nTea\nCoffee", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.respond(embed = embed)
    
    @bridge.bridge_command(name = 'order', pass_context=True, help = 'Order an item from the menu')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def cookie(self, ctx: bridge.BridgeContext, *, user:discord.Member, item:str):
        try:
            if "fdm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if item.lower() == "cookie":       
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, 1 cookie. \n\nWith milk for dipping :)", color=0x00ff00)
                    embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 cookie from {ctx.interaction.user.mention}. \n\nWith milk for dipping :)", color=0x00ff00)
                    embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, 1 cookie. \n\nWith milk for dipping :)", color=0x00ff00)
                    embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 cookie from {ctx.message.author.mention}. \n\nWith milk for dipping :)", color=0x00ff00)
                    embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(embed = embed)
        elif item.lower() == "sandwich":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, 1 sandwich.", color=0x00ff00)
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 sandwich from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, 1 sandwich.", color=0x00ff00)
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is 1 sandwich from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                    embed.set_footer(text = 'Wynter 2.0')
                    return await ctx.respond(embed = embed)
        elif item.lower() == "seeds":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a pile of birb seeds.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a pile of birb seeds from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a pile of birb seeds.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a pile of birb seeds from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "pineapple":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a handful of pineapple chunks.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a handful of pineapple chunks from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a handful of pineapple chunks.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a handful of pineapple chunks from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "steak":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a juicy steak, cooked to perfection.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a juicy steak, cooked to perfection from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a juicy steak, cooked to perfection.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a juicy steak, cooked to perfection from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "pizza":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a 10\" pizza.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a 10\" pizza, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a 10\" pizza.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a 10\" pizza, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "muffin":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a muffin.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a muffin, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a muffin.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a muffin, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "cola" or item.lower() == "coke":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of cola.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of cola, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of cola.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of cola, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "pepsi":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of pepsi.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of pepsi, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of pepsi.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of pepsi, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")
                    return await ctx.respond(embed = embed)
        elif item.lower() == "beer":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of beer.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of beer, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of beer.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of beer, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")
                    return await ctx.respond(embed = embed)

        elif item.lower() == 'vodka':
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of vodka.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of vodka, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of vodka.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of vodka, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                    return await ctx.respond(embed = embed)
   
        elif item.lower() =="whiskey":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of whiskey.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of whiskey, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of whiskey.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of whiskey, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                    return await ctx.respond(embed = embed)

        elif item.lower()=="martini":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a martini.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a martini, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a martini.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a martini, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                    return await ctx.respond(embed = embed)
    
        elif item.lower() == "rum":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a glass of rum.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of rum, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a glass of rum.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a glass of rum, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                    return await ctx.respond(embed = embed)
    
        elif item.lower() == "pinacolada" or item.lower() == "pina colada":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a pina colada.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a pina colada, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a pina colada.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a pina colada, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                    return await ctx.respond(embed = embed)

        elif item.lower() == "tea":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a mug of tea.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of tea, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a mug of tea.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of tea, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                    return await ctx.respond(embed = embed)

        elif item.lower() == "coffee":
            if isinstance(ctx, bridge.BridgeApplicationContext):
                if not user or user.id == ctx.interaction.user.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.interaction.user.mention}, I present to you, a mug of coffee.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of coffee, from {ctx.interaction.user.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
                    return await ctx.respond(f"{user.mention}", embed = embed)
            else:
                if not user or user.id == ctx.message.author.id:
                    embed = discord.Embed(title = "Enjoy!", description = f"{ctx.message.author.mention}, I present to you, a mug of coffee.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here's a mug of coffee, from {ctx.message.author.mention}.", color=0x00ff00)
                    embed.set_footer(text = 'Wynter 2.0')
                    embed.set_image(url = "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p.jpg")
                    return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "I don't quite know how you got here!", description = f"You probably entered an invalid item.", color="red")
            embed.set_footer(text = 'Wynter 2.0')
            m = await ctx.respond(embed = embed)
            await asyncio.sleep(5)
            await m.delete()
def setup(bot):
    bot.add_cog(FoodAndDrink(bot))