import telebot
from answers import BotAnswers
from ik import Scene
from accounts_backend import User

bot = telebot.TeleBot(
    "1459191581:AAFeeTzijPTHP-VfiYBbFmMUy5ItDBHHJNM",
    parse_mode = "HTML"
)

scene = Scene()

@bot.message_handler(commands=['start'])
def greetings(message):
    # if not user.is_new: return
    bot.send_message(
        message.chat.id,
        text=scene.text.current(),
        reply_markup=scene.keyboard.current()
        )

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    print(call.data)
    scene.keyboard.update(call.data)
    scene.text.update(call.data)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=scene.text.current(),
        reply_markup=scene.keyboard.current()
        )

@bot.message_handler(content_types=["text"])
def default_answer(message):
	bot.send_message(message.chat.id, text="don't understand")

bot.polling()
