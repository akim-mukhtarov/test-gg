import requests as r
from telebot import types as teletypes

class Scene():
    def __init__(self):
        self.keyboard = self.SceneKeyboard()
        self.text = self.SceneText()

    class SceneText():
        def __init__(self):
            self.texts = {
                'goBack': "<b>Всего три простых шага!</b>\n\
1️) Пополняй свой аккаунт Good Game в любом из наших киберспортивных клубов от 250 ₽ за 24 суммарно;\n\
2️) Нажми на кнопку  \"Открыть Коробку удачи\"\n\
3️) Выигрывай призы!\n\
\n\
Все призы можно получить у администратора. \n\
Подробнее о всех призах в разделе 🎁<b>Призы</b>🎁",
                'presentsAll': "Призы из Кейсов можно забрать сразу у администратора.\n\
Для этого необходимо подойти к администратору и открыв вкладку <b>\"Мои подарки<b>\"</b>\
показать список призов, которые у тебя сейчас есть.\n\
\n\
<b>Базовый Кейс (250 рублей)</b>\n\
1 час игры за пк\n\
Полчаса игры за PS\n\
Полчаса игры за ПК\n\
\n\
<b>Кейс для бояр (500 рублей)</b>\n\
Батончик\n\
1.5 часа за PC\n\
Кола (0.5)\n\
Пакет в зал Стандарт (ночной)\n\
\n\
<b>Кейс для Вельмож (1000 рублей)</b>\n\
Пакет в зал VIP (утренний)\n\
Кола и батончик\n\
3 часа за PS\n\
\n\
<b>Кейс для Меценатов (2000 рублей)</b>\n\
Абонемент на посещение клуба (на все выходные)\n\
Кальян\n\
Пакет в зал VIP (ночной)",
                 'getPresentsList': "Ваши призы: ",
                 'getNewPresent': 'ну давай'
            }
            self.txt = self.texts['goBack']
        def update(self, btn):
            if btn in self.texts:
                self.txt = self.texts[btn]
        def current(self):
            return self.txt

    class SceneKeyboard():
        def __init__(self):
            start = teletypes.InlineKeyboardMarkup()
            start.add(teletypes.InlineKeyboardButton(text='Открыть кейс', callback_data="getNewPresent"))
            start.add(teletypes.InlineKeyboardButton(text='Мои призы', callback_data="getPresentsList"))
            start.add(teletypes.InlineKeyboardButton(text='Подарки', callback_data="presentsAll"))

            endpoint = teletypes.InlineKeyboardMarkup()
            endpoint.add(teletypes.InlineKeyboardButton(text='Назад', callback_data="goBack"))

            self.markups = {
                'goBack': start,
                'presentsAll': endpoint,
                'getNewPresent': endpoint,
                'getPresentsList': endpoint
            }
            self.markup = self.markups['goBack']

        def update(self, btn):
            if btn in self.markups:
                self.markup = self.markups[btn]
        def current(self):
            return self.markup
