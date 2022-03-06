from bs4 import BeautifulSoup
import requests
import schedule


def bot_send_text(bot_message):
    
    bot_token = '5212795032:AAH32kz9IJlgoXZZFOZcQz6RfshGiWXxb_w'
    bot_chatID = '5178063489' #mio
    #bot_chatID = '220619299' #Jose
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    print("envio")
    return response.json()


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
    

def report():
    btc_price = f'El precio del dolar blue hoy es  : {btc_scraping()}'
    bot_send_text(btc_price)


if __name__ == '__main__':
        
    schedule.every().day.at("18:27").do(report)

    while True:
        schedule.run_pending()
        #test_bot = bot_send_text('¡Hola, Telegram!')
        report()

