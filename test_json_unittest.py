import unittest
from unittest.mock import patch
from datetime import datetime
from json_operations import read_json_file, mask_number, print_last_five_operations

class TestFinancialOperations(unittest.TestCase):

    @patch('json_operations.json.load')
    def test_read_json_file(self, mock_load):
        mock_load.return_value = [{'date': '2023-01-01T12:00:00.000Z', 'description': 'Test op', 'from': '1234567890', 'to': '0987654321', 'state': 'EXECUTED', 'operationAmount': {'amount': 100, 'currency': {'code': 'RUB'}}}]
        result = read_json_file('operations.json')
        self.assertEqual(result, [{'date': '2023-01-01T12:00:00.000Z', 'description': 'Test op', 'from': '1234567890', 'to': '0987654321', 'state': 'EXECUTED', 'operationAmount': {'amount': 100, 'currency': {'code': 'RUB'}}}])

    def test_print_last_five_operations_with_empty_operations(self):
        operations = []
        with patch('builtins.print') as mock_print:
            print_last_five_operations(operations)
            mock_print.assert_not_called()

    def test_mask_number(self):
        # Тестируем маскировку номера
        self.assertEqual(mask_number(''), 'N/A')

    def test_print_last_five_operations_with_pending_operations(self):
        operations = [
            {'date': '2023-01-01T12:00:00.000Z', 'description': 'Test op 1', 'from': '1234567890', 'to': '0987654321', 'state': 'PENDING', 'operationAmount': {'amount': 100, 'currency': {'code': 'RUB'}}},
            {'date': '2023-01-02T12:00:00.000Z', 'description': 'Test op 2', 'from': '1234567890', 'to': '0987654321', 'state': 'PENDING', 'operationAmount': {'amount': 200, 'currency': {'code': 'RUB'}}},
            {'date': '2023-01-03T12:00:00.000Z', 'description': 'Test op 3', 'from': '1234567890', 'to': '0987654321', 'state': 'PENDING', 'operationAmount': {'amount': 300, 'currency': {'code': 'RUB'}}},
            {'date': '2023-01-04T12:00:00.000Z', 'description': 'Test op 4', 'from': '1234567890', 'to': '0987654321', 'state': 'PENDING', 'operationAmount': {'amount': 400, 'currency': {'code': 'RUB'}}},
            {'date': '2023-01-05T12:00:00.000Z', 'description': 'Test op 5', 'from': '1234567890', 'to': '0987654321', 'state': 'PENDING', 'operationAmount': {'amount': 500, 'currency': {'code': 'RUB'}}},
        ]
        with patch('builtins.print') as mock_print:
            print_last_five_operations(operations)
            mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()