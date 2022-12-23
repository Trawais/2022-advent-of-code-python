import unittest
from solution import Solution

class Task12(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(Solution().first_part("./tasks/12/example.txt"), 31)
        
    def test_firstPartSolution(self):
        self.assertEqual(Solution().first_part("./tasks/12/input.txt"), 339)
        
    def test_secondPart(self):
        self.assertEqual(Solution().second_part("./tasks/12/example.txt"), 29)
        
    def test_secondPartSolution(self):
        self.assertEqual(Solution().second_part("./tasks/12/input.txt"), 332)

if __name__ == '__main__':
    unittest.main()
