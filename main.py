from units import read_json_file, data_json, mask_number
from datetime import datetime

def main():

    """

    """
    json_file = read_json_file(data_json)
    """
    Функция фильтрации по ключу = 'EXECUTED'
    """
    json_file = [d for d in json_file if 'state' in d and d['state'] == 'EXECUTED']
    """
    Функция фильтрации по ключу = 'date'. Выбирается самая последняя дата через цикл. Выводится 5 первых операций.
    """
    json_file = sorted(json_file, key=lambda x: x.get('date', ''), reverse=True)
    for i in range(0, 5):
        my_date = json_file[i]['date']
        format_date = datetime.fromisoformat(my_date).strftime('%d.%m.%Y')
        print(format_date, end=" ")
        print(json_file[i]['description'])
        """
        Функция фильтрации по ключу = 'from'. Выбирается которая имеет ключ - назанчение перевода(карта).
        """
        if json_file[i].get('from') is not None:
            print(mask_number(json_file[i]['from']), end=" -> ")
        print(mask_number(json_file[i]['to']))
        """
        Вывод в терминал.
        """
        print(json_file[i]['operationAmount']['amount'] + " " + json_file[i]['operationAmount']['currency']['name'])
        print()
main()





