from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
from async_throttle import Throttle
from typing import Callable, Dict, Any
import logging

logger = logging.getLogger(__name__)

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: float = 1.0, prefix: str = "antiflood_"):
        self.default_limit = rate_limit
        self.prefix = prefix
        self.throttler = Throttle()
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Any],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user = event.from_user
        if not user:
            return await handler(event, data)

        # Individual handler uchun limitni olamiz (flags orqali)
        limit = get_flag(data, "throttling_rate_limit") or self.default_limit
        key = f"{self.prefix}{user.id}"

        try:
            async with self.throttler(key, rate=limit):
                return await handler(event, data)
        except Exception:
            logger.warning(f"⛔️ Throttled: {user.id} - too many requests")
            await event.answer("🚫 Juda ko‘p so‘rov yuborildi. Iltimos, biroz kuting.")
