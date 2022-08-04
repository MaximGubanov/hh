import telebot

bot = telebot.TeleBot('5547274402:AAG6gNiuJ38XYPtqI1hrwuwAzAi8okQC_Fk')

CHANNEL_NAME = -1001709744135


def bot_send_to_chat(data):
    bot.send_message(CHANNEL_NAME, data)


if __name__ == '__main__':
    bot.infinity_polling()
