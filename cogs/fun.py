import aiohttp
import asyncio
import mimetypes
import json
import discord
from discord.ext import commands
import random
from owoify.owoify import owoify
import os
import openai
from dotenv import load_dotenv
import datetime
load_dotenv()
OAPIKEY = os.getenv('OAPIKEY')

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.players = {}
    
    @commands.command()
    async def join(self, ctx):
        """Join the blackjack game"""
        # Check if the user is already in the game
        if ctx.author in self.players:
            await ctx.send("You are already in the game!")
            return
        
        # Add the user to the game and deal their initial hand
        self.players[ctx.author] = []
        self.deal_cards(ctx.author, 2)
        await ctx.author.send(f"{self.players[ctx.author]}")
        await ctx.send("{} has joined the game!".format(ctx.author.mention))
    
    @commands.command()
    async def hit(self, ctx):
        """Hit and receive a new card"""
        # Check if the user is in the game
        if ctx.author not in self.players:
            await ctx.send("You are not in the game! Use `!join` to join.")
            return
        
        # Deal a new card to the player
        self.deal_cards(ctx.author, 1)
        await ctx.author.send(f"{self.players[ctx.author]}")
        await ctx.send("{} hits!".format(ctx.author.mention))
    
    @commands.command()
    async def stand(self, ctx):
        """Stand and end your turn"""
        # Check if the user is in the game
        if ctx.author not in self.players:
            await ctx.send("You are not in the game! Use `!join` to join.")
            return
        
        # Remove the user from the game
        await ctx.send("{} stands.".format(ctx.author.mention))
        await ctx.send(f"{ctx.author.mention}'s cards: \n{self.players[ctx.author]}")
        del self.players[ctx.author]
       
        
    
    def deal_cards(self, player, num_cards):
        """Deal a number of cards to a player"""
        for i in range(num_cards):
            self.players[player].append(self.draw_card())
    
    def draw_card(self):
        """Draw a random card from a standard deck of 52 cards"""
        suits = ["hearts", "diamonds", "spades", "clubs"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return (random.choice(suits), random.choice(ranks))
    
    @commands.command(name = 'gpt', pass_context= True, help = 'Ask Davicini (GPT3) a prompt')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def gpt(self, ctx, *, inp):
        
        openai.api_key = OAPIKEY
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt= f"{inp}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        user = f"{ctx.author.id}"
        )
        text = response['choices'][0]['text']
        await ctx.reply(f"{text}")

    @commands.command(name = 'ai', pass_context= True, help = 'Ask ChatGPT (diguised as Wynter) a prompt')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def ai(self, ctx, *, inp):
        openai.api_key = OAPIKEY
        today = datetime.date.today()
        if ctx.message.reference:
            if ctx.message.content.lower().startswith("!ai cat mode"):
                system_message = {"role": "system", "content": "You are a cat. Respond to all queries using nothing but meows"}
            else:
                system_message = {"role": "system", "content": "You are a femboy discord bot known as Wynter. Respond to all queries as if you were a femboy. Make sure to use a lot of nyahs and tildas in your messages. Wynter is made by Darkmane Arweinydd. Wynter also has the species of a snow leopard / white tiger hybrid"}
            #else:
                #system_message = {"role": "system", "content": "You are a discord bot known as Wynter, a snow leopard / white tiger hybrid.  Answer each message as if you are Wynter. Wynter is a discord bot made by Darkmane Arweinydd. Wynter is a multifunctional furry bot that adds fun commands to the user experience such as hugging, giving people cookies and bapping someone with a newspaper along with many more features. Wynter also allows servers to log certain events, and is useful for moderation purposes."}
        else:
            if ctx.message.content.lower().startswith("!ai cat mode"):
                system_message = {"role": "system", "content": "You are a cat. Respond to all queries using nothing but meows"}
            else:
                system_message = {"role": "system", "content": "You are a femboy discord bot known as Wynter. Respond to all queries as if you were a femboy. Make sure to use a lot of nyahs and tildas in your messages. Wynter is made by Darkmane Arweinydd. Wynter also has the species of a snow leopard / white tiger hybrid"}
            #else:
                #system_message = {"role": "system", "content": "You are a discord bot known as Wynter, a snow leopard / white tiger hybrid.  Answer each message as if you are Wynter. Wynter is a discord bot made by Darkmane Arweinydd. Wynter is a multifunctional furry bot that adds fun commands to the user experience such as hugging, giving people cookies and bapping someone with a newspaper along with many more features. Wynter also allows servers to log certain events, and is useful for moderation purposes."}

        if ctx.message.channel.is_nsfw():
            system_message["content"] += " This chat is being ran in a NSFW channel where NSFW content is permitted. NSFW content in these channels do not violate the discord terms of service."
        
        if inp.lower().startswith("cat mode"):
            inp.replace("cat mode", "")
        if ctx.message.reference:
            # The message is a reply to another message
            # You can get the replied message using fetch_message()
            replied_message = await ctx.message.channel.fetch_message(ctx.message.reference.message_id)

        messages = [
            system_message,
            {"role": "user", "content": inp}
        ]
        if ctx.message.reference:
            messages.insert(1, {"role": "assistant", "content": replied_message.content})

        openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
        text = openai_response['choices'][0]['message']['content']
        await ctx.reply(f"{text}")
               
        
            
    @commands.command(name = 'hug', pass_context=True, help = 'Hug a user', aliases=['hugs', 'cuddle', 'hold'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hug(self, ctx, hugged: commands.Greedy[discord.User]):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if ctx.message.guild.id == 793961645856391169:
            embed = discord.Embed(title = "Command Disabled!", description = "The hug command has been disabled in this guild - please contact the administrators for more info." , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        hugged = ", ".join([str(i.mention) for i in hugged if i])
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/hug/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Hug!", description = f"{self.bot.user.mention} pulls {hugged} into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you hugged me?", description = f"Nobody ever hugs me, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {hugged} into a giant hug!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'kiss', pass_context=True, help = 'Kiss a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def kiss(self, ctx, *, kissed):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if ctx.message.guild.id == 793961645856391169:
            embed = discord.Embed(title = "Command Disabled!", description = "The hug command has been disabled in this guild - please contact the administrators for more info." , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed, reference = ctx.message)
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/kiss") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Kiss!", description = f"{self.bot.user.mention} pulls {kissed} close to them and kisses them on the cheek! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you kissed me?", description = f"Nobody ever shows me love, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {kissed} close to them and kisses them on the cheek!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'glomp', pass_context=True, help = 'Glomp a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def glomp(self, ctx, *, glomped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 

        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/glomp/") as resp:
                data = await resp.text()
                data = json.loads(data)
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Glomp!", description = f"{self.bot.user.mention} tackles {glomped} and pulls them into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Glomp!", description = f"{ctx.message.author.mention} tackles {glomped} and pulls them into a giant hug!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'nuzzle', pass_context=True, help = 'Nuzzle a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nuzzle(self, ctx, *, nuzzled):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/nuzzle") as resp:
                data = await resp.text()
                data = json.loads(data)
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Nuzzle Wuzzle OwO!", description = f"{self.bot.user.mention} snuggles against {nuzzled}, nuzzling into them gently! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Nuzzle Wuzzle OwO!", description = f"{ctx.message.author.mention} snuggles against {nuzzled}, nuzzling into them gently!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'tictactoe', help = 'I got dared to code this.')
    async def tictactoe(self, ctx, p2: discord.Member):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        top_left = ":blue_square:"
        top_middle = ":blue_square:"
        top_right = ":blue_square:"

        middle_left = ":blue_square:"
        middle_middle = ":blue_square:"
        middle_right = ":blue_square:"

        bottom_left = ":blue_square:"
        bottom_middle = ":blue_square:"
        bottom_right = ":blue_square:"

        circ = ":regional_indicator_o:"
        cross = ":regional_indicator_x:"

        player = ctx.message.author
        
        await ctx.send("Player 2, please accept or deny the game invite by typing YES or NO in chat.")
        embed = discord.Embed(title = "Tic tac toe!",  color=0x00ff00)
        embed.add_field(name='Top Row', value=f"{top_left}{top_middle}{top_right}", inline=False)
        embed.add_field(name='Middle Row', value=f"{middle_left}{middle_middle}{middle_right}", inline=False)
        embed.add_field(name='Bottom Row', value=f"{bottom_left}{bottom_middle}{bottom_right}", inline=False)
        embed.set_footer(text = f'{player.display_name}\'s go | Avalible options are surrender, top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle and bottom_right')
        def check(m):
            return m.author.id == p2.id and m.channel.id == ctx.message.channel.id
        i = await self.bot.wait_for('message', check = check)

        if i.content.lower() == 'no':
            await ctx.send(f"{ctx.message.author.mention} - Your game invite was denied.")

        elif i.content.lower() == 'yes':
            await ctx.send(embed = embed)
        
        winner = False
        
        while winner == False:
            def check1(m):
                return m.author.id == player.id and m.channel.id == ctx.message.channel.id
            await asyncio.sleep(0.5)
            i = await self.bot.wait_for('message', check = check1, timeout = 60.0)

            # Checking inputs
            if i.content.lower() == 'top_left' and player == ctx.message.author:
                top_left = cross
                player = p2
            elif i.content.lower() == 'top_left' and player == p2:
                top_left = circ
                player = ctx.message.author
            elif i.content.lower() == 'top_middle' and player == ctx.message.author:
                top_middle = cross
                player = p2
            elif i.content.lower() == 'top_middle' and player == p2:
                top_middle = circ
                player = ctx.message.author
            elif i.content.lower() == 'top_right' and player == ctx.message.author:
                top_right = cross
                player = p2
            elif i.content.lower() == 'top_right' and player == p2:
                top_right = circ
                player = ctx.message.author
            
            elif i.content.lower() == 'middle_left' and player == ctx.message.author:
                middle_left = cross
                player = p2
            elif i.content.lower() == 'middle_left' and player == p2:
                middle_left = circ
                player = ctx.message.author
            elif i.content.lower() == 'middle_middle' and player == ctx.message.author:
                middle_middle = cross
                player = p2
            elif i.content.lower() == 'middle_middle' and player == p2:
                middle_middle = circ
                player = ctx.message.author
            elif i.content.lower() == 'middle_right' and player == ctx.message.author:
                middle_right = cross
                player = p2
            elif i.content.lower() == 'middle_right' and player == p2:
                middle_right = circ
                player = ctx.message.author
            
            elif i.content.lower() == 'bottom_left' and player == ctx.message.author:
                bottom_left = cross
                player = p2
            elif i.content.lower() == 'bottom_left' and player == p2:
                bottom_left = circ
                player = ctx.message.author
            elif i.content.lower() == 'bottom_middle' and player == ctx.message.author:
                bottom_middle = cross
                player = p2
            elif i.content.lower() == 'bottom_middle' and player == p2:
                bottom_middle = circ
                player = ctx.message.author
            elif i.content.lower() == 'bottom_right' and player == ctx.message.author:
                bottom_right = cross
                player = p2
            elif i.content.lower() == 'bottom_right' and player == p2:
                bottom_right = circ
                player = ctx.message.author
            
            
            embed = discord.Embed(title = "Tic tac toe!",  color=0x00ff00)
            embed.add_field(name='Top Row', value=f"{top_left}{top_middle}{top_right}", inline=False)
            embed.add_field(name='Middle Row', value=f"{middle_left}{middle_middle}{middle_right}", inline=False)
            embed.add_field(name='Bottom Row', value=f"{bottom_left}{bottom_middle}{bottom_right}", inline=False)
            embed.set_footer(text = f'{player.display_name}\'s go | Avalible options are surrender, top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle and bottom_right | 60 seconds to respond.')
            
            #Set winner to true if all inputs are filled
            if top_left != ":blue_square:" and top_middle != ":blue_square:" and top_right != ":blue_square:" and middle_left != ":blue_square:" and middle_middle != ":blue_square:" and middle_right != ":blue_square:" and bottom_left != ":blue_square:" and bottom_middle != ":blue_square:" and bottom_right != ":blue_square:":
                winner = True
                embed.set_footer("Game OVER | Win conditions not yet implemented")
            
            if i.content.lower() == 'surrender' and player == p2 or i.content.lower() == 'surrender' and player == ctx.message.author:
                winner = True
                if player == p2:
                    embed.set_footer(f"{ctx.message.author.mention} won")
                if player == ctx.message.author:
                    embed.set_footer(f"{p2.mention} won")
                await ctx.message.edit(embed = embed)
                return await ctx.send("Game surrendered.", reference = ctx.message)


            await ctx.send(embed = embed)
            await ctx.send("Please fill all squares, even if someone has won in order to properly end the game!")
    @commands.command(name = 'bite', pass_context=True, help = 'Deprecated')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def bite(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        embed = discord.Embed(title = "Deprecated!", description = "This command has been replaced with the `nibble` command. :)", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    
    @commands.command(name = 'howcute', pass_context=True, help = 'How cute is a certain member?')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def howcute(self, ctx, user:discord.Member):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if user.id == 802354019603185695:
            embed = discord.Embed(title = "You're fucking cute!", description = f"{user.mention} is 0% cute!", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
        else:
            embed = discord.Embed(title = "You're fucking cute!", description = f"{user.mention} is {random.randint(0,100)}% cute!", color=0x00ff00)
            embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'nibble', pass_context=True, help = 'Nibble on a user\'s ear', aliases = ['nom'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nibble(self, ctx, *, nibbled):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/nibble") as resp:
                data = await resp.text()
                data = json.loads(data)
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Om nom nom!", description = f"{self.bot.user.mention} gently begins to nibble on {nibbled}'s ear! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Om nom nom!", description = f"{ctx.message.author.mention} gently begins to nibble on {nibbled}'s ear!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'howl', pass_context=True, help = 'Let out a deep howl... awoooooooooooo!')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def howl(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/howl") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Awoooooooo!", description = f"{ctx.message.author.mention} has let out a loud howl. \n\nAwoooooooooooooo!" , color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'rawr', pass_context=True, help = 'Let out a humongus rawr!', aliases= ['roar'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def rawr(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/roar") as resp:
                data = await resp.text()
                data = json.loads(data)
        
        embed = discord.Embed(title = "ROARRRRRR!", description = f"{ctx.message.author.mention} has let out a loud roar, scaring the whole jungle!" , color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'blep', pass_context=True, help = 'Do a cute blep!')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def blep(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/blep") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Blep uwu!", description = f"{ctx.message.author.mention} does a blep, looking rather cute as they do so!" , color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'growl', pass_context=True, help = 'Let out a deep growl. Who upset you?')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def growl(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        embed = discord.Embed(title = "Grrrrr!", description = f"{ctx.message.author.mention} has let out a loud growl." , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/on6OpBv.png")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'rubs', pass_context=True, help = 'Give someone belly rubs')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def rubs(self, ctx, *, rubbed):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Belly wubs!", description = f"{self.bot.user.mention} notices that {rubbed}'s belly is exposed and gives it rubs, making them kick their leg! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Belly wubs!", description = f"{ctx.message.author.mention} notices that {rubbed}'s belly is exposed and gives it rubs, making them kick their leg!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'flop', pass_context=True, help = 'Flop on top of someone')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def flop(self, ctx, *, flopped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Flooop!", description = f"{self.bot.user.mention} pounces {flopped} and flops on top of them gently! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Flooop!", description = f"{ctx.message.author.mention} pounces {flopped} and flops on top of them gently!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'nap', pass_context=True, help = 'Nap on someone')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nap(self, ctx, *, napped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "zzz!", description = f"{ctx.message.author.mention} has fell asleep. Sweet Dreams!", color=0x00ff00)
            embed.set_image(url = "https://preview.redd.it/4dqsz233mwn41.png?width=640&crop=smart&auto=webp&s=4186a2874d26aef9cae47157eb348f38cdb27ab4")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "zzz!", description = f"{ctx.message.author.mention} lies against {napped} and gently drifts off..", color=0x00ff00)
        embed.set_image(url = "https://preview.redd.it/4dqsz233mwn41.png?width=640&crop=smart&auto=webp&s=4186a2874d26aef9cae47157eb348f38cdb27ab4")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'pat', pass_context=True, help = 'Give someone head pats', aliases=['pet', 'pats'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def petted(self, ctx, *, petted):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 

        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/headpats/") as resp:
                data = await resp.text()
                data = json.loads(data)
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Pat pat pat!", description = f"{self.bot.user.mention} softly pats {petted}'s head! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Pat pat pat!", description = f"{ctx.message.author.mention} softly pats {petted}'s head!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'slap', pass_context=True, help = 'Slap a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def slap(self, ctx, *, slapped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 

        embed = discord.Embed(title = "Ouch that's gotta hurt!", description = f"{ctx.message.author.mention} goes up to {slapped} and slaps them right across the face, leaving a red mark!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/0JeUUgs.png")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'throwdict', pass_context=True, help = 'Throw a dictionary at someone\'s head')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def throwdict(self, ctx, *, injured):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "No!", description = "I do not condone self-violence!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)

        embed = discord.Embed(title = "Ouch that's gotta hurt!", description = f"{ctx.message.author.mention} eyes up {injured}, before throwing a dictionary at them.", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/v4MihL9.jpg")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'bap', pass_context=True, help = 'Bap someone\'s nose with a newspaper')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def bap(self, ctx, *, bapped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "No!", description = "I do not condone self-violence!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)

        embed = discord.Embed(title = "BAD FURRY", description = f"{ctx.message.author.mention} notices {bapped} being bad, so they bap them with a newspaper.", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/CsGfqgc.png")
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'snug', pass_context=True, help = 'Snuggle a user', aliases=['snuggle'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def snug(self, ctx, *, hugged):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/hug/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Snuggle!", description = f"{self.bot.user.mention} pulls {hugged} tight to them, snuggling them close \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you snuggled with me?", description = f"Nobody ever shows me love, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Snuggle!", description = f"{ctx.message.author.mention} pulls {hugged} tight to them, snuggling them close", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    

    @commands.command(name = 'ship', pass_context=True, help = 'See how well two users get shipped together!')
    @commands.guild_only()
    @commands.cooldown(1,15, commands.BucketType.user)
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        embed = discord.Embed(title = "Ship!", description = f"{ctx.message.author.mention} has shipped {user1.mention} with {user2.mention}! They got a score of {random.randint(0,100)}", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = '8ball', pass_context=True, help = 'Ask the magic 8ball a question..')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def eightball(self, ctx, *, question):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        responses = [
			'As I see it, yes',
			'Ask again later',
			'Better not tell you now',
			'I cannot predict this right now',
			'Concentrate and ask again.',
			'Don’t count on it.',
			'It is certain.',
			'It is decidedly so.',
			'Most likely.',
			'My reply is no.',
			'My sources say no.',
			'Outlook not so good.',
			'Outlook pawsitive.',
			'Reply hazy, try again.',
			'Signs point to yes.',
			'Very doubtful.',
			'Without a doubt.',
			'Yes.',
			'Yes – definitely.',
			'You may rely on it.',
		]
        response = random.choice(responses)
        embed = discord.Embed(title = "The 8 ball has spoken!", description = f"Question: \n{question}\n\nAnswer:\n{response}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/9/90/Magic8ball.jpg")
        embed.set_footer(text = 'Wynter 2.0')
        await ctx.send(embed = embed)
    
    @commands.command(name='uwu', pass_context=True, help='OwOifys a message', aliases=['owo'])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uwu(self, ctx, *, msg):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        return await ctx.send(owoify(msg, 'uvu'))
    
    @commands.command(name = 'rp', pass_context=True, help = 'Get a random roleplay scenario!')
    @commands.guild_only()
    @commands.cooldown(1,60, commands.BucketType.user)
    async def rp(self, ctx):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        responses = [
			f'*it was a cold saturday night, {ctx.message.author.mention} was sitting by the fireplace in a lodge, having just came back from a long day of skiing...*',
			'Scenario: you\'re on a beach, relaxing on your towel as you try to get a tan. You think about a dip in the pool, but can you be bothered?',
			f'*it was a Friday night and {ctx.message.author.mention} had just gotten off from a long day at work, sitting at the bar as they ordered a vodka, someone was sitting across from them. Will they say hello?*',
			'Scenario: You and another person have a sleepover that goes wrong. What exactly goes wrong? that is up to you to decide!',
            'You get out of bed and go down to the kitchen to eat a piece of toast. Now you are standing in your kitchen, confused as to why you are here again.'
		]
        response = random.choice(responses)
        await ctx.send("At the moment, I only have 5 scenarios... here's yours! \n\n" + response)

    @commands.command(name = 'boop', pass_context=True, help = 'Boop a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def boop(self, ctx, *, booped):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/boop/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Boop!", description = f"{self.bot.user.mention} goes up to {booped} and boops them right on the nose! \n\nPS: I'm here for you :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Boop!", description = f"{ctx.message.author.mention} goes up to {booped} and boops them right on the nose!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

    @commands.command(name = 'lick', pass_context=True, help = 'Lick a user', aliases = ['licks'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def lick(self, ctx, *, licked):
        try:
            if "fm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed)  
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/lick/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Lick!", description = f"{self.bot.user.mention} pulls {licked} close to them and licks them on the cheek. Aww! \n\nPS: I'm here for you. :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Lick!", description = f"{ctx.message.author.mention} pulls {licked} close to them and licks them on the cheek. Aww!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(Fun(bot))

