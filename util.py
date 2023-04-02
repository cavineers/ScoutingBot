import discord
from discord.ext import commands
import os
import traceback

async def handle_command_error(ctx:commands.Context, e:Exception):
    "Print exception traceback to console, then send and appropriate error message to the command author."
    traceback.print_exception(e)
    if isinstance(e, commands.CheckFailure):
        await ctx.reply(embed=DiscordEmbed("Check Failure", "You lack the requirements to run this command."))
        return
    elif isinstance(e, commands.CommandInvokeError):
        e = e.original
    await ctx.reply(embed=DiscordEmbed(f"Got Error {type(e).__name__}", str(e), discord.Color.red()), mention_author=False)

class DiscordEmbed(discord.Embed):
    "A class for more easily creating a discord embed."
    def __init__(self, title:str, description:str, color:discord.Color, *fields, thumbnail:str=None, image:str=None, footer:dict=None, author:dict=None, **kw):
        "Construction notes:\nfooter - {text, icon_url}\nauthor - {name, url, icon_url}\nfield - {name, value, inline}"
        #init embed
        discord.Embed.__init__(self, title=title, description=description, color=color, **kw)
        if thumbnail:
            self.set_thumbnail(url=thumbnail)
        if image:
            self.set_image(url=image)
        if footer:
            self.set_footer(**footer)
        if author:
            self.set_author(**author)
        for field in fields:
            self.add_field(**field)