
import app.keyboard as kb
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F
from data.data import dollar, weather, timetable
import datetime
from config import URL_E742B, URL_R146B, URL_O745B
from database.models import models_main
from database.configur import PATH

router = Router()

number = 200
Main_url = ''
dict_users = {}

@router.message(CommandStart())
async def cmd_start(message: Message):
    global number
    number = 200
    await message.answer('Привет', reply_markup=kb.main)


@router.message(F.text == 'dollar')
async def dollar_curse_handler(message: Message):
    ans = dollar()
    await message.answer(ans)


@router.message(F.text == 'weather')
async def weather_handler(message: Message):
    ans = weather()
    await message.answer(ans)


@router.message(F.text == 'timetable')
async def timetable_handler(message: Message):
    dict_users[message.from_user.id] = []
    await message.answer('Выберите группу _ ', reply_markup=kb.settings_group)


@router.callback_query(F.data == 'О745Б')
async def callback_1(call: CallbackQuery):
    global number
    dict_users[call.message.from_user.id] = [URL_O745B, 0]
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')


@router.callback_query(F.data == 'Е742Б')
async def callback_2(call: CallbackQuery):
    global number
    dict_users[call.message.from_user.id] = [URL_E742B, 1]
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')


@router.callback_query(F.data == 'Р146Б')
async def callback_3(call: CallbackQuery):
    global number
    dict_users[call.message.from_user.id] = [URL_R146B, 2]
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')


@router.callback_query(F.data == 'yesterday')
async def yester(call: CallbackQuery):
    global number
    number -= 1
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')

@router.callback_query(F.data == 'tomorrow')
async def tomorrow(call: CallbackQuery):
    global number
    number += 1
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')

@router.callback_query(F.data == 'today')
async def today(call: CallbackQuery):
    date = datetime.date.today()
    day_week = date.weekday()
    global number
    number += (day_week - number % 7)
    ans = models_main(PATH, number % 7, dict_users[call.message.from_user.id][0], dict_users[call.message.from_user.id][1])
    await call.message.answer(ans, reply_markup=kb.settings_table_button, parse_mode='html')

