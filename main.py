"""
Данный скрипт работает следующим образом: программа пробегается по выбранной папке,
и если есть файлы с расширением .htm, то программа меняет на расширение .html
"""

import os

def convert_htm_to_html(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".htm"):
                htm_path = os.path.join(root, file)
                html_path = os.path.join(root, file.replace(".htm", ".html"))
                os.rename(htm_path, html_path)
                print(f"Converted: {htm_path} to {html_path}")

# Заменить 'C:/webbbbbbb/gdvl.ru' на путь к вашей папке с файлами
folder_path = 'C:/webbbbbbb/gdvl.ru'
convert_htm_to_html(folder_path)
