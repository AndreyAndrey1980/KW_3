import json
from datetime import datetime

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def mask_number(number, mask_sчет='Счет **1234', mask_карта='Visa Classic 123456******7789'):
    if not number:
        return 'N/A'

    if 'счет' in number.lower() or number.isdigit():
        return mask_sчет.replace('**', number[-4:])
    elif 'Visa' in number.lower() or 'Maestro' in number.lower() or 'американ экспресс' in number.lower():
        parts = number.split()
        if len(parts) >= 4 and len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 4 and len(parts[3]) == 4:
            return mask_карта.replace('1234', parts[0]).replace('56**', parts[1] + parts[2]).replace('****', parts[3])
    return number

def print_last_five_operations(operations):
    executed_operations = sorted([op for op in operations if 'state' in op and op['state'] == 'EXECUTED'],
                                  key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)[:5]

    for op in executed_operations:
        formatted_date = datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        masked_from = mask_number(op.get('from'))
        masked_to = mask_number(op.get('to'))
        operation_amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['code']}"

        print(f"{formatted_date} {op['description']}")
        print(f"{masked_from} -> {masked_to}")
        print(f"{operation_amount}\n")