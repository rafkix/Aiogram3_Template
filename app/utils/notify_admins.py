from aiogram import Bot
from aiogram.utils.markdown import hbold

from data.config import ADMINS


# Xabar yuborish funksiyasi
async def notify_admins(bot: Bot) -> None:
    """
    Adminlarga xabar yuborish
    """
    for admin_id in ADMINS:
        try:
            await bot.send_message(
                                    chat_id=admin_id,
                                    text=f"{hbold('Assalomu Alaykum')}"
                                )
        except Exception as e:
            # Xatolik bo'lsa, uni loglash
            print(f"Xato: {e}")