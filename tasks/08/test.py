import unittest
import solution

class Task08(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/08/example.txt"), 21)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/08/input.txt"), 1785)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().second_part("./tasks/08/example.txt"), 8)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().second_part("./tasks/08/input.txt"), 345168)

if __name__ == '__main__':
    unittest.main()
