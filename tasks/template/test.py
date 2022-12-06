import unittest
import solution

class Task{{ .Env.TASK }}(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().first_part("./tasks/{{ .Env.TASK }}/example.txt"), 1)
        
    def test_firstPartSolution(self):
        self.assertEqual(solution.Solution().first_part("./tasks/{{ .Env.TASK }}/input.txt"), 1)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().second_part("./tasks/{{ .Env.TASK }}/example.txt"), 2)
        
    def test_secondPartSolution(self):
        self.assertEqual(solution.Solution().second_part("./tasks/{{ .Env.TASK }}/input.txt"), 2)

if __name__ == '__main__':
    unittest.main()
