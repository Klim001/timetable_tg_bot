from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

groups = ['o745b', 'e742b', 'r146b']

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'timetable')],
    [KeyboardButton(text = 'dollar'), KeyboardButton(text = 'weather')]
])

settings_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='О745Б', callback_data="О745Б")],
    [InlineKeyboardButton(text='Е742Б', callback_data="Е742Б")],
    [InlineKeyboardButton(text='Р146Б', callback_data="Р146Б")],
])
settings_table_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пред.день', callback_data="yesterday"), InlineKeyboardButton(text='Сегодня', callback_data="today"), InlineKeyboardButton(text='Cлед.день', callback_data="tomorrow")]
])