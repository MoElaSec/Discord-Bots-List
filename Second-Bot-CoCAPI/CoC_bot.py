import discord
from discord import embeds
from discord.ext import commands
import coc

#! Prepare a Dictionary from bot-info.txt
with open("bot-info.txt") as file:
    content = file.read()
    paths = content.split("\n")  # split it into lines
    info_dict = {}
    for path in paths:
        token = path.split("=")
        info_dict[token[0]] = token[1]

coc_bot_chn_id = int(info_dict["COC_BOT_CHANNEL"])
token = info_dict["TOKEN"]

coc_client = coc.login(info_dict['COC_DEV_EMAIL'], info_dict['COC_DEV_PASS'], key_count=5, key_names="Bot key", client=coc.EventsClient,)
# clan_tag = info_dict['CLAN_TAG'] # Tag of the clan that you want to follow.


#! Step 1:Create Client (this is the actual bot) 
# client = discord.Client()
bot = commands.Bot(command_prefix="!")  # ? use ! to start your commands


#! Step 2: do some stuff
##! EVENTS:

@bot.event #the func bellow is going to run as an event for the bot
async def on_ready(): #On_ready() is discord packag function that run when bot is ready + async for parralel while looking for chn maybe there are slight delay so we need some func to wait while we do that  hence we need this
    """Send a welcoming msg to the coc_bot channel"""
    coc_channel = bot.get_channel(coc_bot_chn_id)  #retrieve a chn and save it in a val to use it later

    msg = """Welcome the CoC Bot is up & Runnnig
    type !help for all the used commands
    """
    await coc_channel.send(msg)  #wait for chn to be retieved then send msg


@bot.event
async def on_disconnect():
    """Say GoodBye when the bot disconnect"""
    chn = bot.get_channel(coc_bot_chn_id)
    await chn.send("Goodbye... Diconnected")


##! COMMANDS:

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    if ctx.message.channel.id == coc_bot_chn_id:
        await ctx.message.channel.send('{0.name} joined in: {0.joined_at}'.format(member))

@bot.command(name="version")
async def version(context):
    if context.message.channel.id == coc_bot_chn_id:
        myEmbed = discord.Embed(title="Current Version",
                                description="The Bot is in it's early status!",
                                color=0x00ff00)

        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="Dec 1'st, 2020", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="moElaSec")

        await context.message.channel.send(embed=myEmbed)

@bot.command()
async def heros(ctx, player_tag):
    if ctx.message.channel.id == coc_bot_chn_id:
        player = await coc_client.get_player(player_tag)

        to_send = ""
        for hero in player.heroes:
            to_send += "{}: Lv {}/{}\n".format(str(hero), hero.level, hero.max_level)

        await ctx.send(to_send)



#! Step 3: run the client(bot) on the server
bot.run(token)  # pass the secret bot token
