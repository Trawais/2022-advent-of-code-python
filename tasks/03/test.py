import unittest
import solution

class Task03(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/03/example.txt"), 157)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/03/input.txt"), 7811)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/03/example.txt"), 70)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/03/input.txt"), 2)

if __name__ == '__main__':
    unittest.main()
