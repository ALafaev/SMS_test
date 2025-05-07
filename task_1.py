from pathlib import * # Библиотека для работы с директориями
from constant import * # Исходные данные


dir_dict = {}
for disk in DISC_NAME:
    if not Path(f'{disk}:').exists():
        print(f'System has no disk {disk}:') # Если корневая директория отсутствует в системе, выводим сообщение об ошибке
    else:
        directory = Path(f'{disk}:')
        for i in directory.rglob(f'*.{EXPECTED_SUFFIX}'): # Ищем все файлы с нужным расширением
            folder_path = str(i.parent) # Путь к папке с найденным файлом
            if folder_path not in dir_dict.keys(): # Проверяем отсутствие данного пути в формируемом словаре
                dir_dict[folder_path] = 1 # Если путь отсутствует в словаре, присваиваем ему количество 1
            else:
                dir_dict[folder_path] = dir_dict[folder_path] + 1 # Если такой путь уже есть, количество увеличиваем на 1

for folder, count in dir_dict.items(): # Печатаем полученный словарь в нужном формате
    print(f'{folder} ({count})')
