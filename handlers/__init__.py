"""Ипорты модулей"""
from aiogram import Dispatcher
from handlers import handlers, start

def include_routers(dp: Dispatcher):
    """Взятие роутеров"""
    dp.include_routers(
        start.router,
        handlers.router
    )
