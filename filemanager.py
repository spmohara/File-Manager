import os

class FileManager:
    """ A class to manage various file and directory operations.

    Author
    ------
    Sean O'Hara

    Attributes
    ----------
    path: str or None
        Optional, defines the global path of a file or directory.
            ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'`` or ``'C:\\Users\\johndoe\\Documents'``

    Methods
    -------
    valid_path(path=None)
        Checks if path is a file, directory, parent directory, or includes file extension.

    valid_file(path=None)
        Checks if path points to valid file.

    file_extension(path=None)
        Gets the file extension of a path.

    create_file(path=None):
        Creates a new file.

    rename_file(path=None, new_path=None):
        Renames an existing file.

    delete_file(path=None):
        Deletes an existing file.

    clear_content(path=None):
        Clears the file content.     

    read_content(path=None):
        Reads the file content.

    write_content(content, path=None):
        Writes the provided content to a file.

    append_content(content, path=None):
        Appends the provided content to a file.

    read_line(path=None):
        Reads one line of a file.

    read_lines(path=None):
        Reads the lines of a file.

    write_lines(lines, path=None):
        Writes the provided lines to a file.

    valid_directory(path=None)
        Checks if path points to valid directory.

    parent_directory(path=None)
        Gets the parent directory of a path.

    list_directory(path=None):
        Lists a directories content.

    create_directory(path=None):
        Creates a new directory.

    rename_directory(new_path, path=None):
        Renames an existing directory.

    delete_directory(path=None):
        Deletes an existing directory.
    """
    def __init__(self, path=None):
        if path is None:
            self._path = os.getcwd()
        else:
            self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if isinstance(value, str) and self.valid_path(value):
            self._path = value
        else:
            raise ValueError('Invalid path attribute')

    def valid_path(self, path=None):
        """ Checks if path is a file, directory, parent directory, or includes file extension.

        Returns
        -------
        bool
            ``True`` if path is valid, otherwise ``False``.
        """
        if path is not None:
            self._valid_param(path, str, 'validate path')
        return os.path.isfile(path) or os.path.isdir(path) or os.path.dirname(path) or os.path.splitext(path)[1]

    def valid_file(self, path=None):
        """ Checks if path points to valid file.

        Returns
        -------
        bool
            ``True`` if file exists, otherwise ``False``.
        """
        if path is not None:
            self._valid_param(path, str, 'validate file')
        return os.path.isfile(self._get_path(path))
    
    def file_extension(self, path=None):
        """ Gets the file extension of a path.

        Returns
        -------
        str
            The file extension (if any).
        """
        if path is not None:
            self._valid_param(path, str, 'get file extension')
        return os.path.splitext(self._get_path(path))[1]

    def create_file(self, path=None):
        """ Creates a new file.

        """
        if path is not None:
            self._valid_param(path, str, 'create file')
        self._op_handler(self._get_path(path), 'write')

    def rename_file(self, new_path, path=None):
        """ Renames an existing file.

        Parameters
        ----------
        new_path: str
            The path of the new file.
        """
        self._valid_param(new_path, str, 'rename file')
        if path is not None:
            self._valid_param(path, str, 'rename file')
        self._op_handler(self._get_path(path), 'rename', new_path)
        self.path = new_path

    def delete_file(self, path=None):
        """ Deletes an existing file.

        """
        if path is not None:
            self._valid_param(path, str, 'delete file')
        self._op_handler(self._get_path(path), 'remove')

    def clear_content(self, path=None):
        """ Clears the file content.

        """
        if path is not None:
            self._valid_param(path, str, 'clear content')
        self._op_handler(self._get_path(path), 'write')

    def read_content(self, path=None):
        """ Reads the file content.

        Returns
        -------
        str
            The file content.
        """
        if path is not None:
            self._valid_param(path, str, 'read content')
        return self._op_handler(self._get_path(path))

    def write_content(self, content, path=None):
        """ Writes the provided content to a file.

        Parameters
        ----------
        content: str
            The content to write.
        """
        self._valid_param(content, str, 'write content')
        if path is not None:
            self._valid_param(path, str, 'write content')
        self._op_handler(self._get_path(path), 'write', content)

    def append_content(self, content, path=None):
        """ Appends the provided content to a file.

        Parameters
        ----------
        content: str
            The content to append.
        """
        self._valid_param(content, str, 'append content')
        if path is not None:
            self._valid_param(path, str, 'append content')
        self._op_handler(self._get_path(path), 'append', content)

    def read_line(self, path=None):
        """ Reads single line of a file.

        Returns
        -------
        str
            The line of the file.
        """
        if path is not None:
            self._valid_param(path, str, 'read line')
        return self._op_handler(self._get_path(path), 'readline')

    def read_lines(self, path=None):
        """ Reads the lines of a file.

        Returns
        -------
        list
            The lines of the file.
        """
        if path is not None:
            self._valid_param(path, str, 'read lines')
        return self._op_handler(self._get_path(path), 'readlines')

    def write_lines(self, lines, path=None):
        """ Writes the provided lines to a file.

        Parameters
        ----------
        lines: list
            The lines to write.
        """
        self._valid_param(lines, list, 'write lines')
        if path is not None:
            self._valid_param(path, str, 'write lines')
        self._op_handler(self._get_path(path), 'writelines', lines)
    
    def valid_directory(self, path=None):
        """ Checks if path points to valid directory.

        Returns
        -------
        bool
            ``True`` if directory exists, otherwise ``False``.
        """
        if path is not None:
            self._valid_param(path, str, 'validate directory')
        return os.path.isdir(self._get_path(path))
    
    def parent_directory(self, path=None):
        """ Gets the parent directory of a path.

        Returns
        -------
        str
            The parent directory (if any).
        """
        if path is not None:
            self._valid_param(path, str, 'get parent directory')
        return os.path.dirname(self._get_path(path))

    def list_directory(self, path=None):
        """ Lists the contents of a directory.

        """
        if path is not None:
            self._valid_param(path, str, 'list directory')
        return self._op_handler(self._get_path(path), 'listdir')

    def create_directory(self, path=None):
        """ Creates a new directory.

        """
        if path is not None:
            self._valid_param(path, str, 'create directory')
        self._op_handler(self._get_path(path), 'mkdir')

    def rename_directory(self, new_path, path=None):
        """ Renames an existing directory.

        Parameters
        ----------
        new_path: str
            The path of the new directory.
        """
        self._valid_param(new_path, str, 'rename directory')
        if path is not None:
            self._valid_param(path, str, 'rename directory')
        self._op_handler(self._get_path(path), 'rename', new_path)
        self.path = new_path

    def delete_directory(self, path=None):
        """ Deletes an existing directory.

        """
        if path is not None:
            self._valid_param(path, str, 'delete directory')
        self._op_handler(self._get_path(path), 'rmdir')

    def _valid_param(self, param, type_, op):
        if not (param and isinstance(param, type_)):
            raise ValueError(f'Unable to {op}: invalid parameter')

    def _get_path(self, path):
        return self._path if path is None else path

    def _op_handler(self, path, op='read', data=''):
        try:
            if op == 'listdir':
                return os.listdir(path)
            elif op == 'mkdir':
                os.mkdir(path)
            elif op == 'rename':
                os.rename(path, data)
            elif op == 'remove':
                os.remove(path)
            elif op == 'rmdir':
                os.rmdir(path)
            else:
                mode = op[0]
                with open(path, mode) as f:
                    if op == 'read':
                        return f.read()
                    elif op in ('write', 'append'):
                        f.write(data)
                    elif op == 'readline':
                        return f.readline()
                    elif op == 'readlines':
                        return f.readlines()
                    elif op == 'writelines':
                        f.writelines(data)
        except FileNotFoundError:
            raise FileNotFoundError('No such file or directory') from None
        except FileExistsError:
            raise FileExistsError('File already exists') from None
        except PermissionError:
            raise PermissionError('Insufficient file permissions') from None
        except OSError:
            raise OSError('OS error during file operation') from None
        except UnicodeDecodeError:
            raise ValueError('Unable to read file content') from None
        except Exception as e:
            raise ValueError(e) from None
