import unittest
import solution

class Task10(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/10/example_1.txt"), 0)
        self.assertEqual(solution.Solution().first_part("./tasks/10/example_2.txt"), 13140)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/10/input.txt"), 13740)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().second_part("./tasks/10/example_2.txt"), None)
        # The result is written to stdout
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().second_part("./tasks/10/input.txt"), None)
        # The result is written to stdout

if __name__ == '__main__':
    unittest.main()
