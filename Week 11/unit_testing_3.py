import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'BAR')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_isdigit(self):
        self.assertTrue('123'.isdigit())
"""
When an assertion fails in a unit test, Python's unittest framework provides detailed feedback about the failure. It tells you which specific test method failed, 
what the expected output was, what the actual output was, and on which line the failure occurred. In the output, a visual difference is shown between the expected and
 actual values to help you quickly identify the issue. This is useful for debugging, especially when dealing with unexpected logic or data mismatches.
 The test suite will still run the remaining tests, but the final report will indicate how many tests passed and how many failed, along with the reasons for each failure.
"""

if __name__ == '__main__':
    unittest.main()
