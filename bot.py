from http import client
import re
from turtle import title
import discord
from main import search

token = "OTk4OTc2MTg0MTIzNjU4Mzky.GqMYIk.hzkHSJjezlA9nBLPqHrfgE-FUtfGtGS9T1dHpc"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.split(' ')[0] == "!stockx":
        query = message.content.replace('!stockx', '')

        item = search(query)

        embed = discord.Embed(
            title = item['title'],
            url = 'https://stockx.com/' + item['shortDescription']
        )

        embed.set_thumbnail(
            url = item['media']['imageUrl']
        )
        
        embed.add_field(
            name = 'Colorway',
            value = item['colorway']
        )

        embed.add_field(
            name = 'Style ID',
            value = item['styleId']
        )

        embed.add_field(
            name = 'Release Date',
            value = item['releaseDate']
        )

        embed.add_field(
            name = 'Average Price',
            value = item['market']['averageDeadstockPrice']
        )

        await message.channel.send(embed=embed)
    

client.run(token)  

