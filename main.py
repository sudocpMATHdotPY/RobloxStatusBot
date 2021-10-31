import os
import discord
from discord.ext import commands
import requests
import random
from replit import db
from mechanize import Browser
client = discord.Client()
global compare
compare = None
compare = db["web"]
Title = "boblox 44"
desc = "Roblox notifies"
br = Browser()
headers = {'Accept-Encoding': 'identity'}
link = "https://docs.google.com/document/d/1eG-kNy4pCZX2DDqQoNTQb7Nlx_ViRAnfKnrf0H-Sn3E/edit?usp=sharing"
#css = input("type: ")
#if css == "math":
async def alert(message):
    for server in client.guilds:
        print(server)
        for channel in server.text_channels:
            try:
                await channel.send(message)
            except Exception:
                continue
            else:
                break
def get(url):
  try:
      r = requests.get(url, headers=headers)
      return r.text
  except:
       return False
def check(url):
  try:
       r = requests.get(url, timeout=10)
       if r.status_code == 200:
         br.open(url)
         return br.title()
       elif r.status_code == 503:
         return("Roblox Maintenance")
       else:
         return str(r.status_code)
  except:
       return False
files = ["1.gif", "meme2.gif", "meme3.gif", "meme4.gif"]

@client.event

async def on_message(message):
  msg = message.content
  mess = msg.split()
  global link
  if msg.startswith("$roblox"):
    get = check("https://roblox.com")
    if get == "Roblox Maintenance":
      await message.channel.send("Roblox is down for Maintenance")
    else:
      await message.channel.send(get)
          #await message.channel.send(file=discord.File('link.png'))
    
@client.event

async def on_ready():
  global compare
  print("ready")
  while True:
    current = get("https://status.roblox.com")
    if current != compare:
      await alert("https://status.roblox.com has changed! check it out for the latest news!")
      gete = check("https://roblox.com")
      if gete == "Roblox Maintenance":
        await alert("Roblox.com is down for maintenance")
      else:
        await alert("Roblox.com is up!")
    compare = current
    db["web"] = compare


 
client.run('THIS IS A BOT TOKEN')
