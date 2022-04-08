import os, telebot
import requests, sys, random
TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']
GIPHY_API_KEY = os.environ['GIPHY_API_KEY']

bot = telebot.TeleBot(TELEGRAM_API_KEY)

def getGiphyImage(search_keyword):
  URL = 'http://api.giphy.com'
  SEARCH_PATH = '/v1/gifs/search'
  payload = {'api_key': GIPHY_API_KEY, 'q': search_keyword}
  r = requests.get(URL + SEARCH_PATH, params=payload)
  data = r.json()['data']
  image_position = random.randrange(0, len(data))
  image_url = data[image_position]['images']['original']['url']
  return image_url

@bot.message_handler(commands=['greet'])
def greet(msg):
  search = msg.text.split()[1]
  res = getGiphyImage(search)

  bot.send_animation(msg.chat.id, res, caption="EVEDO TO 1$ !!")
  
  #bot.reply_to(msg, res)

bot.set_webhook(url="https://exciting-giphy-bot.herokuapp.com/", certificate=open('mycert.pem'))
