class Solution:
    
    def __getLines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        splitted = [line.split(',') for line in lines]
        pairs = []
        for line in splitted:
            pairs.append(
                [
                    [int(s) for s in line[0].split('-')],
                    [int(s) for s in line[1].split('-')]
                ]
            )
        return pairs
    
    def firstPart(self, filePath):
        pairs = self.__getLines(filePath)
        fully_overlaps = 0
        for pair in pairs:
            first = pair[0]
            second = pair[1]
            first_set = set(range(first[0], first[1] + 1))
            second_set = set(range(second[0], second[1] + 1))
            
            if len(first_set.intersection(second_set)) == min([len(first_set), len(second_set)]):
                fully_overlaps += 1
                
        return fully_overlaps
    
    def secondPart(self, filePath):
        pairs = self.__getLines(filePath)
        overlaps = 0
        for pair in pairs:
            first = pair[0]
            second = pair[1]
            first_set = set(range(first[0], first[1] + 1))
            second_set = set(range(second[0], second[1] + 1))
            
            if first_set.intersection(second_set):
                overlaps += 1
            
        return overlaps