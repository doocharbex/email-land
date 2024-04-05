import telebot
from django.http import JsonResponse
from .models import *

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "به ربات EmailLand خوش امدی 😍")


@bot.message_handler(commands=['getuserID'])
def get_user_id(message):
    try:
        telegram_id = message.from_user.id

        user_limit, created = UserLimit.objects.get_or_create(telegram_id=telegram_id)
        if user_limit.email_count > 0:

            bot.reply_to(message, f"Your user ID: {telegram_id}")

            user_limit.email_count -= 1
            user_limit.save()
        else:
            bot.reply_to(message, "شما دیگر اجازه استفاده از این دستور را ندارید.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


def bot_status(request):
    is_bot_online = bot.get_me().is_bot
    if is_bot_online:
        status = "آنلاین"
    else:
        status = "آفلاین"
    return JsonResponse({"status": status})


bot.polling()
