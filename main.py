import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

bot = Bot(token="")
dp = Dispatcher()

router = Router()

class Anketa(StatesGroup):
    name = State()
    age = State()
    gender = State()

@router.message(Command('anketa'))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])
    await msg.answer('Введите ваше имя', reply_markup=markup)

@router.message(F.data =='cancel_anketa')
async def next_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
         InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])
    await msg.answer('Введите ваш возраст', reply_markup=markup)

@router.callback_query(F.data == 'set_name_anketa')
async def next_handler(callback_query: CallbackQuery, state: FSMContext):
    await anketa_handler(callback_query, state)

@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы неверно ввели возраст')
        markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
         InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])
        await msg.answer('Введите свой возраст')
        return

    await state.set_state(Anketa.gender)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Мужской', callback_data='Male'), InlineKeyboardButton(text='Женский', callback_data='Female')],
        [InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
         InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]
    ])
    await msg.answer('Введите ваш пол', reply_markup=markup)

@router.callback_query(F.data =='Male',Anketa.gender)
async def Mujik(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(gender="m")
    await callback_query.message.answer(str(state.get_data()))
    await state.clear()

@router.callback_query(F.data =='Female',Anketa.gender)
async def Wife(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(gender="W")
    await callback_query.message.answer(str(state.get_data()))
    await state.clear()

# @router.message(Anketa.age)
# async def set_gender_by_anketa_handler(msg: Message, state: FSMContext):
#     await state.update_data(gender=msg.text)
#     await msg.answer(str(state.get_data()))
#     await state.clear()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start', description='Поехали'),
        BotCommand(command='anketa', description='Оставь надежды, всяк сюда входящий'),
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
