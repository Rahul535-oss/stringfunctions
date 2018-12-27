import unittest
import doctest
import stringfunctions


class TestUniversalID(unittest.TestCase):
    def test_to_list(self):
        self.assertEqual(stringfunctions.to_list("Hello"), ['Hello'])
        self.assertEqual(stringfunctions.to_list([]), [])

    def test_to_string(self):
        self.assertEqual(stringfunctions.to_string(1), "1")
        self.assertEqual(stringfunctions.to_string("Hello"), "Hello")
        self.assertEqual(stringfunctions.to_string(None), "None")
        self.assertEqual(stringfunctions.to_string([1, 2, 3]), "[1, 2, 3]")

    def test_is_string(self):
        self.assertTrue(stringfunctions.is_string("Hello"))
        self.assertFalse(stringfunctions.is_string(6))
        self.assertFalse(stringfunctions.is_string(None))
        self.assertFalse(stringfunctions.is_string(["A"]))

    def test_is_list(self):
        self.assertTrue(stringfunctions.is_list(["A"]))
        self.assertTrue(stringfunctions.is_list([]))
        self.assertFalse(stringfunctions.is_list("Hello"))
        self.assertFalse(stringfunctions.is_list("Hello"))

    def test_trim(self):
        self.assertEqual(stringfunctions.trim("A  B C   "), "A B C")
        self.assertEqual(stringfunctions.trim(["A   B C   ", "", "E  "]), ["A B C", "E"])
        string_with_newlines = """   A  B 
            C   """
        self.assertEqual(stringfunctions.trim(string_with_newlines), "A B C")

        self.assertRaises(BaseException, stringfunctions.trim, None)
        self.assertRaises(BaseException, stringfunctions.trim, 1)

    def test_is_empty(self):
        self.assertTrue(stringfunctions.is_empty("      "))
        self.assertTrue(stringfunctions.is_empty(""))
        self.assertTrue(stringfunctions.is_empty(None))

    def test_contains(self):
        self.assertTrue(stringfunctions.contains("Hello World", "Wo"))
        self.assertFalse(stringfunctions.contains("Hello World", "wo"))
        self.assertTrue(stringfunctions.contains("Hello World", "wo", True))

    def test_doctest(self):
        suite = unittest.TestSuite()
        suite.addTest(doctest.DocTestSuite("stringfunctions"))
        result = unittest.TextTestRunner().run(suite)
        self.assertTrue(result.wasSuccessful())


if __name__ == '__main__':
    unittest.main()

    # doctest.testfile('__init__.py')
    # doctest.testmod()
