# Change Log

## Version 0.0.9
Fized bug with ModuleNotFoundError.

## Version 0.0.8
Refactoring the lbrary.

## Version 0.0.7
Added more exceptions.

## Version 0.0.6
Added `Exceptions` package.

## Version 0.0.5
Support `JsonUnion`.

## Version 0.0.4
### Overview
Added the `JsonUnion` class is designed to merge multiple JSON files or dictionaries into a single JSON file, with an option to handle duplicate keys.

### Features
Merge multiple JSON sources.
Optional handling of duplicate keys.

### Usage

#### Initialization
Create an instance of JsonUnion by passing the JSON sources and the output file path. Optionally, set replace_duplicates to True to enable replacing duplicate keys.
```Python
json_union = JsonUnion('file1.json', {'key': 'value'}, JsonFile('file2.json'), 'output.json', replace_duplicates=True)
```

#### Merging
Call the `merge()` method to perform the merge operation.
```Python
json_union.merge()
```
If replace_duplicates is set to False, a KeyError will be raised upon encountering duplicate keys.

## Version 0.0.3
Added access to nested `JsonFile` properties.

## Versoin 0.0.2
Added `update_key` method to `JsonFile` class.

## Version 0.0.1
Initional repository.