from re import M
import aiohttp
import asyncio
import mimetypes
import json
import discord
from discord.ext import commands, bridge

class NSFW(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'gay', pass_context=True, help = 'Get a gay yiff image', description='Get a gay yiff image')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def gay(self, ctx):
        try:
            if "nm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/nsfw/yiff/gay/") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Oh murr!", description = "I hope you enjoy this image ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.respond(embed = embed)
    
    @commands.command(name = 'blowjob', pass_context=True, help = 'Get a gay blowjob image', description = 'Get a gay blowjob image')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def blowjob(self, ctx):
        try:
            if "nm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/nsfw/yiff/blowjob/") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Oh murr!", description = "I hope you enjoy this image ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.respond(embed = embed)
    
    @commands.command(name = 'deeznuts', pass_context=True, help = 'deeznuts. Ha! Gottem!', description= 'deeznuts. Ha! Gottem!')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nutz(self, ctx):
        return await ctx.respond("HA! GOTTEM!")
    
    @commands.command(name = 'yiff', pass_context=True, help = 'Yiff someone else', description= 'Yiff someone else')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def yiff(self, ctx, users: commands.Greedy[discord.Member]):
        members = 0
        for user in users:
            members = members +1
        users = ", ".join([str(i.mention) for i in users if i])
        try:
            if "nm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        if members > 3:
                embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
                embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
                embed.set_footer(text = 'Wynter 2.0')
                return await ctx.respond(ctx.author.mention, embed = embed) 
                
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/nsfw/yiff/gay/") as resp:
                data = await resp.text()
                data = json.loads(data)
            
        if ctx.author in ctx.message.mentions:
            embed = discord.Embed(title = "Hope you like it rough!", description = f"{self.bot.user.mention} pulls {users} on the bed, whips out their massive hybrid cock, and starts to yiff them like there's no tomorrow. \n\nGood luck walking tomorrow ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)
            
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you wanna fuck me?", description = f"I'm surprised, {ctx.author.mention}.. Is a bot really worth fucking? \n\nOkay then, top or bottom? ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)

        embed = discord.Embed(title = "Hope you like it rough!", description = f"{ctx.author.mention} pulls {users} on the bed and starts to yiff them like there's no tomorrow. \n\nGood luck walking tomorrow, guys ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.respond(embed = embed)


    
    @commands.command(name = 'suck', pass_context=True, help = 'Suck off someone else', description = 'Suck off someone else')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def suck(self, ctx, *, users):
        try:
            if "nm:0" in ctx.channel.topic:
                return
        except Exception as e:
            print(e)
        
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(ctx.author.mention, embed = embed) 
                
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrybot.dev/nsfw/yiff/blowjob/") as resp:
                data = await resp.text()
                data = json.loads(data)
            
        if ctx.author in ctx.message.mentions:
            embed = discord.Embed(title = "Down the hatch!", description = f"{self.bot.user.mention} lays on the bed, whilst {ctx.author.mention} sucks them off. Such a good slut ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.respond(embed = embed)
            
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you wanna fuck me?", description = f"I'm surprised, {ctx.author.mention}.. Is a bot really worth sucking off? \n\nOkay then, I'm game ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hope you like it rough!", description = f"{users} lays on the bed, whilst {ctx.author.mention} sucks them off. Such a good slut ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(NSFW(bot))