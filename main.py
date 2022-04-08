import logging, requests, random
from bs4 import BeautifulSoup

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def getYoutube(search_keyword):
    return 0

def getPornhub(search_keyword):
    URL = 'https://www.pornhub.com/video/search?search='
    response = requests.get(URL + search_keyword)
    soup = BeautifulSoup(response.text, 'lxml')
    ph_links = []
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("/view_video"):
            ph_links.append('https://www.pornhub.com' + a['href'])
    return random.choice(ph_links)

def getGiphyImage(search_keyword):
  URL = 'http://api.giphy.com'
  SEARCH_PATH = '/v1/gifs/search'
  payload = {'api_key': 'gKs8c63gf2e6Vq75MlQBWpuW1yCD7TsC', 'q': search_keyword}
  r = requests.get(URL + SEARCH_PATH, params=payload)
  data = r.json()['data']
  image_position = random.randrange(0, len(data))
  image_url = data[image_position]['images']['original']['url']
  return image_url

def giphy(update, context):
    search = update.message.text.split()[1]
    update.message.reply_text(search)
    #update.message.reply_text("ananin ami calissana," + search)
    update.message.reply_animation(getGiphyImage(search))

def help(update, context):
    update.message.reply_text('/giphy <search> \n/pornhub <search>')

def youtube(update, context):
    update.message.reply_text(getYoutube(update.message.text.split()[1]))

def pornhub(update, context):
    update.message.reply_text(getPornhub(update.message.text.split()[1]))

def giphy(update, context):
    update.message.reply_animation(getGiphyImage(update.message.text.split()[1]))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5225421589:AAEq4Hr37vkVO4_2YYVTwHSTc6QxhlkD0aU", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("giphy", giphy))
    dp.add_handler(CommandHandler("pornhub", pornhub))
    dp.add_handler(CommandHandler("youtube", youtube))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
