from src.utils import print_last_five_operations, mask_number, read_json_file


def main():
    # Пример использования функции
    file_path = 'operations.json'
    data = read_json_file(file_path)
    print_last_five_operations(data)

if __name__ == '__main__':
    main()