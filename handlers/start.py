"""Уээээ"""
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
import keyboards.keyboards as kb
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    """Уээээ"""
    #pylint: disable= C0415
    from main import bot
    await bot.set_my_commands([
        BotCommand(command='start', description='Поехали'),
        BotCommand(command='anketa', description='Оставь надежды, всяк сюда входящий'),
        BotCommand(command='delete', description='В окно!')
    ])
    await msg.answer(text="Страницы 1", reply_markup=kb.next_page_btn)

@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    """Уээээ"""
    await callback_query.message.edit_text(
        'Страница 2', reply_markup=kb.back_page_btn
    )

@router.callback_query(F.data == 'back')
async def back_handler(callbck_query: CallbackQuery):
    """Уээээ"""
    await callbck_query.message.delete()
    await callbck_query.message.answer(
        text='Страница 1',
        reply_markup=kb.next_page_btn
    )
