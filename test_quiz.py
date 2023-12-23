import unittest
from main import addition, subtraction, multiplication, division, questions

class TestQuiz(unittest.TestCase):

    def test_addition(self):
        self.assertAlmostEqual(addition(5, 5), 10)
        self.assertAlmostEqual(addition(-5, -5), -10)
        self.assertAlmostEqual(addition(5, -5), 0)

    def test_subtraction(self):
        self.assertAlmostEqual(subtraction(6, 6), 0)
        self.assertAlmostEqual(subtraction(15, 3), 12)
        self.assertAlmostEqual(subtraction(1, 5), -4)

    def test_multiplication(self):
        self.assertGreater(multiplication(2, 3), 5)
        self.assertLess(multiplication(-2, 4), 0)

    def test_division(self):
        self.assertAlmostEqual(division(9, 3), 3)
        self.assertAlmostEqual(division(20, 5), 4)
        with self.assertRaises(ValueError):
            division(1, 0)

    def test_questions(self):
        operators = ['+', '-', '*', '/']
        for operator in operators:
            with self.subTest(operator=operator):
                expression, answer = questions(operator)
                self.assertRegex(expression, r'\d+\s[+\-*\/]\s\d+')
                self.assertIsInstance(answer, (int, float))

if __name__ == '__main__':
    unittest.main()
