import telebot
from functools import lru_cache
import threading

#токен бота
bot = telebot.TeleBot('6432853446:AAFR9VbngAWHI5-kgMbZGYZmLyH3_lVLGSQ')

#начальное значение мемоизации
lru_cache(maxsize=128)

#функция для вычисления факториала с использованием мемоизации
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Я бот, который считает факториал числа. '
                          'Просто отправь мне /fct [число] и я дам тебе результат.')

#обработчик команды /factorial
@bot.message_handler(commands=['fct'])
def handle_factorial(message):
    try:
        num = int(message.text.split()[1])
        thread = threading.Thread(target=calculate_and_reply, args=(message, num))  
        thread.start()  
    except (ValueError, IndexError):
        bot.reply_to(message, "Ошибка.Отправьте,пожалуйста,корректное целое число")

def calculate_and_reply(message, num):
    if num < -1000 or num > 1000: 
            result = str(factorial(num))[:5] 
    else: 
        result = str(factorial(num)) 
        bot.reply_to(message, f"Факториал числа {num} равен: {result}") 


#запуск бота
bot.polling(none_stop=True, interval=0)


    