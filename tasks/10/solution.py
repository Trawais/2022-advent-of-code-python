class Solution:
    
    def __init__(self) -> None:
        self.x_register: int = 1
        self.cycle: int = 0
    
    def __get_lines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    
    def first_part(self, filePath):
        lines = self.__get_lines(filePath)
        
        signal_strengths: int = 0
        value = None
        i = 0
        while i < len(lines):
            self.cycle += 1
            if self.cycle % 40 == 20:
                signal_strengths += self.cycle * self.x_register
            line = lines[i]
            if line == 'noop':
                i += 1
                continue
            if value is None:
                (_, value) = line.split(' ')
                # we need to process same command twice so we are going to keep the same i
                continue
            else:
                self.x_register += int(value)
                value = None
                i += 1
        
        return signal_strengths
    
    def second_part(self, filePath):
        print('\n') # prettify the output
        lines = self.__get_lines(filePath)
        
        value = None
        i = 0
        while i < len(lines):
            
            sprite = [self.x_register-1, self.x_register, self.x_register+1]
            if (self.cycle % 40) in sprite:
                print('#', end='')
            else:
                print('.', end='')

            if self.cycle % 40 == 39:
                print()
                
            self.cycle += 1
            
            line = lines[i]
            if line == 'noop':
                i += 1
                continue
            if value is None:
                (_, value) = line.split(' ')
                # we need to process same command twice so we are going to keep the same i
                continue
            else:
                self.x_register += int(value)
                value = None
                i += 1