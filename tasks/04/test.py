import unittest
import solution

class Task04(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/04/example.txt"), 2)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().firstPart("./tasks/04/input.txt"), 602)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/04/example.txt"), 4)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().secondPart("./tasks/04/input.txt"), 891)

if __name__ == '__main__':
    unittest.main()
