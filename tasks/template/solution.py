class Solution:
    
    def __get_lines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    
    def first_part(self, filePath):
        pass
    
    def second_part(self, filePath):
        pass