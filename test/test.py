import unittest
import doctest
import str_util


class TestUniversalID(unittest.TestCase):
    def test_to_list(self):
        self.assertEqual(str_util.to_list("Hello"), ['Hello'])
        self.assertEqual(str_util.to_list([]), [])

    def test_to_string(self):
        self.assertEqual(str_util.to_string(1), "1")
        self.assertEqual(str_util.to_string("Hello"), "Hello")
        self.assertEqual(str_util.to_string(None), "None")
        self.assertEqual(str_util.to_string([1, 2, 3]), "[1, 2, 3]")

    def test_is_string(self):
        self.assertTrue(str_util.is_string("Hello"))
        self.assertFalse(str_util.is_string(6))
        self.assertFalse(str_util.is_string(None))
        self.assertFalse(str_util.is_string(["A"]))

    def test_is_list(self):
        self.assertTrue(str_util.is_list(["A"]))
        self.assertTrue(str_util.is_list([]))
        self.assertFalse(str_util.is_list("Hello"))
        self.assertFalse(str_util.is_list("Hello"))

    def test_trim(self):
        self.assertEqual(str_util.trim("A  B C   "), "A B C")
        self.assertEqual(str_util.trim(["A   B C   ", "", "E  "]), ["A B C", "E"])
        string_with_newlines = """   A  B 
            C   """
        self.assertEqual(str_util.trim(string_with_newlines), "A B C")

        self.assertRaises(BaseException, str_util.trim, None)
        self.assertRaises(BaseException, str_util.trim, 1)

    def test_is_empty(self):
        self.assertTrue(str_util.is_empty("      "))
        self.assertTrue(str_util.is_empty(""))
        self.assertTrue(str_util.is_empty(None))

    def test_contains(self):
        self.assertTrue(str_util.contains("Hello World", "Wo"))
        self.assertFalse(str_util.contains("Hello World", "wo"))
        self.assertTrue(str_util.contains("Hello World", "wo", True))

    def test_replace_substring(self):
        self.assertEqual(str_util.replace_substring('c:\\temp', '\\', '/'), "c:/temp")
        self.assertEqual(str_util.replace_substring('c:/temp/*.*', '/', '\\'), "c:\\temp\\*.*")

    def test_doctest(self):
        suite = unittest.TestSuite()
        suite.addTest(doctest.DocTestSuite("str_util"))
        result = unittest.TextTestRunner().run(suite)
        self.assertTrue(result.wasSuccessful())


if __name__ == '__main__':
    unittest.main()
