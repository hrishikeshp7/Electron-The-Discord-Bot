import discord
from discord.ext import commands
from discord.ext.commands.core import command
import requests
from bs4 import BeautifulSoup
import wikipedia
import pyjokes
import qrcode
from PIL import Image
from io import BytesIO
import time
import datetime
import io
from PyDictionary import PyDictionary
import news_python
import bitlyshortener
import os



client = commands.Bot(command_prefix="h", intents = discord.Intents.all())

client.remove_command("help")

@client.command()
async def on_ready():
    print(Time)

@client.command()
async def p(ctx, *, message, user : discord.Member = None):
    command = message.lower()
    if "help" in command:
        embed = discord.Embed(title='Electron, a Discord Bot')
                         

        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Electron_Software_Framework_Logo.svg/1200px-Electron_Software_Framework_Logo.svg.png')

        embed.set_author(name="Electron", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Electron_Software_Framework_Logo.svg/1200px-Electron_Software_Framework_Logo.svg.png")

        embed.add_field(name="What Electron can do?", value="> Provide Results From Wikipedia.\n> Provide the URL For Your Query from YouTube and YouTube Music.\n> Provide the weather Forecast From your Country/State/City.\n> Tell jokes When You're Bored.\n> Convert Text To QR Code.\n> And more stuffs...", inline=False)

        embed.add_field(name="Commands", value="> `hp help`\n  Use 'hpm' and ask your Queries!...", inline=False)

      

        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))

        await ctx.channel.send(embed=embed)

    elif "hello" in command:
        em=discord.Embed(title="Hello",color=discord.Color.red())
        await ctx.send(embed=em)

    elif "hi" in command:
        em=discord.Embed(title="Hi",color=discord.Color.blue())
        await ctx.send(embed=em)

    elif "born" in command:
        em=discord.Embed(title="6 May 2021",color=discord.Color.blue())
        await ctx.send(embed=em)

    elif "weather" in command:
        url = "https://www.google.com/search?q=weather " + message
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
        pos = strd.find('Wind')
        other_data = strd[pos:]
        result = "The Temperature was currently " + temp.replace("C", "celcius") + ", The Sky was now " + sky + " " + other_data
        em=discord.Embed(title=result,color=discord.Color.red())
        await ctx.send(embed=em)

    elif "yt" in command:
        url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
        GET_content = requests.get(url)
        Play_Content = GET_content.text
        await ctx.send(Play_Content)

    elif "music" in command:
        url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message + " Album - Topic"
        GET_content = requests.get(url)
        Yt_to_YTM = GET_content.text
        Music_URL = Yt_to_YTM.replace("www.", "music.")
        await ctx.send(Music_URL)

    elif "time" in command:
        result = Time
        em=discord.Embed(title="Time is Currently",color=discord.Color.red(), description=result)
        await ctx.send(embed=em)

    elif "date" in command:
        result = datetime.date.today()
        em=discord.Embed(title="Today's Date:",color=discord.Color.red(), description=result)
        await ctx.send(embed=em)


    elif "who is" in command:
        try:
            result_from_wiki = wikipedia.summary(str(message.replace("who is ", "")), sentences=5)
            em=discord.Embed(title=message,color=discord.Color.red(), description=result_from_wiki)
            await ctx.send(embed=em)
        except Exception as e:
            print(e)
            url = "https://en.wikipedia.org/wiki/" + message.replace(" ", "_").replace("is", "")
            await ctx.send(url)

    elif "solve" in command:
        sum =  eval(message.replace("this", "").replace("solve", ""))
        embed=discord.Embed(title="Query : " + message + "\nAnswer : ",description=sum)
        await ctx.send(embed=embed)

    elif "joke" in command:
        random_joke = pyjokes.get_joke()
        em=discord.Embed(title=random_joke,color=discord.Color.red())
        await ctx.send(embed=em)

    elif "favicon" in command:
        url = 'https://www.google.com/s2/favicons?domain=' + message.replace("favicon ", "")
        await ctx.send(url)
    elif "repo" in command:
        url = 'https://api.github.com/repos/' + message.replace("repo info ", "")
        GET_content = requests.get(url)
        with io.open("filepath", "w", encoding="utf-8") as File:
            result = File.write(str(GET_content.text))
        await ctx.send(file=discord.File("filepath"))
    elif "yt" in command:
        url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
        GET_content = requests.get(url)
        Play_Content = GET_content.text
        await ctx.send(Play_Content)

    elif "qr" in command:
        QRFile = "filepath"
        img = qrcode.make(message)
        img.save(QRFile)
        await ctx.send(file=discord.File(QRFile))

    elif "wanted" in command:
        if user == None:
            user = ctx.author
        wanted = Image.open("filepath")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        #317 369    # 733 921
        pfp = pfp.resize((733,921))
        wanted.paste(pfp, (317,369))
        wanted.save("filepath")
        await ctx.send(file=discord.File("filepath"))

    elif "meaning" in command:
        message = message.replace("meaning of ", "")
        dictionary = PyDictionary()
        Dic = dictionary.meaning(message)
        DicList = list(Dic['Noun'])
        em=discord.Embed(title=message,color=discord.Color.red(), description=DicList[0])
        await ctx.send(embed=em)

    elif "news" in command:
        news = news_python.Global(key= "token")
        news_content = news.get_news(query="message")
        await ctx.send(news_content.url)

    elif "short" in command:
        tokens_pool = ['token']  
        shortener = bitlyshortener.Shortener(tokens=tokens_pool, max_cache_size=256)
        long_urls = [message]
        alt = shortener.shorten_urls(long_urls)
        await ctx.send(shortener.usage())

    elif "google" in command:
        glink = "https://google.com/search?q="
        await ctx.send(glink)

@client.command()
async def preverse(ctx,*,msg):
  m= msg[::-1]
  await ctx.send(m)
        
        

        

    

client.run(os.getenv("Token"))
