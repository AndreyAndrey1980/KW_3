import json
from datetime import datetime


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def mask_number(number, mask='XXXX XX** **** XXXX'):
    if not number:
        return 'N/A'
    visible_chars = 6 + 4
    masked_number = (number[:visible_chars] + mask[-4:]) if len(number) > visible_chars else number
    return masked_number


def print_last_five_operations(operations):
    executed_operations = sorted([op for op in operations if 'state' in op and op['state'] == 'EXECUTED'],
                                 key=lambda x: x['date'], reverse=True)[:5]

    for op in executed_operations:
        formatted_date = datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        masked_from = mask_number(op.get('from'))
        masked_to = mask_number(op.get('to'))
        operation_amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['code']}"

        print(f"{formatted_date} {op['description']}")
        print(f"{masked_from} -> {masked_to}")
        print(f"{operation_amount}\n")


# Пример использования функции
file_path = 'operations.json'
data = read_json_file(file_path)
print_last_five_operations(data)