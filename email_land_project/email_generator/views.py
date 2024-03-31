from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmailForm
from .models import EmailAccount, UserLimit
from django.contrib import messages
import requests

@login_required(login_url='login/')
def add_email_telegram(update: Update, context: CallbackContext):
    user = update.effective_user
    limit_user, created = UserLimit.objects.get_or_create(user=user)
    message = update.message
    if message.text is None:
        message.reply_text("لطفا متن معتبری را ارسال کنید.")
        return
    form = EmailForm(message.text)
    if form.is_valid():

        cpanel_username = "persiad1"
        cpanel_password = "09907682822Gg09907682822!"
        cpanel_domain = "emailg.persiadev.net"

        email_username = form.cleaned_data['email_username']
        email_password = form.cleaned_data['email_password']
        email_quota = "3"

        api_url = f"https://{cpanel_domain}:2083/json-api/cpanel"
        payload = {
            "cpanel_jsonapi_user": cpanel_username,
            "cpanel_jsonapi_module": "Email",
            "cpanel_jsonapi_func": "addpop",
            "email": email_username,
            "password": email_password,
            "quota": email_quota
        }
        email_account = EmailAccount(
            email_username=email_username,
            email_password=email_password,
            email_quota=email_quota,
            user=user
        )
        email_account.save()
        try:
            response = requests.post(api_url, data=payload, auth=(cpanel_username, cpanel_password))
            response.raise_for_status()  # بررسی برای خطاهای HTTP
        except ConnectionError as e:
            update.message.reply_text(f'خطا در برقراری اتصال: {str(e)}')
        except HTTPError as e:
            update.message.reply_text(f'خطا در ارسال درخواست: {str(e)}')
        except Exception as e:
            update.message.reply_text(f'خطای ناشناخته: {str(e)}')
        else:
            if limit_user.email_count > 0:
                limit_user.email_count -= 1
                limit_user.save()
                update.message.reply_text('ایمیل مورد نظر ساخته شد')
            else:
                update.message.reply_text('شما به حداکثر تعداد مجاز ایمیل‌ها رسیده‌اید.')
                return
    else:
        update.message.reply_text('فرم نامعتبر است. لطفا ورودی‌های خود را بررسی کنید.')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('به ربات خوش آمدید!')

def main():
    updater = Updater("6655326710:AAFRv4PFSiBwjgplzZYP1XJPmblgz9-up8I", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, add_email_telegram))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
