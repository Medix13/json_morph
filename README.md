# JSON-MORPH

JSON-MORPH is a Python script that allows you to fetch data from an API and convert it into a different format using a mapping configuration. This README provides an overview of the script and instructions on how to use it effectively.

## Table of Contents

- [Run Locally](#prerequisites)
- [Usage](#usage)
  - [Fetching Data](#fetching-data)
  - [Converting Data](#converting-data)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Mapping Configuration](#mapping-configuration)
- [License](#license)

## Run Locally

Clone the project

```bash
git clone git@github.com:Medix13/json_morph.git
```

Go to the project directory

```bash
cd json_morph
```

Install Setup

```bash
python setup.py install
```

## Usage

JSON-MORPH provides two main operations: fetching data from an API (`get`) and converting data (`convert`) based on a mapping configuration.

### Fetching Data

To fetch data from an API and save it, use the following command:

```bash
python json_morph.py get -n <data_name> -u <api_url> -H '{"header1": "value1", "header2": "value2"}'
```

- <data_name>: Name of the data (used for saving and identifying the data).
- <api_url> (Optional): Specify the API URL for fetching data. If not provided, it uses the GET_API_URL from environment variables.
- -H (Optional): Provide HTTP headers as a dictionary for making the API request.

### Converting Data

To convert fetched data using a mapping configuration, use the following command:

```bash
python script.py convert -n <data_name> --mapping_filename <mapping_file>
```

- <data_name>: Name of the data (used for saving and identifying the data).
- --mapping_filename (Optional): Specify the filename of the mapping configuration for data conversion. Default is ./mapping.json.

## Configuration

### Environment Variables

JSON-MORPH uses environment variables for configuration. Create a .env file in the project directory and set the following variables:

- GET_API_URL: The default API URL for fetching data.

### Mapping Configuration

Define the mapping configuration in a JSON file. Ensure it matches the expected format as described in the Converting Data section.

The mapping configuration file defines how data should be transformed. You can specify this in a JSON file (e.g., mapping.json) with the following format:

```bash
{
  "output_field1": "input_path1",
  "output_field2": "input_path2",
  ...
}
```

- output_field: The name of the field in the converted data.
- input_path: The path to the corresponding field in the fetched data, using dot notation for nested fields (e.g., nested.field).

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License. See the [LICENSE ](LICENSE.md) file for details.
