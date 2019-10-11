import unittest

from strmatch import Finder


class FinderTestCase(unittest.TestCase):
    def setUp(self):
        self.finder = Finder

    def test_finder_cls(self):
        """Initialize Finder with a string_list or raise exception"""
        with self.assertRaises(TypeError) as context:
            finder_cls = self.finder()
        string_list = ['str', 'finder', 'example']
        finder_cls = self.finder(string_list)
        self.assertEqual(string_list, finder_cls.string_list)

    def test_match_short_list_of_strings(self):
        """Match short list of strings"""
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder_cls = self.finder(string_list)
        find_str = finder_cls.find('sad')
        expected = ['asd', 'asdd']
        self.assertEqual(find_str, expected)

    def test_match_long_list_of_strings(self):
        """Match long list of strings"""
        long_string = ['nfjte', 'wiggp', 'lqgipxuglnne', 'rdrsqztta', 'jpdcc', 'iytucm', 'jfrbbt', 'czvvtutj',
                       'xwvorizq', 'ju', 'ktdlek',
                       'yqouiypvjzdv', 'qwpmp', 'bwlzzvpmzz', 'sblqoazhx', 'doimcsggit', 'ssuqhibgecrbtvt', 'lvhtw',
                       'fcltvta', 'uxchxr', 'yzf', 'ylebsz']
        finder_cls = self.finder(long_string)
        find_str = finder_cls.find('n')
        excepted = ['nfjte', 'lqgipxuglnne']
        self.assertEqual(find_str, excepted)

        find_str = finder_cls.find('jfe')
        excepted = ['nfjte', 'lqgipxuglnne', 'jpdcc', 'jfrbbt', 'czvvtutj', 'ju',
                    'ktdlek', 'yqouiypvjzdv', 'ssuqhibgecrbtvt', 'fcltvta', 'yzf', 'ylebsz']
        self.assertEqual(find_str, excepted)

        find_str = finder_cls.find('jfeqzs')
        excepted = ['nfjte', 'lqgipxuglnne', 'rdrsqztta', 'jpdcc', 'jfrbbt', 'czvvtutj', 'xwvorizq', 'ju', 'ktdlek',
                    'yqouiypvjzdv', 'qwpmp', 'bwlzzvpmzz', 'sblqoazhx', 'doimcsggit', 'ssuqhibgecrbtvt', 'fcltvta',
                    'yzf', 'ylebsz']
        self.assertEqual(find_str, excepted)


if __name__ == '__main__':
    unittest.main()
