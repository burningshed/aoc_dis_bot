import pickle
import requests
import json
from discord.ext import commands
import discord
from MusicLeague import musicleague

env_file = open("./.dis_config", 'rb')
env = pickle.load(env_file)
env_file.close()

ml = musicleague()

bot = commands.Bot(command_prefix='!')

@bot.command(name='list',  help='prints the given years advent of code private scoreboard')
async def list_themes(ctx):
    theme_list = ml.get_cur_themes()
    title = ('name', 'stars')
    hbreak = str("~"*12)
    response = \
    f"""```
    Ryan (Still) Sucks Theme Selection List \n
    {hbreak}
    ID | {title[0]: ^16} | "votes"
    {hbreak}
    """
    for theme in theme_list:
        response += f"{theme.id} | {theme.name : ^16} | {theme.get_votes()}\n\t"
    response += """
    ```"""
    await ctx.send(response)


bot.run(env["DISCORD_TOKEN"])

# TODO: create musicleague class, in it have accessable id and name objects and a get_votes class and get_cur_themes
# 1. id
# 2. name
# 3. theme 