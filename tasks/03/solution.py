class Solution:
    
    def __getLines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    
    def __countSumOfTheProperties(self, list):
        sum = 0
        for property in list:
            if 'a' <= property and property <= 'z':
                sum += ord(property) - 96
            if 'A' <= property and property <= 'Z':
                sum += ord(property) - 38
        return sum
    
    def firstPart(self, filePath):
        lines = self.__getLines(filePath)
        common = []
        for line in lines:
            compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]
            common.append(list(set(compartment1).intersection(compartment2))[0])
            
        return self.__countSumOfTheProperties(common)
    
    def secondPart(self, filePath):
        lines = self.__getLines(filePath)
        badges = []
        group_size = 3
        for i in range(0, len(lines), group_size):
            first_two_common = set(lines[i]).intersection(lines[i+1])
            badges.append(list(first_two_common.intersection(lines[i+2]))[0])
            
        return self.__countSumOfTheProperties(badges)