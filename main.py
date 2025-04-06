import os
import telegram
import random
from time import sleep
from dotenv import load_dotenv
from telegram.error import NetworkError


def get_files(folder_name):
    files=os.listdir(folder_name)
    random.shuffle(files)
    for file in files:
        file_path=os.path.join(folder_name, file)
        return file_path


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TG_TOKEN"])
    chat_id=os.environ["TG_CHAT_ID"]
    bot.send_message(chat_id=chat_id, text="пиривета! меня зовут федарчик и я уметь скачивать картинки космос")
    time_sleep=os.environ.get("TG_TIME_SLEEP", 14400)
    while True:
        folder_name= os.environ.get("FOLDER_NAME", "images")
        try:
            file_path = get_files(folder_name)
            with open(file_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            sleep(time_sleep)
        except NetworkError:
            print("Ошибка сети. Повторная попытка подключения через 20 секунд")
            sleep(20)
            


if __name__ == "__main__":
    main()