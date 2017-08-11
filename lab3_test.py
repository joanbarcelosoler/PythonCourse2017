################################
from lab3_answers import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_shout(self):
        s = 'foo'
        self.assertEqual(shout(s), 'FOO!')
        with self.assertRaises(TypeError):
            shout(2)

    def test_reverse(self):
        self.assertEqual(reverse('FOO'), 'OOF')
        self.assertNotEqual(reverse('Foo'), 'Foo')
        with self.assertRaises(TypeError):
            reverse(2)

    def test_reversewords(self):
        s = 'hello world'
        self.assertEqual(reversewords(s), ['world', 'hello'])
        with self.assertRaises(TypeError):
            reversewords(2)

    def test_reversewordletters(self):
        s = 'hello world'
        self.assertEqual(reversewordletters(s), ['dlrow olleh'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            reversewordletters(2)


if __name__ == '__main__':
    unittest.main()
###############
