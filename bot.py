import pickle
import requests
import json
from discord.ext import commands
import discord
from autoloader import Autoloader

env_file = open("./.dis_config", 'rb')
aoc_url = 'https://adventofcode.com/'
current_year = '2020'
env = pickle.load(env_file)
env_file.close()

bot = commands.Bot(command_prefix='!')

al = Autoloader()
al.connect()
hbreak = "-" * 24
allowed_cats = ('stars', 'local_score', 'global_score')
allowed_years = ['20'+str(x) for x in range(15, 21)]
@bot.command(name='sb',  help='prints the given years advent of code private scoreboard')
async def score_board(ctx, year=current_year, cat='stars'):
    if year not in allowed_years:
        year = '2020'
    if cat not in allowed_cats:
        cats = 'stars'
    lb = al.check_leaderboard(year)
    title = ('name', 'stars')
    response = \
    f"""```
    {year} Advent of Code Leaderboard \n
    {hbreak}
    {title[0]: ^16} | {cat}
    {hbreak}
    """
    for id_num in lb:
        response += f"{lb[id_num]['name']: ^16} | {str(lb[id_num][cat])}\n\t"
    response += """
    ```"""
    await ctx.send(response)


bot.run(env["DISCORD_TOKEN"])
