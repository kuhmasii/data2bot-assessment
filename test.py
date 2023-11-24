from unittest import TestCase, main
from main import JsonFileParser

class TestJsonFileParser(TestCase):
    """
    Test cases for the JsonFileParser class.

    Methods:
    - `setUp()`: Initializes a JsonFileParser instance for testing.
    - `test_instance_created()`: Verifies if an instance of JsonFileParser is created successfully.
    - `test_read_json_file_method()`: Checks the functionality of the read_json_file method.
    - `test_snif_json_file_method()`: Checks the functionality of the snif_json_file method.
    - `test_get_schema_method()`: Checks the functionality of the get_schema method.
    """

    def setUp(self):
        """
        Set up a JsonFileParser instance for testing.
        """
        self.ins = JsonFileParser('./data/data_1.json', './test/test.json')

    def test_instance_created(self):
        """
        Verify if an instance of JsonFileParser is created successfully.
        """
        self.assertIsInstance(self.ins, JsonFileParser)
    
    def test_read_json_file_method(self):
        """
        Check the functionality of the read_json_file method.
        """
        data = self.ins.read_json_file()

        self.assertIsInstance(data, dict)
        self.assertIn('message', data)
        self.assertTrue(data)
        
    def test_snif_json_file_method(self):
        """
        Check the functionality of the snif_json_file method.
        """
        data = self.ins.snif_json_file()

        self.assertEqual(data, True)
        self.assertTrue(data)

    def test_get_schema_method(self):
        """
        Check the functionality of the get_schema method.
        """
        data = self.ins.get_schema('test')

        self.assertIsInstance(data, dict)
        self.assertEqual(data['type'], 'test')

if __name__ == '__main__':
    main()
