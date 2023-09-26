import os
import json
import requests
import argparse
import sys
from dotenv import load_dotenv
import art
from termcolor import colored
import ast

# Load environment variables from a .env file
load_dotenv()

# Get the API URL from environment variables
GET_API_URL = os.getenv('GET_API_URL')

# Define directories for storing data
DATA_DIRECTORY = './data/get/'
CONVERTED_DATA_DIRECTORY = './data/convert_data/'

# Define a class to hold data configuration
class DataConfig:
    def __init__(self, data_name, mapping_filename):
        self.data_name = data_name
        self.mapping_filename = mapping_filename

def save_data(data_name, data):
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    filename = os.path.join(DATA_DIRECTORY, f'{data_name}.json')
    
    with open(filename, 'w', encoding='utf-8') as writeJSON:
        json.dump(data, writeJSON, ensure_ascii=False)

def get_data_and_save(config, args):
    try:
        url = args.url or GET_API_URL 
        headers = args.headers if args.headers else None
        response = requests.get(url , headers=headers)
    
        if response.status_code == 200:
            data = response.json()
            save_data(config.data_name, data)
            print(f'Data saved successfully as {config.data_name}.json')
        else:
            raise Exception(f'Failed to retrieve data. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'An error occurred: {e}')
        sys.exit(1)

def convert_data(config, data):
    destination_folder = CONVERTED_DATA_DIRECTORY
    os.makedirs(destination_folder, exist_ok=True)

    if isinstance(data, list):
        for item in data:
            converted_item = {}
            with open(config.mapping_filename, 'r') as mapping_file:
                mapping = json.load(mapping_file)
            
            for output_field, input_path in mapping.items():
                # Handle nested keys using get_nested_value function
                input_data = get_nested_value(item, input_path)

                converted_item[output_field] = input_data

            user_filename = input('Enter a filename for the converted data (without ".json"): ')
            filename = os.path.join(destination_folder, f'{user_filename}.json')
            with open(filename, "w", encoding="utf-8") as writeJSON:
                json.dump(converted_item, writeJSON, ensure_ascii=False)
        print(f'Conversion for {config.data_name} done!')
    else:
        print('Data is not in the expected format. It should be a list of items.')

def get_nested_value(data, nested_key):
    keys = nested_key.split('.')
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

def main():
    logo = art.text2art('JSON-MORPH', font='doom')
    colored_logo = colored(logo, 'red')
    print(colored_logo)

    parser = argparse.ArgumentParser(
    description='Fetch and convert data',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter  # Include default values in help    
    )

    # Operation choice
    parser.add_argument(
        'operation',
        choices=['get', 'convert'],
        help='Specify the operation to perform: "get" to fetch data or "convert" to transform data.'
    )

    # Data name
    parser.add_argument(
        '-n', '--data_name',
        help='Name of the data. This name will be used for saving and identifying the data.'
    )

    # Mapping filename
    parser.add_argument(
        '--mapping_filename',
        default=None,
        help='Specify the filename of the mapping configuration for data conversion.'
    )

    # API URL
    parser.add_argument(
        '-u', '--url',
        default=GET_API_URL,
        help='Specify the API URL for fetching data. (Default: GET_API_URL from environment variables)'
    )

    # Headers as a dictionary
    parser.add_argument(
        '-H', '--headers',
        type=ast.literal_eval,
        default={},
        help='Provide HTTP headers as a dictionary for making the API request.'
    )


    args = parser.parse_args()
    
    if args.operation == 'get':
        data_name = args.data_name or input('Please give the name of the data: ').lower()
        config = DataConfig(data_name, None)

        get_data_and_save(config, args)
    elif args.operation == 'convert':
        data_name = args.data_name or input('Please give the name of the data (or press Enter to use the default): ').lower()
        mapping_filename = args.mapping_filename or './mapping.json'
        
        if not os.path.exists(mapping_filename):
            print(f'Mapping file ({mapping_filename}) not found.')
            return
        
        config = DataConfig(data_name, mapping_filename)

        # Load data from the source file
        source_path = os.path.join(DATA_DIRECTORY, f'{config.data_name}.json')
        with open(source_path, 'r') as f:
            data = json.load(f)

        convert_data(config, data)
    else:
        print('Invalid operation. Choose either "get" or "convert."')

if __name__ == "__main__":
    main()
