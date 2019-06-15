#import components
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

#logging's settings 

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )



#function for greeting user -- в скобках параметры на вход, которые принимает функция
def greet_user(bot, update): 
	text='Вызван /start'
	logging.info(text)
	update.message.reply_text(text)

#function for talk_to_me
def talk_to_me(bot, update):
	user_text="Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
	#user_text=update.message.text #создаем переменную с текстом сообщения пользователя
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
		update.message.chat.id, update.message.text)

	#print(update.message) #выводит атрибуты собщения id, user, etc --бесполезная фигня, меняем на логи 
	#print(user_text) #выводим текст сообщения пользователя в консоль
	update.message.reply_text(user_text) #отвечаем тем же текстом --эхо бот


#function with updater
def main():
	mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
	logging.info('Бот запускается')
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user)) #обработчик команд
	dp.add_handler(MessageHandler(Filters.text, talk_to_me)) #обработчик сообщений
	mybot.start_polling()
	mybot.idle()

#functions calling
main()