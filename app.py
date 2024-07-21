import data
import telebot
import first_and_last_adresses
from telebot import types
bot = telebot.TeleBot(data.TOKEN)

class User:
    _cmd_status = None
    def __init__(self, id:int, name=''):
        self.id = id
        self.name = name
        self.status = 'alive'
    def cmd_handler(self, cmd: str):
        if cmd[:5] == 'start':
            self.status = 'alive'
            return
        if cmd[:3] == 'end':
            self.status = 'dead'
            return
        if cmd == ["first_and_last"]:
            self._cmd_status = 'searching_first_and_lst'
            bot.send_message(self.id, 'Результат')
            return

cmd_list = ['help', 'start', 'end']
user = User(0, 'sfsdf')
@bot.message_handler(commands=['start'])
def receive_comands(message):
    bot.send_message(message.chat.id, 'Бот начал свою работу')
    user.id = message.from_user.id,
    user.name = message.from_user.first_name
    # bot.send_message(message.chat.id, user.status)
@bot.message_handler(commands=['end'])
def receive_comands(message):
    bot.send_message(message.chat.id, 'Бот окончил свою работу')
@bot.message_handler(commands=['help'])
def receive_comands(message):
    bot.send_message(message.chat.id, data.TEXT_OF_HELP)
@bot.message_handler(commands=['first_and_last_adress'])
def receive_comands(message):
    user._cmd_status = 'frst_and_lst'
    bot.send_message(message.chat.id, user._cmd_status)
@bot.message_handler(content_types=['text'])
def get_text(message):
    if user._cmd_status == 'frst_and_lst':
        ip = message.text.split(" ")[0]
        submask = message.text.split(" ")[1]
        min, max = first_and_last_adresses.find_network_addresses(ip, submask)
        result = " ".join(["Минимальный адресс равен", min,",а максимальный", max])
        bot.send_message(message.chat.id, result)
        user._cmd_status = None

bot.polling()