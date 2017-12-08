

# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?

# Импортируйте необходимые библиотеки

# import 

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 
import pprint
import json

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        json_file = open('data.json', 'r')
        fl = json_file.read()
        data = json.loads(fl)

except FileExistsError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


pprint.pprint(data)

# Вывести в форматированном виде поля: 

# company, email, phone, address
