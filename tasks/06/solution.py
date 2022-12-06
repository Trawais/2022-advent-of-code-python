from collections import Counter

class Solution:
    
    @staticmethod
    def get_input_line(filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines[0]
    
    def both_parts(self, input, window_length):
        for i in range(window_length - 1, len(input)):
            starting_index = i - window_length + 1
            ending_index = i + 1
            temp = input[starting_index:ending_index]
            if len(set(temp)) == window_length: # convertin substring to the Set will eliminate the duplicated chars
                return i+1
        else:
            return -1
    