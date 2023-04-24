import asyncio
import discord
from discord.ext import commands
from configs import config
from help_cog import HelpCog
from music_cog import MusicCog

import logging

async def main():
    logging.basicConfig(level=logging.WARNING)

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(config.commands_prefix),intents=intents)
    async with bot:
        bot.remove_command('help')
        await bot.add_cog(HelpCog(bot))
        await bot.add_cog(MusicCog(bot))
        await bot.start(config.bot_token.get_secret_value())


asyncio.run(main())