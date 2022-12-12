import unittest
import solution

class Task09(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/09/example.txt"), 13)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/09/input.txt"), 6081)
        
    # def test_secondPart(self):
    #     self.assertEqual(solution.Solution().second_part("./tasks/09/example.txt"), 2)
        
    # def test_secondPartSolution(self):
    #     self.assertEqual(solution.Solution().second_part("./tasks/09/input.txt"), 2)

if __name__ == '__main__':
    unittest.main()
