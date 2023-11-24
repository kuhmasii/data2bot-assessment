import json

def test():
    input_file1 = "./data/data_1.json"
    input_file2 = "./data/data_2.json"
    output_file1 = "./schema/schema_1.json"
    output_file2 = "./schema/schema_2.json"

    instance1 = JsonFileParser(input_file1, output_file1)
    instance2 = JsonFileParser(input_file2, output_file2)
    instance1.snif_json_file()
    instance2.snif_json_file()

    print("Done! Good day Data2bots :)")

class JsonFileParser:
    """
    Parses JSON files and generates schemas based on the encountered data types.

    Attributes:
    - `in_file` (str): Input file path.
    - `out_file` (str): Output file path for the schema.

    Methods:
    - `read_json_file() -> json`: Reads the JSON file and returns its content as a JSON object.
    - `snif_json_file() -> json`: Analyzes the JSON file to generate a schema based on data types.
    - `output_json_file(schema: dict) -> bool`: Writes the generated schema to an output JSON file.
    - `get_schema(object_type: str) -> dict`: Generates a basic schema object for different data types.
    """

    def __init__(self, in_file:str, out_file:str):
        self.in_file = in_file
        self.out_file = out_file

    def read_json_file(self) -> json:
        """Reads the JSON file and returns its content as a JSON object."""
        with open(self.in_file, "r") as file:
            json_data = json.load(file)
            return json_data

    def snif_json_file(self) -> json:
        """
        Analyzes the JSON file and generates a schema based on data types.

        Returns:
        - JSON: The generated schema.
        """
        json_file = self.read_json_file()['message']
        schema = {}
        
        for key,value in json_file.items():
            # program should identify what is a string
            if isinstance(value, str): schema[key] = self.get_schema('string')

            # program should identify what is an integer
            if isinstance(value, int): schema[key] = self.get_schema('integer')

            # program should identify what is an boolean(True)
            if value == True: schema[key] = self.get_schema('true')

            # program should identify what is an boolean(False)
            if value == False: schema[key] = self.get_schema('false')

            # program should identify what is an list    
            if isinstance(value, list): schema[key] = self.get_schema('array')
            
            # program should identify what is an dict
            if isinstance(value, dict): schema[key] = self.get_schema('object')
            
            # NB: The arranging matters because of using only if block            
            # program should identify when the value in an array is a string
            if isinstance(value, list) and all(isinstance(x, str) for x in value) and value:                 
                schema[key] = self.get_schema('ENUM')

            # program should identify when the value in an array is a json type
            if isinstance(value, list) and all(isinstance(x, dict) for x in value) and value:
                schema[key] = self.get_schema('ARRAY')

        return self.output_json_file(schema)
    
    def output_json_file(self, schema: dict) -> bool:
        """
        Writes the generated schema to an output JSON file.

        Args:
        - `schema` (dict): The generated schema.

        Returns:
        - bool: True if writing is successful, False otherwise.
        """
        with open(self.out_file, "w") as file:
            json.dump(schema, file, indent=1)
            return True

    def get_schema(self, object_type: str) -> dict:
        """
        Generates a basic schema object for different data types.

        Args:
        - `object_type` (str): The type of the object.

        Returns:
        - dict: The generated schema object.
        """
        data = {
            "type": object_type,
            "tag": "",
            "description": "",
            "required": False
        }
        return data

if __name__ == "__main__":
    # Test function to demonstrate the usage of JsonFileParser
    test()
