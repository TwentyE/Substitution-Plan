# Imports
from logging import error
from Vertretungs_data import *
import discord
from discord.ext import commands
import json
import random
import asyncio


# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    version = data["version"]
    client_id = data["client_id"]

# Get data.py
# with open ("data.py", "r") as data:


# Intents
intents = discord.Intents.default()

bot = commands.Bot(
    intents=intents, command_prefix=prefix, help_command=None)

# On guild join


@discord.ext.commands.Cog.listener()
async def on_guild_join(self, guild: discord.Guild, message):
    welcome_message = (
        "Hello, thanks for using the vpBot! The whole project is avalible on GitHub!")
    await message.channel.send(welcome_message)

# On Ready


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)

# Discord rich presence (rpc)


async def rpc():
    '''
    This function creates a discord rpc and randomly displays one of the items in all_rpcs
    '''
    await bot.wait_until_ready()

    all_rpcs = [f"{bot.command_prefix}help",
                f"Current version of the vpBot is {version}", "The Bot-Prefix is: ?"]

    while not bot.is_closed():
        active_rpc = random.choice(all_rpcs)
        await bot.change_presence(activity=discord.Game(name=active_rpc))
        await asyncio.sleep(7)

# Vertretungsplan embed


@bot.command(aliases=['vp', 'vertretungsplan'])
async def vertretung(ctx):
    '''
    This function adds the "vertretung" command, with wich you can let the vpBot send an embed with the newest substitution-plan of your class.
    '''
    vertretung_embed = discord.Embed(
        title=f'Vertretungsplan', description="Hier steht der Vertretungsplan für die Klasse 10C1", color=16614505)

    # Setting an author name and picture for the embed
    vertretung_embed.set_author(
        name="Vertretungs-Bot", icon_url="https://cdn.discordapp.com/attachments/820979957240037396/897910242698989578/news.png")
 
    # Setting a thumbnail for the embed
    vertretung_embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/820979957240037396/897924057822031912/unknown.png")

    vertretung_embed.add_field(
        name="Der Vertretungsplan:", value=output
    )

    # Setting a footer for the embed
    vertretung_embed.set_footer(
        text="This is a project brought to you by TwentyE, consider joining my Discord server")

    await ctx.send(embed=vertretung_embed)

# Conference command


@bot.command()
async def conference(message):
    """
    Sends a funny picture of a cat
    """
    conference_message = "https://cdn.discordapp.com/attachments/820979957240037396/898317433402720257/camera-cats-cute-funny-conference-call-7933178112.png"
    await message.channel.send(conference_message)

# Purge command


@bot.command(aliases=['c'])
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['clear all', 'ca'])
async def clear_all(ctx,):
    await ctx.channel.purge(limit=999999)

# ERRORS
@clear.error
async def clearing_error(ctx):
    await ctx.channel.send("Please insert a number of messages that you want to be deleted.")

@bot.event
async def CommandNotFound(Exception, ctx):
    await ctx.send("This command does not exist. Type ?help to see all existing commands.")

# ATTRIBUTIONS
# Icons made by https://www.flaticon.com/authors/vectors-market https://www.flaticon.com/

bot.loop.create_task(rpc())
bot.run(token)
