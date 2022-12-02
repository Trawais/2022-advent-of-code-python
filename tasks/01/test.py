import unittest
import solution

class Task01(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/01/example.txt"), 24000)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/01/input.txt"), 69289)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/01/example.txt"), 45000)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/01/input.txt"), 205615)

if __name__ == '__main__':
    unittest.main()
