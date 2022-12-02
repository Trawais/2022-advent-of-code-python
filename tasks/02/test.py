import unittest
import solution

class Task02(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/02/example.txt"), 15)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/02/input.txt"), 11767)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/02/example.txt"), 12)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/02/input.txt"), 13886)

if __name__ == '__main__':
    unittest.main()
