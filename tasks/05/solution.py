class Solution:
    
    def __init__(self) -> None:
        self.stacks = [[]]
        self.commands = []
    
    def __getLines(self, filePath):
        file = open(filePath, 'r')
        lines = file.readlines()
        file.close()
        return lines
    
    def __parseInput(self, lines):
        reading_part = 1
        for line in lines:
            if not line.strip():
                continue
            if line.startswith(' 1 '):
                reading_part = 2
                continue
            
            if reading_part == 1:
                self.__parseAndStoreStack(line)
            else:
                self.__parseAndStoreCommand(line)
                
    def __parseAndStoreCommand(self, line):
        splitted = line.split();
        self.commands.append(
            {
                'crate_count': int(splitted[1]),
                'from_stack': int(splitted[3]) - 1,
                'to_stack': int(splitted[5]) - 1
            }
        )
        
    def __parseAndStoreStack(self, line):
        for i in range(0, len(line), 4):
            if i // 4 > len(self.stacks) - 1:
                self.stacks.append([])
            if line[i+1] != ' ':
                self.stacks[i // 4].insert(0, line[i+1])
            
    def __processCommands(self):
        for command in self.commands:
            for i in range(0, command['crate_count']):
                temp = self.stacks[command['from_stack']].pop()
                self.stacks[command['to_stack']].append(temp)
                
    def __processCommandsSecondPartWay(self):
        for command in self.commands:
            crate_count = command['crate_count']
            from_stack = command['from_stack']
            to_stack = command['to_stack']
            
            temp = self.stacks[from_stack][-crate_count:]
            self.stacks[from_stack] = self.stacks[from_stack][:-crate_count]
            self.stacks[to_stack].extend(temp)
    
    def __getTopOfStacks(self):
        result = []
        for stack in self.stacks:
            result.append(stack[-1])
        return ''.join(result)
        
    def firstPart(self, filePath):
        lines = self.__getLines(filePath)
        self.__parseInput(lines) # Will fill up self.stacks and self.commands arrays
        self.__processCommands()
                
        return self.__getTopOfStacks()
    
    def secondPart(self, filePath):
        lines = self.__getLines(filePath)
        self.__parseInput(lines) # Will fill up self.stacks and self.commands arrays
        self.__processCommandsSecondPartWay()
                
        return self.__getTopOfStacks()