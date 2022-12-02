class Solution:
    
    def __sumAllCallories(self, filePath):
        file = open(filePath, 'r')
        lines = file.readlines()
        file.close()
        stripped = [s.strip() for s in lines]
        elves = []
        index = 0
        for line in stripped:
            if line:
                if len(elves) <= index:
                    elves.append(0)
                elves[index] += int(line)
            else:
                index += 1
        return elves
    
    
    def firstPart(self, filePath):
        elves = self.__sumAllCallories(filePath)
        return max(elves)
    
    def secondPart(self, filePath):
        elves = self.__sumAllCallories(filePath)
        elves.sort(reverse=True)
        return elves[0] + elves[1] + elves[2]
