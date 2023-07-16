import discord
from dotenv import load_dotenv
import os
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.command
    async def mahjong(ctx):
        file = discord.File("mahjong_tiles.gif")
        await ctx.send(file=file, content="Mahjong tiles")

    client = MyClient(intents=intents)
    load_dotenv()
    client.run(os.environ['TOKEN'])
