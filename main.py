import discord 
from discord.ext import commands
import requests
#bot stuff
BOT_TOKEN="nuh_uh"
BOT_CHANNEL_old = 1290021825018986557
BOT_CHANNEL = 1290041727654297610
ROLE_NAME = "smrkec mleko"
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

#youtube stuff
API_KEY = 'not_leaking_private_information'
CHANNEL_ID = 'UCZwXyjPPXOAIO0FlsJUKdTQ'
VIDAKOVIC_CHANNEL_ID = "UCKJpQyy-r0VjkjAfXeKtNRw"
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
def get_latest_video(api_key, channel_id):
    params = {
        'part': 'snippet',
        'channelId': channel_id,
        'order': 'date',
        'maxResults': 1,
        'type': 'video',
        'key': api_key
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            latest_video = data['items'][0]['snippet']
            video_id = data['items'][0]['id']['videoId']
            title = latest_video['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            return(f"[{title}]({video_url})")
        else:
            return("Keine video gefunden, nuh uh")
    else:
        return(f"Plačite svoje mlekarje (niam pojma ka to pomen): {response.status_code}")



#BOT INIT MESSAGE
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    channel = bot.get_channel(BOT_CHANNEL)
    #await channel.send(f"Logged in as {bot.user}")

# Assign the "jagodno mleko" role to new members
@bot.event
async def on_member_join(member):
    guild = member.guild
    role = discord.utils.get(guild.roles, name=ROLE_NAME)
    if role is not None:
        await member.add_roles(role)
        print(f"Assigned {ROLE_NAME} role to {member.name}")
    else:
        print(f"Role '{ROLE_NAME}' not found.")

# Command example
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, i love iMleko")

@bot.command()
async def website(ctx):
    await ctx.send("[iMleko](https://imleko.si/)")

@bot.command()
async def youtube(ctx):
    await ctx.send("[iMleko - youtube](https://youtube.com/@imleko)")

@bot.command()
async def upload(ctx):
    try:
        await ctx.send(get_latest_video(API_KEY, CHANNEL_ID))
    except:
        await ctx.send("Plači mi če hočš da še kaj delam!!!")

@bot.command()
async def vidakovic(ctx):
    try:
        await ctx.send(get_latest_video(API_KEY, VIDAKOVIC_CHANNEL_ID))
    except:
        await ctx.send("Revolucija!!!! Nema mleka!!!")

@bot.command()
async def bestmilk(ctx):
    await ctx.send("iMleko!!! 🗣️🗣️🔥🔥")

bot.run(BOT_TOKEN)
