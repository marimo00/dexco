import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '1277942532:AAHbK_NFjOiFw1Gmi7XnnEphj9gx-EdwbBw')
CHAT_ID = os.environ.get('HAT_ID', '-1001385971119')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception(TELEGRAM_TOKEN, CHAR_ID)

if __name__ == "__main__":
  print(TELEGRAM_TOKEN)
  print(CHAT_ID)
