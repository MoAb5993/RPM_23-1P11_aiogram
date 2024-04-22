import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

bot = Bot(token="6495085956:AAHNbitT6w1lRBmFhO0X9zpaUhk-aqKoupo")
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start', description='Поехали'),
        BotCommand(command='help', description='Никто не поможет'),
        BotCommand(command='delete', description='В окно!')
    ])
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await msg.answer(text="Страницы 1", reply_markup=inline_markup)
    
@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(
        'Страница 2', reply_markup=inline_markup
    )

@router.callback_query(F.data == 'back')
async def back_handler(callbck_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await callbck_query.message.delete()
    await callbck_query.message.answer(
        text='Страница 1',
        reply_markup=inline_markup
    )

async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())
