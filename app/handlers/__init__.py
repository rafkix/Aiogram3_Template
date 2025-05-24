from aiogram import Dispatcher

from app.handlers import users, groups, channels

def setup(dp: Dispatcher):
    """
    Botning routerlarini sozlash uchun setup funksiyasi.
    """
    users.setup(dp)  # Foydalanuvchi bilan bog'liq handlerlarni ulash
