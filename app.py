import telebot
from tkn import currency, TOKEN
from exten import ConvException, GetCurrency

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = 'Для перевода одной валюты в другую введите команду в следующем виде: \n\
<имя валюты которую конвертируем> <имя валюты в которую конвертируем> <количество первой валюты>\n\
Для вывода информации о валютах введите команду /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message):
    text = 'Список валют\n ----------'
    for k in currency.keys():
        text = '\n'.join((text, k, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message):
    your_msg = message.text.split(' ')

    if len(your_msg) != 3:
        raise ConvException('Введено неверное количество параметров.')

    base, quote, amount = your_msg

    result = GetCurrency.get_price(base, quote, amount)
    text = f'Цена {amount} {base} в {quote} = {result}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
