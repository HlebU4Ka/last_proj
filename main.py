from units import read_json_file, data_json
from datetime import datetime
def mask_number(sub):
    my_list = sub.split(" ") # Массив из слов
    card_number = my_list[-1] # Последние цифры
    if (my_list[0] != "Счет"):
        card_number = card_number[:6] + "*" * 6 + card_number[12:]
        # TODO: Разбить по 4, вставить пробелы между ними
    else:
        card_number = "**" + card_number[-4:]
    my_list[-1] = card_number
    return " ".join(my_list)
def main():
    json_file = read_json_file(data_json)
    json_file = [d for d in json_file if 'state' in d and d['state'] == 'EXECUTED']
    json_file = sorted(json_file, key= lambda x: x.get('date', ''), reverse=True)
    for i in range(0, 5):
        my_date = json_file[i]['date']
        format_date = datetime.fromisoformat(my_date).strftime('%d.%m.%Y')
        print(format_date, end=" ")
        print(json_file[i]['description'])
        if json_file[i].get('from') is not None:
            print(mask_number(json_file[i]['from']), end=" -> ")
        print(mask_number(json_file[i]['to']))
        print(json_file[i]['operationAmount']['amount'] + " " + json_file[i]['operationAmount']['currency']['name'])
        print()
main()





