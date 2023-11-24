# JSON File Parser and Test Suite

This repository contains Python code to parse JSON files and generate schemas based on the data types encountered, along with a test suite to verify the functionality of the parser.

## JsonFileParser

### Purpose
The `JsonFileParser` class is designed to parse JSON files and generate schemas for their contents. It identifies different data types within the JSON structure and generates a basic schema accordingly.

### Usage
To use the `JsonFileParser`:
1. Initialize an instance of `JsonFileParser` with input and output file paths.
2. Call the `snif_json_file()` method to generate the schema based on the data types found in the JSON file.

### File Structure
main.py: Contains the JsonFileParser class for parsing JSON files and generating schemas.
test.py: Includes test cases for the functionalities of the JsonFileParser.

### Getting Started
Clone this repository.
Install Python and required dependencies (e.g., unittest).
Use the provided code snippets to parse JSON files and run the test suite.
Feel free to explore and use the code provided for JSON parsing and testing purposes!

### Test Suite - TestJsonFileParser
Purpose
The TestJsonFileParser class includes test cases to verify the functionality of the JsonFileParser methods.

### Running the Tests
To run the test suite:

Import the TestJsonFileParser class from main.py.
Execute the tests using a test runner (e.g., unittest.main())
run the test.py file

Example usage:
```python
from main import JsonFileParser

# Initialize the JsonFileParser instance
instance = JsonFileParser('./data/data_1.json', './schema/schema_1.json')

# Generate the schema
instance.snif_json_file()