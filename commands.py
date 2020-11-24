import os
import discord

from discord.ext import commands, tasks
from dotenv import load_dotenv

from datetime import datetime

load_dotenv()

waiwaiid=211617201315119104
stlid=772395954292654090

TOKEN = os.getenv("discord_token")
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$",intents=intents)

now = datetime.now()
current_time = now.strftime("%H")
late = int(current_time) == 0 





@client.event
async def on_ready():

    checkjustin.start()
    print("I am conncted to Discord.")

@tasks.loop(minutes=20)
async def checkjustin():

    for guild in client.guilds:
    
        #print(guild.name)

        for member in guild.members:
            if late:
                if str(member.display_name)== "wklu":

                    await member.send(content = "It is already quite late, " + member.display_name + " should go to bed now.")
                    await member.move_to(None)

            #print(member.name)
   
@client.command()
async def memdbers(ctx):
    stl = await client.fetch_guild(stlid)
    members = stl.members
    print(stl.name)
    for member in members:
        await ctx.send(member.name)

    await ctx.send("done")

# if time is bewtween 00 and 06 && member name is equal to "wklu", if "wklu" try to join a voice channel, he will be moved out immediately
@client.event
async def on_voice_state_update(member, before, after):
    # print(member.display_name)
    # print(member.name)
    # print(member.id)
    # print(before)
    # print(after)
    kid = str(member.display_name)
    banname="wklu"
    if late:

        if kid==banname:
            await member.send(content = "It is already quite late, " + kid + ". You should not party anymore")
            await member.move_to(None)
        else:
            await member.send(content = "Enjoy your eveing, " + kid + ".")

@client.command()
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner_id)
    print(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title = name + " 's Discord Server Information",
        description = description,
        color = discord.Color.red()
    )

    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)



client.run(TOKEN)

