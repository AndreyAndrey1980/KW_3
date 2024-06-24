import json
from datetime import datetime

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
  
def mask_number(number, mask_card='**** **** **** ****', mask_account='**** **** ****'):
    if not number:
        return 'N/A'

    if 'счет' in number.lower() or number.isdigit():
        # Маска номера банковского счета
        return f"**{number[-4:]}"
    else:
        # Маска номера кредитной карты
        parts = number.split()
        card_number = parts[-1]
        # Замаскируйте номер карты, оставив видимыми первые 6 и последние 4 цифры
        hidden_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return hidden_number

def filter_by_state(operations, state):
    return [op for op in operations if 'state' in op and op['state'] == state]

def sort_by_date(operations, reverse=False):
    return sorted(operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)

def print_last_five_operations(operations):
    state = 'EXECUTED'
    reverse = True
    executed_operations = filter_by_state(operations, state)
    sorted_operations = sort_by_date(executed_operations, reverse)
    for op in sorted_operations[:5]:
        formatted_date = datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        masked_from = mask_number(op.get('from'))
        masked_to = mask_number(op.get('to'))
        operation_amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['code']}"

        print(f"{formatted_date} {op['description']}")
        print(f"{masked_from} -> {masked_to}")
        print(f"{operation_amount}\n")
