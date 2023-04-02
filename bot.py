import cogs
import configs
from constants import *
import discord
from discord.ext import commands
from util import DiscordEmbed, handle_command_error

def get_prefix(bot:commands.Bot, message:discord.Message):
    id_str = str(message.guild.id if message.guild else message.channel.id)
    return configs.read_configs()[configs.DISCORD_COMMAND_PREFIXES].get(id_str, DEFAULT_COMMAND_PREFIX)


intentes = discord.Intents.default()
intentes.messages = True
bot = commands.Bot(command_prefix=get_prefix, intentes=intentes)
    

@bot.event
async def on_ready():
    print("Ready.")

@bot.command(name="prefix.set")
@commands.has_permissions(manage_guild=True)
async def prefix_set(ctx:commands.Context, prefix:str):
    "Set command prefix locally."
    id_str = str(ctx.guild.id if ctx.guild else ctx.channel.id)
    prev = get_prefix(bot, ctx.message)
    c = configs.read_configs()
    c[configs.DISCORD_COMMAND_PREFIXES][id_str] = prefix
    configs.write_config(c)
    await ctx.reply(embed=DiscordEmbed("Set Command Prefix", f"Set command prefix from '{prev}' to '{prefix}'.", discord.Color.green()), mention_author=False)

@prefix_set.error
async def prefix_set_error(ctx:commands.Context, e:Exception):
    await handle_command_error(ctx, e)

@bot.command(name="prefix.get", aliases=["prefix", "prefix.view", "prefix.show"])
async def prefix_get(ctx:commands.Context):
    "Get local command prefix."
    prefix = get_prefix(bot, ctx.message)
    await ctx.reply(embed=DiscordEmbed("View Command Prefix", f"Prefix is '{prefix}'", discord.Color.green()), mention_author=False)

@prefix_get.error
async def prefix_get_error(ctx:commands.Context, e:Exception):
    await handle_command_error(ctx, e)

@bot.command(name="scout", aliases=["scouting"])
async def scout_shortcut(ctx:commands.Context):
    "Shortcut to scouting site (might not always be up)."
    await ctx.reply("http://scouting.4541cavineers.org/", mention_author=False)

@bot.command(name="github")
async def github_shortcut(ctx:commands.Context):
    "Shortcut for the robotics github page."
    await ctx.reply("https://github.com/cavineers", mention_author=False)

@bot.command(name="sheets")
async def sheets_shortcut(ctx:commands.Context):
    "Shortcut for the scouting google sheets. Note: Access is limited"
    await ctx.reply("https://docs.google.com/spreadsheets/d/1KCPyhZ5O3CdlRzDyMer7pqnJjNJhin79JegNVN5Jo5M/edit#gid=153223117", mention_author=False)

@bot.command(name="suggestions", aliases=["suggest"])
async def suggestions_link(ctx:commands.Context):
    "Send the link to the command suggestions google form."
    await ctx.reply("https://forms.gle/pxtXa9d9PZN4ykUc7", mention_author=False)


def run():
    "Run the bot."
    for cog in cogs.all_cogs:
        bot.add_cog(cog(bot) if isinstance(cog, type) else cog)

    bot.run(configs.read_configs()[configs.DISCORD_TOKEN])