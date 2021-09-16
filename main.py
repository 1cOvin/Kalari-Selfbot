import discord, time, asyncio, requests
import json
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

Snow = discord.Client()
Snow = commands.Bot( description='Snow Selfbot', command_prefix=prefix, self_bot=True
)

@Snow.event
async def on_ready():
	print(f'''{Fore.BLUE}
  ██████  ███▄    █  ▒█████   █     █░
▒██    ▒  ██ ▀█   █ ▒██▒  ██▒▓█░ █ ░█░
░ ▓██▄   ▓██  ▀█ ██▒▒██░  ██▒▒█░ █ ░█ 
   ▒   ██▒▓██▒  ▐▌██▒▒██   ██░░█░ █ ░█ 
 ▒██████▒▒▒██░   ▓██░░ ████▓▒░░░██▒██▓ 
 ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  
 ░ ░▒  ░ ░░ ░░   ░ ▒░  ░ ▒ ▒░   ▒ ░ ░  
 ░  ░  ░     ░   ░ ░ ░ ░ ░ ▒    ░   ░  
       ░           ░     ░ ░      ░

{Fore.WHITE}[+] {Fore.BLUE}Welcome To #SNOWGANG
{Fore.WHITE}[+] {Fore.BLUE}Type .cmds For Commands, You Can Change The Prefix If You Want'''+Fore.RESET)


@Snow.command()
async def cmds(ctx):
    await ctx.message.delete()
    print(f'''{Fore.WHITE}[!] {Fore.BLUE}fox / Shows Random Fox Images'''+Fore.RESET)

@Snow.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    snowgang = discord.Embed(color=0x56aeec)
    snowgang.set_footer(text=f"#SNOWGANG")
    snowgang.set_image(url=r["image"])
    try: await ctx.send(embed=snowgang)
    except:
        await ctx.send(r['image'])    
            
Snow.run(token, bot=False)
