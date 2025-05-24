from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_commands(bot: Bot):
    """
    Bot uchun komandalarni sozlash
    """
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Show help")
    ]
    await bot.set_my_commands(commands=commands)