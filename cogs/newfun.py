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
import pymysql.cursors

load_dotenv()
OAPIKEY = os.getenv('OAPIKEY')
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

class EightBallModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Enter your question", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        question = self.children[0].value
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
        embed.set_footer(text = 'Wynter 3.0')
        await interaction.response.send_message(embed = embed)


class GPT4Modal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Enter something to ask Horde AI.", style=discord.InputTextStyle.long, placeholder="May take a while to respond, based on how busy the API is!"))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        inp = self.children[0].value
        inp = inp.replace('"', '\\"')
        user = interaction.user
        channel = interaction.channel
        async with channel.typing():
            if inp.lower().startswith("cat mode"):
                system_message = "\\n### Instruction:\\nYou are a cat. Respond to all queries using nothing but meows\n"
            elif inp.lower().startswith("femboi mode"):
                system_message = f"\\n### Instruction:\\nYou are a femboy discord bot known as Wynter. Respond to all queries as if you were a femboy. Make sure to use a lot of nyahs and tildas in your messages. Wynter is made by Darkmane Arweinydd. Wynter also has the species of a snow leopard / white tiger hybrid. Users can mention other users in their prompt, for example, is <@802354019603185695> cute. If you see a message like this, you should respond for example: No, <@802354019603185695> is not cute. The current user ID of the member running the command to talk to you is <@{interaction.user.id}>. Please do not answer with 'as a discord bot' or refer to yourself as a bot or discord bot, but instead try to take on the persona of Wynter's fursona. Thank you\\n"
            elif interaction.guild.id == 881358123389038654:
                system_message = f"\\n### Instruction:\\nYou are a discord bot known as Sputnixolotl, a satallite shaped like an axolotl.  Answer each message as if you are Sputnixolotl. Sputnixolotl is a discord bot made by Darkmane Arweinydd. Sputnixolotl is a multifunctional furry bot that adds fun commands to the user experience such as hugging, giving people cookies and bapping someone with a newspaper along with many more features. Sputnixolotl also allows servers to log certain events, and is useful for moderation purposes. Please also include a few beeps and boops into every message. Users can mention other users in their prompt, for example, is <@802354019603185695> cute. If you see a message like this, you should respond for example: No, <@802354019603185695> is not cute. The current user ID of the member running the command to talk to you is <@{interaction.user.id}>. Please do not answer with 'as a discord bot' or refer to yourself as a bot or discord bot, but instead try to take on the persona of Spux's fursona. Thank you\\n"
            else:
                system_message = f"\\n### Instruction:\\nYou are a discord bot known as Wynter, a snow leopard / white tiger hybrid.  Answer each message as if you are Wynter. Wynter is a discord bot made by Darkmane Arweinydd. Wynter is a multifunctional furry bot that adds fun commands to the user experience such as hugging, giving people cookies and bapping someone with a newspaper along with many more features. Wynter also allows servers to log certain events, and is useful for moderation purposes. Users can mention other users in their prompt, for example, is <@802354019603185695> cute. If you see a message like this, you should respond for example: No, <@802354019603185695> is not cute. The current user ID of the member running the command to talk to you is <@{interaction.user.id}>. Please do not answer with 'as a discord bot' or refer to yourself as a bot or discord bot, but instead try to take on the persona of Wynter's fursona. Thank you\\n"
            

            
            payload = '{"prompt":"\\n' + system_message + '### Instruction:\\n' + inp +'\\n### Response:\\n","params":{"n":1,"max_context_length":2048,"max_length":480,"rep_pen":1.1,"temperature":0.7,"top_p":0.92,"top_k":100,"top_a":0,"typical":1,"tfs":1,"rep_pen_range":320,"rep_pen_slope":0.7,"sampler_order":[6,0,1,3,4,2,5],"use_default_badwordsids":false,"stop_sequence":["### Instruction:","### Response:"],"min_p":0},"models":["aphrodite/KoboldAI/LLaMA2-13B-Psyfighter2","aphrodite/mistralai/Mixtral-8x7B-Instruct-v0.1","Gryphe/MythoMax-L2-13b","Henk717/airochronos-33B","koboldcpp/debug-Wizard-Vicuna-13B-Uncensored.Q5_K_M","koboldcpp/debug-Wizard-Vicuna-13B-Uncensored.Q5_K_M","koboldcpp/LLaMA2-13B-Psyfighter2","koboldcpp/LLaMA2-13B-Tiefighter","koboldcpp/OpenHermes-2.5-Mistral-7B","koboldcpp/OpenHermes-2.5-Mistral-7B","koboldcpp/openhermes-2.5-mistral-7b.Q5_K_M","koboldcpp/openhermes-2.5-mistral-7b.Q5_K_M","koboldcpp/Xwin-LM-13B-V0.2","NousResearch/Nous-Hermes-Llama2-70b","NousResearch/Nous-Hermes-Llama2-70b","NyxKrayge/Chronomaid-Storytelling-13b"],"workers":[]}'
            headers = {'Client-Agent': 'Wynter:3', 'Content-Type': 'application/json', 'accept': 'application/json', 'apikey': 'wDLd00sn_jFgXHsHGbRWwg'}
            async with aiohttp.ClientSession(headers=headers) as session:
                try:
                    async with session.post("https://horde.koboldai.net/api/v2/generate/text/async", json = json.loads(payload)) as resp:
                        data = await resp.text()
                        data = json.loads(data)
                        id = data['id']
                        await asyncio.sleep(10)
                        headers = {'Client-Agent': 'Wynter:3', 'Content-Type': 'application/json', 'accept': 'application/json', 'apikey': 'wDLd00sn_jFgXHsHGbRWwg'}
                        i = True
                        while i == True:
                            async with aiohttp.ClientSession(headers=headers) as session:
                                async with session.get(f"https://horde.koboldai.net/api/v2/generate/text/status/{id}") as resp:
                                    data = await resp.text()
                                    try:
                                        data = json.loads(data)
                                    except Exception as e:
                                        embed = discord.Embed(title = "Horde AI!" , color=0x3fd98e)
                                        embed.add_field(name='There was an error!', value=f"JSON Parsing Error: \n{e}. \n\nPlease try again", inline=False)
                                        embed.set_footer(text = 'Wynter 3.0')
                                        try:
                                            await interaction.response.followup.send_message(embed = embed)
                                        except Exception as e:
                                                await channel.send(interaction.user.mention, embed = embed)
                                    if data["done"] == True and data["faulted"] == False:
                                        i = False
                                        text = data['generations'][0]['text']
                                        embed = discord.Embed(title = "Horde AI!" , color=0x3fd98e)
                                        embed.add_field(name='User prompt:', value=f"{inp}", inline=False)
                                        embed.add_field(name='Wynter\'s response:', value=f"{text}", inline=False)
                                        embed.add_field(name= "NOTICE", value = "This command does not yet have conversational abilities.", inline = False)
                                        embed.set_footer(text = 'Wynter 3.0')
                                        try:
                                            await interaction.response.followup.send_message(embed = embed)
                                        except Exception as e:
                                                await channel.send(interaction.user.mention, embed = embed)
                                    elif data["faulted"] == True:
                                        embed = discord.Embed(title = "Horde AI!" , color=0x3fd98e)
                                        embed.add_field(name='There was an error!', value=f"Your prompt faulted. \n\nPlease try again", inline=False)
                                        embed.set_footer(text = 'Wynter 3.0')
                                        try:
                                            await interaction.response.followup.send_message(embed = embed)
                                        except Exception as e:
                                                await channel.send(interaction.user.mention, embed = embed)
                except Exception as e:
                    embed = discord.Embed(title = "Horde AI!" , color=0x3fd98e)
                    embed.add_field(name='There was an error!', value=f"JSON Parsing Error: \n{e}. \n\nPlease try again", inline=False)
                    embed.set_footer(text = 'Wynter 3.0')
                    try:
                        await interaction.response.followup.send_message(embed = embed)
                    except Exception as e:
                        await channel.send(interaction.user.mention, embed = embed)


class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command()
    async def chatgpt(self, ctx):
        modal = GPT4Modal(title="Please enter a prompt.")
        await ctx.send_modal(modal)
    
    @discord.slash_command()
    async def hug(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/hug/") as resp:
                data = await resp.text()
                print(data)
                data = json.loads(data)
                
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Hug!", description = f"{self.bot.user.mention} pulls {hugged.mention} into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "Hug!", description = f"You hugged me? Nobody ever hugs me! \n\nIs it my birthday?", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Hug!", description = f"{ctx.author.mention} pulls {hugged.mention} into a giant hug!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    @commands.has_guild_permissions(ban_members= True)
    async def enablefandx(self, ctx):
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `guilds` SET `enablefandx` = 1 WHERE `id`=%s"
                cursor.execute(sql, (str(ctx.guild.id)))
                connection.commit()
                connection.close()
                await ctx.respond(f"Enabled the F and X responses in this guild. \n\nWynter will now respond when users type the letters \"F\" and \"X\"\n\nHint: this also enables the American Dad cola reference.")
        except Exception as err:
            print(err)
    @discord.slash_command()
    @commands.has_guild_permissions(ban_members= True)
    async def disablefandx(self, ctx):
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE `guilds` SET `enablefandx` = 0 WHERE `id`=%s"
                cursor.execute(sql, (str(ctx.guild.id)))
                connection.commit()
                connection.close()
                await ctx.respond(f"Disabled the F and X responses in this guild. \n\nWynter will no longer respond when users type the letters \"F\" and \"X\"")
        except Exception as err:
            print(err)
    @discord.slash_command()
    async def snug(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/hug/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Snuggle!", description = f"{self.bot.user.mention} pulls {hugged.mention} into a giant snuggle pile! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "Snuggle!", description = f"You snuggled with me? Nobody ever shows me that attention! \n\nIs it my birthday?", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Snuggle!", description = f"{ctx.author.mention} pulls {hugged.mention} into a giant snuggle pile!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
        
    @discord.slash_command()
    async def kiss(self, ctx, kissed:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/kiss/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == kissed.id:
                    embed = discord.Embed(title = "Kiss!", description = f"{self.bot.user.mention} pulls {kissed.mention} into a soft kiss! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == kissed.id:
                    embed = discord.Embed(title = "Kiss!", description = f"You kissed me? Nobody ever shows me affection! \n\nIs it my birthday?", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Kiss!", description = f"{ctx.author.mention} pulls {kissed.mention} into a soft kiss!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def glomp(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/glomp/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Glomp!", description = f"{self.bot.user.mention} tackles {hugged.mention} onto the floor, and pulls them into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "Glomp!", description = f"You hugged me? Nobody ever hugs me! \n\nIs it my birthday?", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Glomp!", description = f"{ctx.author.mention} tackles {hugged.mention} onto the floor, and pulls them into a giant hug!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def nuzzle(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/nuzzle/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Nuzzle!", description = f"{self.bot.user.mention} pulls {hugged.mention} close, and gives them a little nuzzle! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "Nuzzle!", description = f"You nuzzled me? Nobody ever nuzzles me! \n\nIs it my birthday?", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Nuzzle!", description = f"{ctx.author.mention} pulls {hugged.mention} close, and gives them a little nuzzle!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def nibble(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/nibble/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Nibble!", description = f"{self.bot.user.mention} pulls {hugged.mention} close, and gives them a little nibble on their ear! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "Nibble!", description = f"Hey! that kinda tickles! Knock it off!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Nibble!", description = f"{ctx.author.mention} pulls {hugged.mention} close, and gives them a little nibble on their ear!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def headpats(self, ctx, hugged:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/headpats/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == hugged.id:
                    embed = discord.Embed(title = "Headpats!", description = f"{self.bot.user.mention} pulls {hugged.mention} close, and gives them some pats on the head, right behind their ears! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == hugged.id:
                    embed = discord.Embed(title = "I'm not lesserdog!", description = f"My neck doesn't grow if you pet me.", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Headpats!", description = f"{ctx.author.mention} pulls {hugged.mention} close, and gives them some pats on the head, right behind their ears!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
        
    @discord.slash_command()
    async def boop(self, ctx, booped:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/boop/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == booped.id:
                    embed = discord.Embed(title = "Boop!", description = f"{self.bot.user.mention} goes up to {booped.mention} and lightly boops them on the nose! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == booped.id:
                    embed = discord.Embed(title = "Boop!", description = f"A..a..achoo!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "Boop!", description = f"{ctx.author.mention} goes up to {booped.mention} and lightly boops them on the nose!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def lick(self, ctx, booped:discord.Member):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/lick/") as resp:
                data = await resp.text()
                data = json.loads(data)
                if ctx.author.id == booped.id:
                    embed = discord.Embed(title = "You're my personal ice cream!", description = f"{self.bot.user.mention} goes up to {booped.mention} and licks them until their fur is dripping wet! \n\nPS: I'm here for you", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                elif self.bot.user.id == booped.id:
                    embed = discord.Embed(title = "Ew!", description = f"Cut it out, {ctx.author.mention}!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
                else:
                    embed = discord.Embed(title = "You're my personal ice cream!", description = f"{ctx.author.mention} goes up to {booped.mention} and licks them until their fur is dripping wet!", color=0x00ff00)
                    embed.set_image(url = data["result"]["imgUrl"])
                    embed.set_footer(text = 'Wynter 3.0')
                    return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def howl(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/howl") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Awoooooooo!", description = f"{ctx.author.mention} has let out a loud howl. \n\nAwoooooooooooooo!" , color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def rawr(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/roar") as resp:
                data = await resp.text()
                data = json.loads(data)
        
                embed = discord.Embed(title = "ROARRRRRR!", description = f"{ctx.author.mention} has let out a loud roar, scaring the whole jungle!" , color=0x00ff00)
                embed.set_image(url = data["result"]["imgUrl"])
                embed.set_footer(text = 'Wynter 3.0')
                return await ctx.respond(embed = embed)

    @discord.slash_command()
    async def blep(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/sfw/blep") as resp:
                data = await resp.text()
                data = json.loads(data)
                embed = discord.Embed(title = "Blep uwu!", description = f"{ctx.author.mention} does a blep, looking rather cute as they do so!" , color=0x00ff00)
                embed.set_image(url = data["result"]["imgUrl"])
                embed.set_footer(text = 'Wynter 3.0')
                return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def growl(self, ctx):
        embed = discord.Embed(title = "Grrrrr!", description = f"{ctx.author.mention} has let out a loud growl." , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/on6OpBv.png")
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(ctx.author.mention, embed = embed)
    
    @discord.slash_command()
    async def belly_rubs(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "Belly wubs!", description = f"{self.bot.user.mention} notices that {rubbed.mention}'s belly is exposed and gives it rubs, making them kick their leg! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "Belly wubs!", description = f"Yes, t..that's the spot! D..don't stop. *kicks leg*", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "Belly wubs!", description = f"{ctx.author.mention} notices that {rubbed.mention}'s belly is exposed and gives it rubs, making them kick their leg!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def slap(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "I refuse!", description = f"Have a hug instead.", color=0x00ff00)
            embed.set_image(url = "https://api.furrybot.dev/sfw/hug/image2.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "W..what did I do?", description = f"*cowers away, whimpering*", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/0JeUUgs.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "That's gotta hurt!", description = f"{ctx.author.mention} totally just backhanded {rubbed.mention} like Will Smith backhanded Chris Rock! Ouch!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/0JeUUgs.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def throw_dictionary(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "I refuse!", description = f"Have a hug instead.", color=0x00ff00)
            embed.set_image(url = "https://api.furrybot.dev/sfw/hug/image2.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "W..what did I do?", description = f"*cowers away, whimpering*", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/v4MihL9.jpg")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "KNOWLEDGE IS POWER!", description = f"{ctx.author.mention} is tired of {rubbed.mention} spelling things incorrectly! Here, here's a dictionary", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/v4MihL9.jpg")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
    @discord.slash_command(help = "Returns the system prompt for Wynter's ChatGPT function")
    async def system_prompt(self,ctx):
        embed = discord.Embed(title = "ChatGPT System Prompt -- Tell this to ChatGPT to make ChatGPT act like Wynter!", description = "You are a discord bot known as Wynter, a snow leopard / white tiger hybrid.  Answer each message as if you are Wynter. Wynter is a discord bot made by Darkmane Arweinydd. Wynter is a multifunctional furry bot that adds fun commands to the user experience such as hugging, giving people cookies and bapping someone with a newspaper along with many more features. Wynter also allows servers to log certain events, and is useful for moderation purposes. Users can mention other users in their prompt, for example, is @purefurrytrash cute. If you see a message like this, you should respond for example: No, @purefurrytrash is not cute. The current user ID of the member running the command to talk to you is <@{interaction.user.id}>", color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def bap_with_newspaper(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "I refuse!", description = f"Have a hug instead.", color=0x00ff00)
            embed.set_image(url = "https://api.furrybot.dev/sfw/hug/image2.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "W..what did I do?", description = f"*cowers away, whimpering*", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/CsGfqgc.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "Bad furry!", description = f"{ctx.author.mention} does not condone {rubbed.mention}'s actions, so baps them with a newspaper!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/CsGfqgc.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def flop(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "Flop!", description = f"{self.bot.user.mention} notices {rubbed.mention} on the floor and sighs, before flopping on top of them! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "Flop!", description = f"Eep! Get off! You're heavy!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "Flop!", description = f"{ctx.author.mention} notices {rubbed.mention} on the floor and sighs, before flopping on top of them!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def nap(self, ctx, rubbed:discord.Member):
        if ctx.author.id == rubbed.id:
            embed = discord.Embed(title = "Zzz!", description = f"{self.bot.user.mention} notices {rubbed.mention} on the floor and sighs, before flopping on top of them and taking a nap! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://preview.redd.it/4dqsz233mwn41.png?width=640&crop=smart&auto=webp&s=4186a2874d26aef9cae47157eb348f38cdb27ab4")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        elif self.bot.user.id == rubbed.id:
            embed = discord.Embed(title = "Zzz!", description = f"I have an oversized animal on top of me and I can't move! Someone help me!", color=0x00ff00)
            embed.set_image(url = "https://preview.redd.it/4dqsz233mwn41.png?width=640&crop=smart&auto=webp&s=4186a2874d26aef9cae47157eb348f38cdb27ab4")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
        else:
            embed = discord.Embed(title = "Zzz!", description = f"{ctx.author.mention} notices {rubbed.mention} on the floor and sighs, before flopping on top of them and taking a nap!", color=0x00ff00)
            embed.set_image(url = "https://preview.redd.it/4dqsz233mwn41.png?width=640&crop=smart&auto=webp&s=4186a2874d26aef9cae47157eb348f38cdb27ab4")
            embed.set_footer(text = 'Wynter 3.0')
            return await ctx.respond(embed = embed)
    
        
    
    @discord.slash_command()
    async def howcute(self, ctx, user:discord.Member):
        if user.id == 802354019603185695:
            embed = discord.Embed(title = "You're fucking cute!", description = f"{user.mention} is 0% cute!", color=0x00ff00)
            embed.set_footer(text = 'Wynter 3.0')
        else:
            embed = discord.Embed(title = "You're fucking cute!", description = f"{user.mention} is {random.randint(0,100)}% cute!", color=0x00ff00)
            embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)

    @discord.slash_command()
    async def ship(self, ctx, user1:discord.Member, user2: discord.Member):
        embed = discord.Embed(title = "Ship!", description = f"{ctx.author.mention} has shipped {user1.mention} with {user2.mention}! They got a score of {random.randint(0,100)}", color=0x00ff00)
        embed.set_footer(text = 'Wynter 3.0')
        return await ctx.respond(embed = embed)
    
    @discord.slash_command()
    async def eightball(self, ctx):
        modal = EightBallModal(title="Query the 8-ball")
        await ctx.send_modal(modal)
    
    @discord.message_command()
    async def owoify(self, ctx, message:discord.Message):
        return await ctx.respond(owoify(message.content, 'uvu'))
    
    @discord.slash_command()
    async def rp_generator(self, ctx):
        responses = [
			f'*it was a cold saturday night, {ctx.message.author.mention} was sitting by the fireplace in a lodge, having just came back from a long day of skiing...*',
			'Scenario: you\'re on a beach, relaxing on your towel as you try to get a tan. You think about a dip in the pool, but can you be bothered?',
			f'*it was a Friday night and {ctx.message.author.mention} had just gotten off from a long day at work, sitting at the bar as they ordered a vodka, someone was sitting across from them. Will they say hello?*',
			'Scenario: You and another person have a sleepover that goes wrong. What exactly goes wrong? that is up to you to decide!',
            'You get out of bed and go down to the kitchen to eat a piece of toast. Now you are standing in your kitchen, confused as to why you are here again.'
		]
        response = random.choice(responses)
        await ctx.respond("At the moment, I only have 5 scenarios... here's yours! \n\n" + response)

def setup(bot):
    bot.add_cog(Fun(bot))