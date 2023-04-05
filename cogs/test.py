import discord
from discord.ext import bridge, commands
import asyncio
import re


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @bridge.bridge_command(name= 'test', help = 'Test' , description = 'Test of the bridge commands feature')
    async def test(self, ctx: bridge.BridgeContext, *, users):
        memcount = 0
        members = []
        for user in users.split(" "):
            members.append(await ctx.guild.fetch_member(int(user.strip('<@!>'))) for mention in re.findall(r'(<@)?!?[0-9]{17,18}>?', user))
        for member in members:
            memcount = memcount+1
        await ctx.defer()
        if isinstance(ctx, bridge.BridgeExtContext):
            command_type = "Traditional (prefix-based) command"
        elif isinstance(ctx, bridge.BridgeApplicationContext):
            command_type = "Application command"
        await ctx.respond(f"This command was invoked with a(n) {command_type}. You mentioned {memcount} users in this command")
    
    

def setup(bot):
    bot.add_cog(Test(bot))