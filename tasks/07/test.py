import unittest
import solution

class Task07(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/07/example.txt"), 95437)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/07/input.txt"), 1611443)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().second_part("./tasks/07/example.txt"), 24933642)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().second_part("./tasks/07/input.txt"), 2)

if __name__ == '__main__':
    unittest.main()
