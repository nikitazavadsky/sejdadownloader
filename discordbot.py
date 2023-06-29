import discord

import os
from time import sleep

from megauploader import upload_file
from sejda import download_file

intents = discord.Intents.all()

client = discord.Client(intents = intents)
guild = discord.Guild

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    channelIDsToListen = [ 1053716403934478356, 1053716404580405332 ]

    success_flag = False
    failure_count = 0

    while not success_flag:

        if message.channel.id in channelIDsToListen:

            if str(message.content).startswith("https://www.sejda.com"):
                channel = message.channel
                print("Downloading PDF file...")

                try:
                    download_file(message.content)

                    sleep(1)

                    pdfs = [file for file in os.listdir() if file.endswith('.pdf')]

                    if not pdfs:
                        print("No PDF from Sejda")
                    else:
                        print("Uploading PDF file to Mega.nz...")
                        upload_file(pdfs[0])

                        sleep(3)

                        os.remove(pdfs[0])
                        success_flag = True
                        print("Successfully loaded file to mega!")
                except:
                    if failure_count < 3:
                        print("Something went wrong... Try again in 3 seconds")
                        sleep(3)
                    else:
                        print("More than 3 failures occured. Aborting")
                        failure_count = 0
                        break
    
client.run(TOKEN)