"""Импорт модуля состояний"""
from aiogram.fsm.state import State, StatesGroup

class Anketa(StatesGroup):
    """Сами состояния"""
    name = State()
    age = State()
    gender = State()
