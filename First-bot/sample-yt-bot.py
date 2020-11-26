from .botConfig import get_config_section
import discord

config_dict = get_config_section()

#! Step 1:Create Client (this is the actual bot)
client = discord.Client()

#! Step 2: do some stuff

@client.event #the func bellow is going to run as an event for the client
async def on_ready(): #On_ready() is discord packag function that run when bot is ready + async for parralel while looking for chn maybe there are slight delay so we need some func to wait while we do that  hence we need this
    """Send a msg to the general channel"""
    general_channel = client.get_channel(config_dict["BOT-INFO"]['general_chn_id'])  #retrieve a chn and save it in a val to use it later
    
    await general_channel.send("Hello, World!")  #wait for chn to be retieved then send msg




#! Step 3: run the client(bot) on the server
client.run(config_dict['BOT-INFO']['token'])   # pass the secret bot token