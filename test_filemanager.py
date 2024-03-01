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
        self.assertTrue(self.fm.is_file(self.test_file))
        
    def test_is_directory(self):
        self.assertTrue(self.fm.is_directory(self.cwd))

    def test_is_valid_path(self):
        self.assertTrue(self.fm.is_valid_path(self.test_path))

    def test_path_exists(self):
        self.assertTrue(self.fm.path_exists(self.cwd))

    # --- Path Manipulation Methods ---

    def test_path_join(self):
        joined_path = self.fm.path_join(self.test_path, self.test_file)
        self.assertIn(self.test_file, joined_path)

    def test_change_directory(self):
        par_dir = self.fm.get_parent_directory(self.cwd)
        self.fm.change_directory(par_dir)
        self.assertEqual(par_dir, self.fm.get_current_directory())
        prev_dir = self.cwd
        self.fm.change_directory(prev_dir)
        self.assertEqual(prev_dir, self.fm.get_current_directory())

    def test_get_current_directory(self):
        cwd = self.fm.get_current_directory()
        self.assertEqual(cwd, self.cwd)

    def test_get_parent_directory(self):
        parent_directory = self.fm.get_parent_directory()
        self.assertIn(parent_directory, self.cwd)

    def test_get_base_name(self):
        path = self.fm.path_join(self.cwd, self.test_file)
        base_name = self.fm.get_base_name(path)
        self.assertEqual(base_name, self.test_file)

    def test_get_file_extension(self):
        path = self.fm.path_join(self.test_path, self.test_file)
        file_extension = self.fm.get_file_extension(path)
        self.assertIn(file_extension, self.test_file)

    # --- File Operations Methods ---

    def test_file_operations_methods(self):
        
        # create_file
        self._create_file(self.temp_file1)
        
        # rename_file
        self.fm.rename_file(self.temp_file2)
        self.assertTrue(self.fm.is_file(self.temp_file2))

        # delete_file in tearDown

    # --- File Content Management Methods ---

    def test_file_content_methods(self):
        self._create_file(self.temp_file1)

        # write_content
        content = 'test1\n'
        self.fm.write_content(content)
        self.assertIn('test1', self.fm.read_content())

        # append_content
        content = 'test2\ntest3\n'
        self.fm.append_content(content)
        self.assertIn('test3', self.fm.read_content())

        # read_content
        content = self.fm.read_content()
        self.assertIn('test3', content)

        # clear_file_content
        self.fm.clear_file_content()
        self.assertEqual('', self.fm.read_content())

        # write_lines
        lines = ['test4\n', 'test5\n', 'test6\n']
        self.fm.write_lines(lines)
        self.assertIn('test6', self.fm.read_content())

        # read_line
        line = self.fm.read_line()
        self.assertIn(line, self.fm.read_content())

        # read_all_lines
        lines = self.fm.read_all_lines()
        self.assertIn('test', self.fm.read_content())

    # --- Directory Operations Methods ---

    def test_directory_operations_methods(self):
        # list_directory_contents
        contents = self.fm.list_directory_contents(self.cwd)
        self.assertIn(self.test_file, contents)

        # create_directory
        self._create_directory(self.temp_dir1)

        # rename_directory
        self.fm.rename_directory(self.temp_dir2)
        self.assertTrue(self.fm.is_directory(self.temp_dir2))

        # delete_directory in tearDown

    # --- Cleanup ---
                
    def tearDown(self):
        temp_files = [self.temp_file1, self.temp_file2]
        temp_dirs = [self.temp_dir1, self.temp_dir2]
        for temp_file, temp_dir in zip(temp_files, temp_dirs):
            if self.fm.is_file(temp_file):
                # delete_file
                self.fm.delete_file(temp_file)
                self.assertFalse(self.fm.is_file(temp_file))
            if self.fm.is_directory(temp_dir):
                # delete_directory
                self.fm.delete_directory(temp_dir)
                self.assertFalse(self.fm.is_directory(temp_dir))

    # --- Helper Methods ---

    def _create_file(self, temp_file):
        self.fm.create_file(temp_file)
        self.assertTrue(self.fm.is_file(temp_file))
        self.fm.path = self.fm.path_join(self.cwd, temp_file)

    def _create_directory(self, temp_dir):
        self.fm.create_directory(temp_dir)
        self.assertTrue(self.fm.is_directory(temp_dir))
        self.fm.path = self.fm.path_join(self.cwd, temp_dir)

if __name__ == '__main__':
    unittest.main(failfast=True)
