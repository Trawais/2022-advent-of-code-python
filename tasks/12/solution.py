import os
import copy

class Solution:
    
    def __get_lines(self, filePath) -> None:
        file = open(filePath, 'r')
        lines = [list(line.strip()) for line in file.readlines()]
        file.close()
        all_starts = []
        for row in range(0, len(lines)):
            for col in range(0, len(lines[row])):
                char = lines[row][col]
                if char == 'S':
                    start = (row, col)
                    all_starts.append((row, col))
                    value = 1
                elif char == 'E':
                    end = (row, col)
                    value = 26 # equivalent for 'z' height
                elif char == 'a':
                    all_starts.append((row, col))
                    value = ord(char) - 96
                else:
                    value = ord(char) - 96
                lines[row][col] = { 'value': value, 'length': 999 }
        
        return (lines, start, end, all_starts)
    
    def __print_lines(self, lines):
        if os.environ.get('DEBUG') is None:
            return
        print()
        for row in range(0, len(lines)):
            print(row, '', end='')
            for col in range(0, len(lines[row])):
                print(chr(lines[row][col]['value'] + 96), '', "{:03d}".format(lines[row][col]['length']), ' ', sep='', end='')
            print()
    
    def __next_steps(self, lines, current: tuple[int, int]):
        steps = []
        (row, col) = current
        next_values = list(range(0, lines[row][col]['value']+2))
        #left
        if col > 0 and lines[row][col-1]['value'] in next_values:
            steps.append((row, col-1))
        #right
        if col+1 < len(lines[row]) and lines[row][col+1]['value'] in next_values:
            steps.append((row, col+1))
        #top
        if row > 0 and lines[row-1][col]['value'] in next_values:
            steps.append((row-1, col))
        #down
        if row+1 < len(lines) and lines[row+1][col]['value'] in next_values:
            steps.append((row+1, col))
        
        return steps
    
    def __find_path(self, lines, start: tuple[int, int], end: tuple[int, int]):
        stack = [start]
        visited = []
        lines[start[0]][start[1]]['length'] = 0
        
        while len(stack) > 0:
            current = stack.pop(0)
            (current_row, current_col) = current
            # self.__print_lines(lines)
            next_steps = self.__next_steps(lines, current)
            for next_step in next_steps:
                (next_row, next_col) = next_step
                if lines[current_row][current_col]['length'] + 1 < lines[next_row][next_col]['length']:
                    lines[next_row][next_col]['length'] = lines[current_row][current_col]['length'] + 1
                if next_step not in visited and next_step not in stack:
                    stack.append(next_step)
            visited.append(current)
        
        return lines[end[0]][end[1]]['length']
    
    def first_part(self, filePath):
        (lines, start, end, _) = self.__get_lines(filePath)
        return self.__find_path(lines, start, end)

    def second_part(self, filePath):
        (lines, start, end, all_starts) = self.__get_lines(filePath)
        results: set[int] = set()
        
        for start in all_starts:
            results.add(self.__find_path(copy.deepcopy(lines), start, end))
            if os.environ.get('DEBUG') is not None:
                print('All routes so far:', results)
        return min(results)
