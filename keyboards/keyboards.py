"""Кнопки для выбора пола, смены страниц и отмена анкеты"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_anketa_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])

anketa_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
         InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])

gender_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Мужской', callback_data='Male'),
         InlineKeyboardButton(text='Женский', callback_data='Female')],
        [InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
         InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])

next_page_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])

back_page_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
