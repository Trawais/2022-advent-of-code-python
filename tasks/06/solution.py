class Solution:
    
    @staticmethod
    def get_input_line(filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines[0]
    
    # this method has been refactored by openAI chatbot
    # Here are his comments
    # * I added type hints to the method signature of the both_parts method to make it more readable.
    # * I simplified the loop to iterate over the string using a sliding window of size window_length, and I removed the unnecessary index calculations.
    # * I added a check to ensure that the substring contains all unique characters before returning the ending index of the window.
    def both_parts(self, input: str, window_length: int) -> int:
        for i in range(len(input) - window_length + 1):
            temp = input[i:i+window_length]
            if len(set(temp)) == window_length:
                return i + window_length
    