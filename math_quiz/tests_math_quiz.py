import unittest
from math_quiz import ComputeRandomInteger, ChooseRandomOperation, PerformComputation


class TestMathGame(unittest.TestCase):

    def TestComputeRandomInteger(self):
        # Test if random numbers generated are within the specified range
        MinValue = 1
        MaxValue = 10
        for Idx in range(1000):  # Test a large number of random values
            rand_num = ComputeRandomInteger(MinValue, MaxValue)
            self.assertTrue(MinValue <= rand_num <= MaxValue)

    def TestChooseRandomOperation(self):
        Operations = ('+', '-', '*')
        # Check whether the ChooseRandomOperation method selects different
        # operations.
        for Idx in range(1000):
             RandomOperator = ChooseRandomOperation()
             self.assertIn(RandomOperator, Operations)

    def TestPerformComputation(self):
            TestCases = [
                (5, 2, '+', '5 + 2', 7), (7, 2, '-', '7 - 2', 5),
                (3, 3, '*', '3 * 3', 9), (9, 4, '*', '9 * 4', 36),
                (6, 1, '-', '6 - 1', 5), (4, 4, '+', '4 + 4', 8),
            ]
            # Compare the results of the PerformComputation method with the 
            # results stored in TestCases
            for FirstNumber, SecondNumber, Operator, ExpectedProblem, ExpectedAnswer in TestCases:
                Problem, Answer = PerformComputation(FirstNumber, SecondNumber, Operator)
                self.assertEqual(Problem, ExpectedProblem)
                self.assertEqual(Answer, ExpectedAnswer)

if __name__ == "__main__":
    unittest.main()
