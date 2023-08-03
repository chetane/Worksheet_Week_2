import unittest
from temperature_convertor import celsius_to_farenheit

class TestTempratureConvertor(unittest.TestCase):

    def test_celsius_to_farenheit_0_32(self):
            celsius = 0
            expected = 32
            actual = celsius_to_farenheit(celsius)
            self.assertEqual(expected, actual)

    def test_celsius_to_farenheit_9_48(self):
            celsius = 9
            expected = 48.2
            actual = celsius_to_farenheit(celsius)
            self.assertEqual(expected, actual)

    def test_celsius_to_farenheit_69_156(self):
            celsius = 69
            expected = 156.2
            actual = celsius_to_farenheit(celsius)
            self.assertEqual(expected, actual)
            
            
if __name__ == '__main__':
 unittest.main()