class Solution:
    
    def __getLines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    
    def firstPart(self, filePath):
        return 1
    
    def secondPart(self, filePath):
        return 2