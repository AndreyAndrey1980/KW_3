from src.utils import print_last_five_operations, mask_number, read_json_file


def main():
    # Пример использования функции
    file_path = 'operations.json'
    data = read_json_file(file_path)
    print_last_five_operations(data)

if __name__ == '__main__':
    main()

# Счёт **1234 -> Счёт **2322
# Visa Classic 1234 56** **** 7789 -> Счёт **1234

# 08.12.2019 Открытие вклада
# N/A -> Счет 90424****
# 41096.24 USD

# 07.12.2019 Перевод организации
# Visa Class**** -> Счет 35158****
# 48150.39 USD

# карта - 16
# счёт - 12