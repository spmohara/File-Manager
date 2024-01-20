import logging
import unittest
from filemanager import FileManager

logging.basicConfig(level=logging.INFO, filename='filemanager_unittest.log', filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.fm = FileManager()
        self.cwd = self.fm.path
        self.test_file = 'filemanager.py'
        self.temp_file1 = 'file.txt'
        self.temp_file2 = 'file.csv'
        self.temp_dir1 = 'folder1'
        self.temp_dir2 = 'folder2'
        try:
            self.assertTrue(self.fm.is_directory(self.cwd))
            self.assertTrue(self.fm.is_file(self.test_file))
            self.assertTrue(self.fm.is_valid_path(self.temp_file1))
            self.assertTrue(self.fm.is_valid_path(self.temp_file2))
            self.assertTrue(isinstance(self.temp_dir1, str))
            self.assertTrue(isinstance(self.temp_dir2, str))
        except AssertionError:
            logging.error('AssertionError', exc_info=True)
            raise

    def tearDown(self):
        temp_files = [self.temp_file1, self.temp_file2]
        temp_dirs = [self.temp_dir1, self.temp_dir2]
        for temp_file, temp_dir in zip(temp_files, temp_dirs):
            if self.fm.is_file(temp_file):
                logging.info('Testing delete_file method...')
                self.fm.delete_file(temp_file)
                logging.info(f'File deleted: {temp_file}')
                self.assertNotIn(temp_file, self.fm.list_directory_contents(self.cwd))
            if self.fm.is_directory(temp_dir):
                logging.info('Testing delete_directory method...')
                self.fm.delete_directory(temp_dir)
                logging.info(f'Directory deleted: {temp_dir}')
                self.assertNotIn(temp_dir, self.fm.list_directory_contents(self.cwd))

    # --- Path Validation Methods ---

    def test_is_file(self):
        logging.info('Testing is_file method...')
        logging.info(f'File exists: {self.test_file}')
        self.assertTrue(self.fm.is_file(self.test_file))
        
    def test_is_directory(self):
        logging.info('Testing is_directory method...')
        logging.info(f'Directory exists: {self.cwd}')
        self.assertTrue(self.fm.is_directory(self.cwd))

    def test_is_valid_path(self):
        logging.info('Testing is_valid_path method...')
        logging.info(f'Path is valid: C:\\Users\\johndoe\\Documents')
        self.assertTrue(self.fm.is_valid_path('C:\\Users\\johndoe\\Documents'))

    def test_path_exists(self):
        logging.info('Testing path_exists method...')
        logging.info(f'Path exists: {self.cwd}')
        self.assertTrue(self.fm.path_exists(self.cwd))

    # --- Path Manipulation Methods ---

    def test_path_join(self):
        logging.info('Testing path_join method...')
        joined_path = self.fm.path_join(self.cwd, 'test')
        logging.info(f'Joined path: {joined_path}')
        self.assertIn('test', joined_path)

    def test_get_current_directory(self):
        logging.info('Testing get_current_directory method...')
        cwd = self.fm.get_current_directory()
        logging.info(f'Current working directory: {cwd}')
        self.assertEqual(cwd, self.cwd)

    def test_get_file_extension(self):
        logging.info('Testing get_file_extension method...')
        path = self.fm.path_join(self.cwd, self.test_file)
        file_extension = self.fm.get_file_extension(path)
        logging.info(f'File extension exists: {file_extension}')
        self.assertEqual(file_extension, '.'+self.test_file.split('.')[-1])

    def test_get_file_name(self):
        logging.info('Testing get_file_name method...')
        path = self.fm.path_join(self.cwd, self.test_file)
        file_name = self.fm.get_file_name(path)
        logging.info(f'File name exists: {file_name}')
        self.assertEqual(file_name, self.test_file)

    def test_get_parent_directory(self):
        logging.info('Testing get_parent_directory method...')
        parent_directory = self.fm.get_parent_directory()
        logging.info(f'Parent directory exists: {parent_directory}')
        self.assertIn(parent_directory, self.cwd)

    # --- File Operations Methods ---

    def test_file_ops_methods(self):
        logging.info('Testing create_file method...')
        self.fm.create_file(self.temp_file1)
        logging.info(f'File created: {self.temp_file1}')
        self.assertIn(self.temp_file1, self.fm.list_directory_contents(self.cwd))

        logging.info('Testing rename_file method...')
        self.fm.path = self.fm.path_join(self.cwd, self.temp_file1)
        self.fm.rename_file(self.temp_file2)
        logging.info(f'File renamed: {self.temp_file2}')
        self.assertIn(self.temp_file2, self.fm.list_directory_contents(self.cwd))

        # delete_file method tested in tearDown method

    # --- File Content Management Methods ---

    def test_file_content_methods(self):
        self.fm.path = self.fm.path_join(self.cwd, self.temp_file1)
        self.fm.create_file(self.temp_file1)
        logging.info(f'File created: {self.temp_file1}')
        self.assertIn(self.temp_file1, self.fm.list_directory_contents(self.cwd))

        logging.info('Testing write_content method...')
        content = 'test1\n'
        self.fm.write_content(content)
        logging.info(f'Content written to file: {content}')
        self.assertIn('test1', self.fm.read_content())

        logging.info('Testing append_content method...')
        content = 'test2\ntest3\n'
        self.fm.append_content(content)
        logging.info(f'Content appended to file: {content}')
        self.assertIn('test3', self.fm.read_content())

        logging.info('Testing read_content method...')
        content = self.fm.read_content()
        logging.info(f'File content: {content}')
        self.assertIn('test3', content)

        logging.info('Testing clear_file_content method...')
        self.fm.clear_file_content()
        logging.info(f'File cleared')
        self.assertEqual('', self.fm.read_content())

        logging.info('Testing write_line method...')
        lines = ['test4\n', 'test5\n', 'test6\n']
        self.fm.write_lines(lines)
        logging.info(f'Lines written to file: {lines}')
        self.assertIn('test6', self.fm.read_content())

        logging.info('Testing read_line method...')
        line = self.fm.read_line()
        logging.info(f'File line: {line}')
        self.assertIn(line, self.fm.read_content())

        logging.info('Testing read_all_lines method...')
        lines = self.fm.read_all_lines()
        logging.info(f'File lines: {lines}')
        self.assertIn('test', self.fm.read_content())

    # --- Directory Operations Methods ---

    def test_directory_ops_methods(self):
        logging.info('Testing list_directory_contents method...')
        dir_contents = self.fm.list_directory_contents(self.cwd)
        logging.info(f'Directory contents: {dir_contents}')
        self.assertIn(self.test_file, dir_contents)

        logging.info('Testing create_directory method...')
        self.fm.create_directory(self.temp_dir1)
        logging.info(f'Directory created: {self.temp_dir1}')
        self.assertIn(self.temp_dir1, self.fm.list_directory_contents(self.cwd))

        logging.info('Testing rename_directory method...')
        self.fm.path = self.fm.path_join(self.cwd, self.temp_dir1)
        self.fm.rename_directory(self.temp_dir2)
        logging.info(f'Directory renamed: {self.temp_dir2}')
        self.assertIn(self.temp_dir2, self.fm.list_directory_contents(self.cwd))

        # delete_directory method tested in tearDown method

if __name__ == '__main__':
    unittest.main(failfast=True)
