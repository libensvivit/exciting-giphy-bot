import logging, requests, random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def getGiphyImage(search_keyword):
  URL = 'http://api.giphy.com'
  SEARCH_PATH = '/v1/gifs/search'
  payload = {'api_key': 'gKs8c63gf2e6Vq75MlQBWpuW1yCD7TsC', 'q': search_keyword}
  r = requests.get(URL + SEARCH_PATH, params=payload)
  data = r.json()['data']
  image_position = random.randrange(0, len(data))
  image_url = data[image_position]['images']['original']['url']
  return image_url

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Currently I am in Alpha stage, help me also!')

def greet(update, context):
    giphy = getGiphyImage(update.message.text.split()[1])
    update.message.reply_animation(giphy)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5225421589:AAEq4Hr37vkVO4_2YYVTwHSTc6QxhlkD0aU", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("greet", greet))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
