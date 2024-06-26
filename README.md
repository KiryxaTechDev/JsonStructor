# JsonStructor Library

The `JsonStructor` library is a Python package that simplifies working with JSON files. It provides methods to read, write, add, remove, and replace elements in a JSON file.

## Installation

You can install the `JsonStructor` library directly from PyPI:

```bash
pip install JsonStructor
```

## Features

- Easy reading and writing of JSON files.
- Ability to add new key-value pairs.
- Option to remove existing keys.
- Functionality to replace values for existing keys.

## Usage

### Initialization

Import the `JsonFile` class from the `JsonStructor` package and initialize it with the path to your JSON file.

```python
from JsonStructor import JsonFile

json_file = JsonFile('path/to/your/file.json')
```

### Reading Content

To read content from a JSON file, use the `get` method.

```python
content = json_file.get()
print(content)
```

### Writing Content

To write content to a JSON file, use the `set` method with a dictionary.

```python
data = {'key': 'value'}
json_file.set(data)
```

### Adding New Key-Value Pairs

To add a new key-value pair to a JSON file, use the `add_new_key` method.

```python
json_file.add_new_key('new_key', 'new_value')
```

### Removing Key-Value Pairs

To remove an existing key-value pair from a JSON file, use the `remove_key` method.

```python
json_file.remove_key('key_to_remove')
```

## Error Handling

The `JsonStructor` library includes error handling for common issues such as non-existent files or invalid JSON content.

## Documentation

Each method in the `JsonFile` class has detailed docstrings with parameters, return types, and raised exceptions information.

## Examples

Below are some examples demonstrating how to use the `JsonStructor` library:

### Reading from a File

```python
# Initialize the JsonFile object
json_file = JsonFile('data.json')

# Read data from the file
data = json_file.get()
print(data)
```

### Writing to a File

```python
# Initialize the JsonFile object
json_file = JsonFile('data.json')

# Write new data to the file
json_file.set({'new_key': 'new_value'})
```

### Adding a New Key

```python
# Initialize the JsonFile object
json_file = JsonFile('data.json')

# Add a new key-value pair
json_file.add_new_key('another_key', 'another_value')
```

### Removing an Existing Key

```python
# Initialize the JsonFile object
json_file = JsonFile('data.json')

# Remove an existing key
json_file.remove_key('key_to_remove')
```

For more information and advanced usage, refer to the docstrings provided within the `JsonStructor.py` module.
```

This markdown document can be used as part of your project's README.md or as standalone documentation for users who want to install and use the `JsonStructor` library.