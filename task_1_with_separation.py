from pathlib import * # Библиотека для работы с директориями

DISC_NAME = ['A','B','C','D','E'] # Название корневой директории (исходные данные)
EXPECTED_SUFFIX = 'js' # Нужное расширение (исходные данные)
N = 3 # На сколько списков нужно разбить общий (исходные данные)


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

required_quantity = int(sum(dir_dict.values())/N) # Вычисляем примерное количество фалов в каждом словаре с округлением в меньшую сторону
small_dir_dict = {}

for folder, count in dir_dict.items():
    small_dir_dict[folder] = count
    if sum(small_dir_dict.values()) >= required_quantity: # Если сумма количества всех элементов не меньше нужного значения,
        for key, value in small_dir_dict.items():
            print(f'{key} ({value})') # Выводим словарь на печать
        print('\n')
        small_dir_dict.clear() # И затем чистим его для повторения цикла
for key, value in small_dir_dict.items():
    print(f'{key} ({value})') # Печатаем последний получившийся словарь
