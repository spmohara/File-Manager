import logging
import unittest
from filemanager import FileManager

logging.basicConfig(level=logging.INFO, filename='filemanager_unittest.log', filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TestFileManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fm = FileManager()
        cls.cwd = cls.fm.path
        cls.test_file = 'filemanager.py'
        cls.test_path = 'C:\\Users\\johndoe\\Documents'
        cls.temp_file1 = 'file1.txt'
        cls.temp_file2 = 'file2.csv'
        cls.temp_dir1 = 'folder1'
        cls.temp_dir2 = 'folder2'

    def setUp(self):
        try:
            if not (self.cwd and self.fm.is_directory(self.cwd)):
                raise AssertionError(f'Current working directory {self.cwd} is invalid.')
            if not (self.test_file and self.fm.is_file(self.test_file)):
                raise AssertionError(f'Test file {self.test_file} is invalid.')
            if not (self.test_path and self.fm.is_valid_path(self.test_path)):
                raise AssertionError(f'Test path {self.test_path} is invalid.')
            for temp_file in (self.temp_file1, self.temp_file2):
                if not (temp_file and self.fm.is_valid_path(temp_file)):
                    raise AssertionError(f'Temp file {temp_file} is invalid.')
            for temp_dir in (self.temp_dir1, self.temp_dir2):
                if not (temp_dir and isinstance(temp_dir, str)):
                    raise AssertionError(f'Temp directory {temp_dir} is invalid.')
        except AssertionError as e:
            logging.error(f'Test setup failed: {e}')
            raise

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
        logging.info(f'Path is valid: {self.test_path}')
        self.assertTrue(self.fm.is_valid_path(self.test_path))

    def test_path_exists(self):
        logging.info('Testing path_exists method...')
        logging.info(f'Path exists: {self.cwd}')
        self.assertTrue(self.fm.path_exists(self.cwd))

    # --- Path Manipulation Methods ---

    def test_path_join(self):
        logging.info('Testing path_join method...')
        joined_path = self.fm.path_join(self.test_path, self.test_file)
        logging.info(f'Joined path: {joined_path}')
        self.assertIn(self.test_file, joined_path)

    def test_get_current_directory(self):
        logging.info('Testing get_current_directory method...')
        cwd = self.fm.get_current_directory()
        logging.info(f'Current working directory: {cwd}')
        self.assertEqual(cwd, self.cwd)

    def test_get_file_extension(self):
        logging.info('Testing get_file_extension method...')
        path = self.fm.path_join(self.test_path, self.test_file)
        file_extension = self.fm.get_file_extension(path)
        logging.info(f'File extension exists: {file_extension}')
        self.assertIn(file_extension, self.test_file)

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
    # delete_file test in tearDown

    def test_file_operations_methods(self):
        
        logging.info('Testing create_file method...')
        self._create_file(self.temp_file1)
        
        logging.info('Testing rename_file method...')
        self.fm.rename_file(self.temp_file2)
        logging.info(f'File renamed: {self.temp_file2}')
        self.assertTrue(self.fm.is_file(self.temp_file2))

    # --- File Content Management Methods ---

    def test_file_content_methods(self):
        self._create_file(self.temp_file1)

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
    # delete_directory test in tearDown

    def test_directory_operations_methods(self):
        logging.info('Testing list_directory_contents method...')
        contents = self.fm.list_directory_contents(self.cwd)
        logging.info(f'{self.test_file} in {contents}')
        self.assertIn(self.test_file, contents)

        logging.info('Testing create_directory method...')
        self._create_directory(self.temp_dir1)

        logging.info('Testing rename_directory method...')
        self.fm.rename_directory(self.temp_dir2)
        logging.info(f'Directory renamed: {self.temp_dir2}')
        self.assertTrue(self.fm.is_directory(self.temp_dir2))

    # --- Cleanup ---
                
    def tearDown(self):
        temp_files = [self.temp_file1, self.temp_file2]
        temp_dirs = [self.temp_dir1, self.temp_dir2]
        for temp_file, temp_dir in zip(temp_files, temp_dirs):
            if self.fm.is_file(temp_file):
                logging.info('Testing delete_file method...')
                self.fm.delete_file(temp_file)
                logging.info(f'File deleted: {temp_file}')
                self.assertFalse(self.fm.is_file(temp_file))
            if self.fm.is_directory(temp_dir):
                logging.info('Testing delete_directory method...')
                self.fm.delete_directory(temp_dir)
                logging.info(f'Directory deleted: {temp_dir}')
                self.assertFalse(self.fm.is_directory(temp_dir))

    # --- Helper Methods ---

    def _create_file(self, temp_file):
        self.fm.create_file(temp_file)
        logging.info(f'File created: {temp_file}')
        self.assertTrue(self.fm.is_file(temp_file))
        self.fm.path = self.fm.path_join(self.cwd, temp_file)

    def _create_directory(self, temp_dir):
        self.fm.create_directory(temp_dir)
        logging.info(f'Directory created: {temp_dir}')
        self.assertTrue(self.fm.is_directory(temp_dir))
        self.fm.path = self.fm.path_join(self.cwd, temp_dir)

if __name__ == '__main__':
    unittest.main(failfast=True)
