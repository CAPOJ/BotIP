import data
import telebot
import first_and_last_adresses
import transform_mask
from telebot import types
from is_right_ip import bitwise_multiply_ip_and_mask
import random
bot = telebot.TeleBot(data.TOKEN)

class User:
    _cmd_status = None
    def __init__(self, id:int, name=''):
        self.id = id
        self.name = name
        self.status = 'alive'
        self.task = ''
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
@bot.message_handler(commands=['from_nn_to_abcd'])
def receive_comands(message):
    user._cmd_status = 'from_nn_to_abcd'
    bot.send_message(message.chat.id, user._cmd_status)
@bot.message_handler(commands=['from_abcd_to_nn'])
def receive_comands(message):
    user._cmd_status = 'from_abcd_to_nn'
    bot.send_message(message.chat.id, user._cmd_status)
@bot.message_handler(commands=['calculate_adress'])
def receive_comands(message):
    user._cmd_status = 'calculate_adress'
    bot.send_message(message.chat.id, user._cmd_status)
@bot.message_handler(commands=['calculate_mask'])
def receive_comands(message):
    user._cmd_status = 'calculate_mask'
    random_num = random.randint(0, 32)
    bot.send_message(message.chat.id, "".join(["Вычислите маску /", str(random_num)]))
    user.task = "".join(["/",str(random_num)])
@bot.message_handler(content_types=['text'])
def get_text(message):
    if user._cmd_status == 'frst_and_lst':
        ip = message.text.split(" ")[0]
        submask = message.text.split(" ")[1]
        min, max = first_and_last_adresses.find_network_addresses(ip, submask)
        result = " ".join(["Минимальный адресс равен", min,",а максимальный", max])
        bot.send_message(message.chat.id, result)
        user._cmd_status = None
    if user._cmd_status == 'from_abcd_to_nn' or user._cmd_status == 'from_nn_to_abcd':
        submaskold = message.text
        if user._cmd_status == 'from_abcd_to_nn':
            newmask = transform_mask.convert_subnet_mask_to_cidr(submaskold)
        else:
            newmask = transform_mask.convert_cidr_to_subnet_mask(submaskold)
        bot.send_message(message.chat.id, " ".join(["Новая маска",newmask]))
        user._cmd_status = None
    if user._cmd_status == 'calculate_adress':
        ip = message.text.split(" ")[0]
        mks = message.text.split(" ")[1]
        res = bitwise_multiply_ip_and_mask(ip,mks)
        bot.send_message(message.chat.id, res)
        user._cmd_status = None
    if user._cmd_status == 'calculate_mask':
        mask = user.task
        # bot.send_message(message.chat.id, mask)
        res = transform_mask.convert_cidr_to_subnet_mask(mask)
        user_msk = message.text
        if user_msk == data.masks[int(mask.split("/")[1])]:
            # bot.send_message(message.chat.id, data.masks[int(mask.split("/")[1])])
            # bot.send_message(message.chat.id, res)
            bot.send_message(message.chat.id, 'Правильно')
        else:
            bot.send_message(message.chat.id, 'Неправильно')
        # bot.send_message(message.chat.id, res)
        user._cmd_status = None
        user.task = ''
bot.polling()