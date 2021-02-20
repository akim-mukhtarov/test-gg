import requests as r
from telegram_response import Telegram_Response

class Bot:
    def __init__(self):
        # приватные поля
        self.__TOKEN = '1459191581:AAFeeTzijPTHP-VfiYBbFmMUy5ItDBHHJNM'
        self.__OFFSET = 0
        self.__URL = 'https://api.telegram.org/bot'
        self.__PATH = self.__URL + self.__TOKEN
        self.__DATA = {'offset': self.__OFFSET, 'limit': 0, 'timeout': 0}

    def __set_offset(self, offset_id):
        # устанавливаем offset на текущее сообщение
        self.__OFFSET = offset_id

    def __inc_offset(self):
        self.__OFFSET += 1

    def __update_request_data(self):
        self.__DATA['offset'] = self.__OFFSET

    def __parse_response(self, update):
        self.__set_offset(update['update_id'])
        message_data = { # формируем информацию для отправки сообщения
            'chat_id': update['message']['chat']['id'], # куда отправляем сообщение
            'text': "I'm <b>bot</b>", # само сообщение для отправки
            'reply_to_message_id': update['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
            'parse_mode': 'HTML'
        }
        self.__inc_offset() # ! инкрементируем в любом случае, потому что как достучаться потом я еще не придумал
        return message_data

    def check_updates(self):
        try: # собственно сам запрос
            request = r.post(
                self.__PATH + '/getUpdates',
                data=self.__update_request_data()
            )
        except Exception as exc:
            print(exc)
            print('Error getting updates')
            return False

        response = Telegram_Response(request)
        if not response.is_ok(): return False
        # only for new messages
        for update in response.get_new_messages(since=self.__OFFSET):
            msg = self.__parse_response(update)
            success = self.send_response(msg)
            if not success: continue


    def send_response(self, msg):
        try:
            request = r.post(self.__PATH + '/sendMessage', data=msg) # запрос на отправку сообщения
        except:
            print('Send message error')
            return False
        if not request.status_code == 200: # проверим статус пришедшего ответа
            return False
        return True

    # геттеры
    def get_token(self):
        return self.__TOKEN
    def get_path(self):
        return self.__PATH

bot = Bot()
print(bot.get_path())
x = 3
while x > 0:
    bot.check_updates()
    x -= 1
