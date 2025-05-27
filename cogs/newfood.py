import discord
from discord import options
from discord.ext import commands
import http.client
import mimetypes
import json
import asyncio
from dotenv import load_dotenv
import pymysql.cursors
import os
import json

load_dotenv()
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')
item = ""
member = None

def connecttodb():
    # Connect to the database
    connection = pymysql.connect(host=DBHOST,
                                user=DBUSER,
                                password=DBPW,
                                db=DB,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

async def take_money(recipient_id, interaction, amount):
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            guild = interaction.guild
            sql = "INSERT IGNORE INTO `eco` (user_id, server_id, money) VALUES (%s, %s, %s)"
            cursor.execute(sql, (str(recipient_id),str(guild.id),amount))
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
            sql = "SELECT `money` FROM `eco` WHERE `user_id`=%s"
            cursor.execute(sql, (str(recipient_id),))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            money = result['money']
            if money >= 10000000:
                sql = "UPDATE `eco` SET `money` = `money` - %s WHERE `user_id`=%s"
                cursor.execute(sql, (amount,str(recipient_id)))
                connection.commit()
                connection.close()
            else:
                return await interaction.response.send_message(f"You do not have enough money for this item. It requires £{amount} and you have £{money}.")
    except Exception as err:
        print(err)

class OrderModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Item", style=discord.InputTextStyle.short, placeholder="type menu for the menu"))

    async def callback(self, interaction: discord.Interaction):
        inp = self.children[0].value
        user = interaction.user
        food = [
        {
            "name" : "test item that is way too expensive for anyone to reasonabily afford (just type \"test\" to order)",
            "cost" : 10000000
        },
        {
            "name": "cookie",
            "cost": 10
        },
        {
            "name": "sandwich",
            "cost": 10
        },
        {
            "name": "seeds",
            "cost": 10
        },
        {
            "name": "pineapples",
            "cost": 10
        },
        {
            "name": "steak",
            "cost": 25
        },
        {
            "name": "pizza",
            "cost": 15
        },
        {
            "name": "muffin",
            "cost": 10
        }
        ]
        drinks = [
            {
                "name": "cola",
                "cost": 10
            },
            {
                "name": "pepsi",
                "cost": 10
            },
            {
                "name": "beer",
                "cost": 15
            },
            {
                "name": "vodka",
                "cost": 20
            },
            {
                "name": "whiskey",
                "cost": 15
            },
            {
                "name": "martini",
                "cost": 15
            },
            {
                "name": "pina colada",
                "cost": 20
            },
            {
                "name": "rum",
                "cost": 15
            },
            {
                "name": "tea",
                "cost": 5
            },
            {
                "name": "coffee",
                "cost": 5
            }
        ]

        if inp.lower() == "test":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10000000)
            
        
        elif inp.lower() == "menu":
            embed = discord.Embed(title = "The Menu!", color=0x00ff00)
            embed.add_field(name = "Food", value = "--------------")
            for f in food:
                embed.add_field(name=f['name'], value=f"£{f['cost']}", inline=False)
            embed.add_field(name = "Drinks", value = "--------------")
            for d in drinks:
                embed.add_field(name=d['name'], value=f"{d['cost']}", inline=False)
            return await interaction.response.send_message(f"{user.mention}", embed = embed)  

        elif "cookie" in inp.lower():
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)

            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{interaction.user.mention}, I present to you, 1 cookie. \n\nWith milk for dipping :)", color=0x00ff00)
                embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                embed.set_footer(text = 'Wynter 3.0')
                return await interaction.response.send_message(f"{user.mention}", embed = embed)  
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, 1 cookie, courtesy of {interaction.user.mention}. \n\nWith milk for dipping :)", color=0x00ff00)
                embed.set_image(url = "https://milkandcardamom.com/wp-content/uploads/2019/11/eggless-chocolate-chip-cookie-6-960x1358.jpg")
                embed.set_footer(text = 'Wynter 3.0')
                return await interaction.response.send_message(f"{member.mention}", embed = embed)  

        elif inp.lower() == "sandwich":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"Hey {user.mention}, here is your sandwich!", color=0x00ff00)
                embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                embed.set_footer(text = 'Wynter 3.0')
                return await interaction.response.send_message(f"{user.mention}", embed = embed)  
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"Hey {member.mention}, here is your sandwich, courtesy of {user.mention}!", color=0x00ff00)
                embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png")
                embed.set_footer(text = 'Wynter 3.0')
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "seeds":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)

            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a pile of birb seeds!", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, here is a pile of birb seeds, courtesy of {user.mention}!", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.vinehousefarm.co.uk/media/catalog/product/cache/e577a9e55fdb952a6bd2c34a3eb531cf/h/-/h-mixed_seed.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
            
        elif inp.lower() == "pineapples" or inp.lower() == "pineapple":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)

            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, here is a handful of pineapple chunks", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)  
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, here is a handful of pineapple chunks, courtesy of {user.mention}", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url= "https://delmontefoodservice.com/sites/default/files/styles/image576x529/public/product/Nice%20Fruit%20Chunks.png?itok=Zyl5Djob")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "steak" or inp.lower() == "ribeye steak" or inp.lower() == "t-bone steak":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 25)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a juicy steak, cooked to perfection.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)  
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a juicy steak, cooked to perfection. Paid for by {user.mention}", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url="https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4-500x375.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed) 
        
        elif inp.lower() == "pizza":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a 10\" pizza.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")  
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a 10\" pizza, paid for with {user.mention}'s credit card.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=480:*")  
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "muffin":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)
            if member.id == user.id:
                embed = discord.Embed(title = "I wanna die!", description = f"{user.mention}, it's muffin time!", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")  
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "I wanna die!", description = f"{member.mention}, it's muffin time!", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://sugargeekshow.com/wp-content/uploads/2019/10/chocolate-chip-muffins-featured.jpg")  
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "cola" or inp.lower() == "coke":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a glass of diet coke.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")  
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a glass of diet coke, straight from {user.mention}'s fridge.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")   
                return await interaction.response.send_message(f"{member.mention}", embed = embed)

        elif inp.lower() == "pepsi" or inp.lower() == "bepis":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 10)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a glass of diet pepsi.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")  
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a glass of diet pepsi, straight from {user.mention}'s fridge.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tumbler_of_cola_with_ice.jpg")   
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "beer":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a cold one.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg") 
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a cold one, cheers to {user.mention}.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://images.everydayhealth.com/images/everything-you-need-to-know-about-nonalcoholic-beer-1440x810.jpg")   
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "vodka":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 20)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a glass of pure, authentic vodka.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a glass of pure, authentic vodka, say thanks to {user.mention} for this one..", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.homewetbar.com/media/catalog/product/cache/265d7bf611d39b8f80e93d32d7319b33/8/1/8162-marquee-vodka-and-soda-pint-glass.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "whiskey":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a glass of whiskey.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a glass of whiskey, from {user.mention}'s personal stash.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "martini":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a martini.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a martini, from {user.mention}'s personal stash.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dirty-martini-3e964eb.jpg?quality=90&resize=504,458?quality=90&webp=true&resize=504,458")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "rum":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 15)
            if member.id == user.id:
                embed = discord.Embed(title = "Try mixing it with coke!", description = f"{user.mention}, I present to you, a glass of rum.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Try mixing it with coke!", description = f"{member.mention}, I present to you, a glass of rum, from {user.mention}'s personal stash.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg/1200px-Appleton_Estate_V-X_Jamaica_Rum-with_glass.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "pina colada":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 20)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a pina colada.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a pina colada, an excellent choice made by {user.mention}.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://www.acouplecooks.com/wp-content/uploads/2020/11/Pina-Colada-056.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "tea":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 5)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a teapot of tea.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a teapot of tea. \n\nMaybe you and {user.mention} can share?", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
        
        elif inp.lower() == "coffee":
            recipient_id = str(user.id)
            take_money(recipient_id, interaction, 5)
            if member.id == user.id:
                embed = discord.Embed(title = "Enjoy!", description = f"{user.mention}, I present to you, a mug of coffee.", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                return await interaction.response.send_message(f"{user.mention}", embed = embed)
            else:
                embed = discord.Embed(title = "Enjoy!", description = f"{member.mention}, I present to you, a mug of coffee. Enjoy it!", color=0x00ff00)
                embed.set_footer(text = 'Wynter 3.0')
                embed.set_image(url = "https://c.files.bbci.co.uk/F800/production/_109288436_tea-milk-cookies.jpg")
                return await interaction.response.send_message(f"{member.mention}", embed = embed)
                
        else:
            embed = discord.Embed(title = "Not happening!", description = f"{interaction.user.mention}, there is no such thing as {inp} on the menu.", color=0x00ff00)
            embed.set_footer(text = 'Wynter 3.0')
            return await interaction.response.send_message(f"{user.mention}", embed = embed)
    

class FoodAndDrink(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @discord.slash_command()
    async def order(self, ctx, user: discord.Option(discord.Member, description="User you're giving this item to (optional if self)" ,required = False)):
        modal = OrderModal(title="What would you like?")
        global member
        if user:
            member = user
        else:
            member = ctx.author
        await ctx.send_modal(modal)

def setup(bot):
    bot.add_cog(FoodAndDrink(bot))