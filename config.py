import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '1443319953:AAFZ5x4bLbCh0CYeeSNlDvwOevxXhIBnxu4')
CHAT_ID = os.environ.get('CHAT_ID', '-451662546')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception(TELEGRAM_TOKEN, CHAR_ID)

if __name__ == "__main__":
  print(TELEGRAM_TOKEN)
  print(CHAT_ID)
