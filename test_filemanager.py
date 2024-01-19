import os
from filemanager import FileManager

file_manager = FileManager()

PATH = os.getcwd()
DIR1 = PATH + '\\folder1'
DIR2 = PATH + '\\folder1'
FILE1 = PATH + '\\file1.txt'
FILE2 = PATH + '\\file2.txt'

print('\n### DIRECTORY METHODS ###')
file_manager.path = PATH
print('Path:', PATH)
print('Valid path') if file_manager.path_exists(PATH) else print('Invalid path')
print('Valid directory') if file_manager.is_directory(PATH) else print('Invalid directory')
print('Directory contents:', file_manager.list_directory_contents())

file_manager.path = DIR1
print('\nPath:', DIR1)
print('Valid path') if file_manager.path_exists(PATH) else print('Invalid path')
file_manager.create_directory()
print('Directory created')
print('Valid directory') if file_manager.is_directory(DIR1) else print('Invalid directory')
print('Parent directory:', file_manager.get_parent_directory(DIR1))
file_manager.rename_directory(DIR2)
print('Directory renamed:', DIR2)
file_manager.delete_directory()
print('Directory deleted')

print('\n### FILE METHODS ###')
file_manager.path = FILE1
print('Path:', FILE1)
print('Valid path') if file_manager.path_exists(FILE1) else print('Invalid path')
print('Valid extension') if file_manager.get_file_extension(FILE1) else print('Invalid extension')
file_manager.create_file()
print('File created')
print('Valid file') if file_manager.is_file(FILE1) else print('Invalid file')
file_manager.write_content('test1\n')
file_manager.append_content('test2\ntest3\n')
print('File content:', file_manager.read_content())
file_manager.clear_file_content()
print('File cleared')
file_manager.write_lines(['test4\n', 'test5\n', 'test6\n'])
print('File line:', file_manager.read_line())
print('File lines:', file_manager.read_all_lines())
file_manager.rename_file(FILE2)
print('File renamed', FILE2)
file_manager.delete_file()
print('File deleted')
