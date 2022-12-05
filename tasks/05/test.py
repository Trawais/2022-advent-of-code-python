import unittest
import solution

class Task05(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/05/example.txt"), 'CMZ')
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/05/input.txt"), 'VRWBSFZWM')
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/05/example.txt"), 'MCD')
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/05/input.txt"), 'RBTWJWMCF')

if __name__ == '__main__':
    unittest.main()
