from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=f"Assalomu Alaykum {message.from_user.first_name}",
    )
