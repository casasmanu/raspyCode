from bs4 import BeautifulSoup
import requests
import schedule

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

usuarios={}
usuarios['manu']='5178063489'

def bot_send_text(bot_message,update: Update):
    
    bot_token = '5212795032:AAH32kz9IJlgoXZZFOZcQz6RfshGiWXxb_w'
    for bot_chatID in usuarios.values():
        #bot_chatID = '5178063489' #mio
        #bot_chatID = '220619299' #Jose
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print("envio")
    
    #return response.json()


def btc_scraping():
    #link de la fuente
    start_url = 'https://www.infodolar.com/cotizacion-dolar-blue.aspx'
    #descargo la info en html de la pagina y la parseo
    downloaded_html = requests.get(start_url)
    soup = BeautifulSoup(downloaded_html.text,"html.parser")
    #busco el selector deseado y lo convierto en string para su uso
    full_table=soup.select('table.cotizaciones td')[2]
    string = full_table.text.split()
    string = string[0] + string[1]
    
    format_result = string
    return format_result
    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hola! Le hablaste al bot de macasas, para ver la lista de comandos envia /help !")

def report(update: Update):
    btc_price = f'El precio del dolar blue hoy es  : {btc_scraping()}'
    bot_send_text(btc_price,update)

def answer_usd(update: Update, context: CallbackContext):
    btc_price = f'El precio del dolar blue hoy es  : {btc_scraping()}'
    update.message.reply_text(btc_price)

def adduser(update: Update, context: CallbackContext):
    usuarios[update.message.chat.full_name]=update.message.chat_id 
    update.message.reply_text("user added to list succesfully")

if __name__ == '__main__':
    #inicio el updater con el codigo token del bot
    updater = Updater('5212795032:AAH32kz9IJlgoXZZFOZcQz6RfshGiWXxb_w',use_context=True)
    #
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('usd', answer_usd))
    updater.dispatcher.add_handler(CommandHandler('addme', adduser))
    #le indico al script que empiece a leer los mensajes recibidos del bot
    updater.start_polling()

    schedule.every().day.at("02:45").do(report,updater )

    while True:
        schedule.run_pending()




