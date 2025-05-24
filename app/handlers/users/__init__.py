from aiogram import Dispatcher
from .start import router as user_router
from .help import router as help_router

def setup(dp: Dispatcher):
    """
    Botning routerlarini ulash uchun setup funksiyasi.
    """
    dp.include_routers(
        user_router,
        help_router
    )