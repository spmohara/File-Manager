# File Manager

# Description
A class to facilitate path management and file operations for common file-related tasks.

Methods can be split into the following groups:
- Path Validation (e.g., is_file, is_directory)
- Path Manipulation (e.g., path_join, get_file_extension)
- File Operations (e.g., create_file, delete_file)
- File Content Management (e.g., read_content, write_content)
- Directory Operations (e.g., create_directory, delete_directory)

# Usage
## Instantiation using current working directory (default)
```python
from filemanager import FileManager

file_manager = FileManager()
```

## Instantiation using path attribute
```python
from filemanager import FileManager

file_manager = FileManager(path='C:\\Users\\johndoe\\Documents')
```

## Attributes
### Get path
- Gets the global path used for all methods.
```python
file_manager.path
```

### Set path
- Defines the global path used for all methods.
```python
file_manager.path = 'C:\\Users\\johndoe\\Documents'
```

## Methods
- <ins>Note</ins>: All **path** parameters are optional if using the **path** attribute.
### Path Validation
#### Checks if a path points to a file.
```python
file_manager.is_file(path='C:\\Users\\johndoe\\Documents\\file.txt')
```

#### Checks if a path points to a directory.
```python
file_manager.is_directory(path='C:\\Users\\johndoe\\Documents')
```

#### Checks if path is a file, directory, parent directory, or includes file extension.
```python
file_manager.is_valid_path(path='C:\\Users\\johndoe')
```
- This method is primarily intended for validating path syntax, not existence (see path_exists method below).

#### Checks if a path pointing to a file or directory exists.
```python
file_manager.path_exists(path='C:\\Users\\johndoe\\Documents\\file.txt')
```

### Path Manipulation
#### Joins multiple path components into a single path.
```python
file_manager.path_join('C:\\Users\\johndoe\\Documents', 'file.txt')
```

#### Changes the current working directory.
```python
file_manager.change_directory(path='C:\\Users\\johndoe')
```

#### Returns the current working directory path.
```python
file_manager.get_current_directory()
```

#### Returns the parent directory of a path (if any).
```python
file_manager.get_parent_directory(path='C:\\Users\\johndoe\\Documents')
```

#### Returns the base name of a path (if any).
```python
file_manager.get_base_name(path='C:\\Users\\johndoe\\Documents\\file.txt')
```

#### Returns the file extension of a path (if any).
```python
file_manager.get_file_extension(path='C:\\Users\\johndoe\\Documents\\file.txt')
```

### File Operations
#### Creates a new file.
```python
file_manager.create_file(path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Renames an existing file.
```python
file_manager.rename_file(new_path='C:\\Users\\johndoe\\Documents\\file2.txt', path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Deletes an existing file.
```python
file_manager.delete_file(path='C:\\Users\\johndoe\\Documents\\file2.txt')
```

### File Content Management
#### Reads the file content.
```python
file_manager.read_content(path='C:\\Users\\johndoe\\Documents\\file.txt')
```

#### Writes the provided content to a file.
```python
file_manager.write_content(content='test1\n', path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Appends the provided content to a file.
```python
file_manager.append_content(content='test2\ntest3\n', path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Reads single line of a file.
```python
file_manager.read_line(path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Reads all lines of a file.
```python
file_manager.read_all_lines(path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Writes the provided lines to a file.
```python
file_manager.write_lines(lines=['test4\n', 'test5\n', 'test6\n'], path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

#### Clears the file content.
```python
file_manager.clear_file_content(path='C:\\Users\\johndoe\\Documents\\file1.txt')
```

### Directory Operations
#### Lists the contents of a directory.
```python
file_manager.list_directory_contents(path='C:\\Users\\johndoe\\Documents')
```

#### Creates a new directory.
```python
file_manager.create_directory(path='C:\\Users\\johndoe\\Documents\\folder1')
```

#### Renames an existing directory.
```python
file_manager.rename_directory(new_path='C:\\Users\\johndoe\\Documents\\folder2', path='C:\\Users\\johndoe\\Documents\\folder1')
```

#### Deletes an existing directory.
```python
file_manager.delete_directory(path='C:\\Users\\johndoe\\Documents\\folder2')
```

# Dependencies
- Python 3.6 or above

# License
Licensed under the [MIT License](LICENSE)