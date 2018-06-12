import unittest
import fizzbuzz

class FizzBuzzTests(unittest.TestCase):

    def test_FizzBuzz_When_Default_ReturnsInput(self):
        number = 1
        result = fizzbuzz.fizzbuzz(number)
        self.assertEqual(result, str(number))

    def test_FizzBuzz_WhenDiv3_ReturnsFizz(self):
        number = 3
        result = fizzbuzz.fizzbuzz(number)
        self.assertEqual(result, 'Fizz')

    def test_FizzBuzz_WhenDiv5_ReturnsBuzz(self):
        number = 5
        result = fizzbuzz.fizzbuzz(number)
        self.assertEqual(result, 'Buzz')

    def test_FizzBuzz_WhenDiv3_AndDiv5_ReturnsFizzBuzz(self):
        number = 15
        result = fizzbuzz.fizzbuzz(number)
        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()

