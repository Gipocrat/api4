import os
import telegram
import random
from time import sleep
from dotenv import load_dotenv
from telegram.error import NetworkError


def get_file_path(folder_name):
    files=os.listdir(folder_name)
    random.shuffle(files)
    for file in files:
        file_path=os.path.join(folder_name, file)
        return file_path
    

def send_photo_from_file(file_path, chat_id, bot):
    with open(file_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TG_TOKEN"])
    chat_id=os.environ["TG_CHAT_ID"]
    bot.send_message(chat_id=chat_id, text="пиривета! меня зовут федарчик и я уметь скачивать картинки космос")
    time_sleep=os.environ.get("TG_TIME_SLEEP", 14400)
    while True:
        folder_name= os.environ.get("FOLDER_FOR_IMAGES", "images")
        try:
            file_path = get_file_path(folder_name)
            send_photo_from_file(file_path, chat_id, bot)
        except NetworkError:
            print("Ошибка сети. Повторная попытка подключения через 20 секунд")
            sleep(20)
        sleep(int(time_sleep))
            


if __name__ == "__main__":
    main()