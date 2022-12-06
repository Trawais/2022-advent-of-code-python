import unittest
import solution

class Task06(unittest.TestCase):
    
    def test_firstPart(self):
        self.assertEqual(solution.Solution().both_parts('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4), 7)
        self.assertEqual(solution.Solution().both_parts('bvwbjplbgvbhsrlpgdmjqwftvncz', 4), 5)
        self.assertEqual(solution.Solution().both_parts('nppdvjthqldpwncqszvftbrmjlhg', 4), 6)
        self.assertEqual(solution.Solution().both_parts('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4), 10)
        self.assertEqual(solution.Solution().both_parts('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4), 11)
        
    def test_firstPartSolution(self):
        input_line = solution.Solution.get_input_line("./tasks/06/input.txt")
        self.assertEqual(solution.Solution().both_parts(input_line, 4), 1987)
        
    def test_secondPart(self):
        self.assertEqual(solution.Solution().both_parts('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14), 19)
        self.assertEqual(solution.Solution().both_parts('bvwbjplbgvbhsrlpgdmjqwftvncz', 14), 23)
        self.assertEqual(solution.Solution().both_parts('nppdvjthqldpwncqszvftbrmjlhg', 14), 23)
        self.assertEqual(solution.Solution().both_parts('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14), 29)
        self.assertEqual(solution.Solution().both_parts('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14), 26)
        
    def test_secondPartSolution(self):
        input_line = solution.Solution.get_input_line("./tasks/06/input.txt")
        self.assertEqual(solution.Solution().both_parts(input_line, 14), 3059)

if __name__ == '__main__':
    unittest.main()
