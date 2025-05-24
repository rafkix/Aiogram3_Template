from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import Command

router = Router()

@router.message(Command(commands=["help"]))
async def help(message: Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))