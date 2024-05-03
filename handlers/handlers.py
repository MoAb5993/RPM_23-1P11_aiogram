'''Импорты'''
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.anketa import Anketa
import keyboards.keyboards as kb

router = Router()

@router.message(Command('anketa'))
async def anketa_handler(msg: Message, state: FSMContext):
    '''Запуск анкеты'''
    await state.set_state(Anketa.name)
    await msg.answer('Введите ваше имя', reply_markup=kb.cancel_anketa_btn)

@router.message(F.data =='cancel_anketa')
async def next_handler(callback_query: CallbackQuery, state: FSMContext):
    '''Отмена'''
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    '''Имя'''
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    await msg.answer('Введите ваш возраст', reply_markup=kb.anketa_btn)

@router.callback_query(F.data == 'set_name_anketa')
async def next_handler_(callback_query: CallbackQuery, state: FSMContext):
    '''Запуск анкеты'''
    await anketa_handler(callback_query, state)

@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    '''Возраст'''
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы неверно ввели возраст')
        await msg.answer('Введите свой возраст')
        return

    await state.set_state(Anketa.gender)
    await msg.answer('Введите ваш пол', reply_markup=kb.gender_btn)

@router.callback_query(F.data =='Male',Anketa.gender)
async def mujik(callback_query: CallbackQuery, state: FSMContext):
    '''Мужской пол'''
    await state.update_data(gender="m")
    await callback_query.message.answer(str(state.get_data()))
    await state.clear()

@router.callback_query(F.data =='Female',Anketa.gender)
async def wife(callback_query: CallbackQuery, state: FSMContext):
    """Уээээ"""
    await state.update_data(gender="W")
    await callback_query.message.answer(str(state.get_data()))
    await state.clear()
