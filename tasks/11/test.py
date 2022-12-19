import unittest
import solution

class Task11(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/11/example.txt"), 10605)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/11/input.txt"), 66124)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().second_part("./tasks/11/example.txt"), 2713310158)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().second_part("./tasks/11/input.txt"), 19309892877)

if __name__ == '__main__':
    unittest.main()
