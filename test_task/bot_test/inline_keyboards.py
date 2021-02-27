import requests as r
from telebot import types as teletypes

class BotKeyboards():
    def __init__(self):
        keyboard = teletypes.InlineKeyboardMarkup()
        keyboard.add(teletypes.InlineKeyboardButton(text='Открыть кейс', callback_data="getNewPresent"))
        keyboard.add(teletypes.InlineKeyboardButton(text='Мои призы', callback_data="getPresentsList"))
        keyboard.add(teletypes.InlineKeyboardButton(text='Подарки', callback_data="presentsAll"))
        self.main = keyboard

        endpoint_keyboard = teletypes.InlineKeyboardMarkup()
        endpoint_keyboard.add(teletypes.InlineKeyboardButton(text='Назад', callback_data="goBack"))
        self.endpoint = endpoint_keyboard
