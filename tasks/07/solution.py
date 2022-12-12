from file_system import Directory, File
from typing import List

class Solution:
    
    def __init__(self) -> None:
        self.root_dir = None
        self.current_dir = None
    
    def __get_lines(self, filePath) -> List[str]:
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    
    def __process_commands(self, commands: List[str]):
        for line in commands:
            if line.startswith('$'): # some command
                if line.startswith('$ cd '): # changing directory
                    self.__process_change_directory(line)
                elif line == '$ ls':
                    continue
            else: # output from previous '$ ls' command
                splitted = line.split(' ')
                if splitted[0] == 'dir':
                    new_dir = Directory(splitted[1], self.current_dir)
                    self.current_dir.child_dirs.append(new_dir)
                else:
                    new_file = File(splitted[1], splitted[0])
                    self.current_dir.child_files.append(new_file)
                        
    def __process_change_directory(self, cmd: str):
        splitted = cmd.split(' ')
        if splitted[2] == '/':
            new_dir = Directory(splitted[2], None)
            self.current_dir = new_dir
            self.root_dir = new_dir
        elif splitted[2] == '..':
            self.current_dir = self.current_dir.parrent
        else:
            next_dir = self.current_dir.get_child_dir(splitted[2])
            self.current_dir = next_dir
    
    def __calculate_dir_sizes(self, current_dir: Directory) -> int:
        if len(current_dir.child_dirs) == 0:
            current_dir.size = current_dir.total_files_size()
            return current_dir.size
        else:
            dir_size = current_dir.total_files_size()
            for dir in current_dir.child_dirs:
                dir_size += self.__calculate_dir_sizes(dir)
            current_dir.size = dir_size
        return current_dir.size
    
    def __get_all_dirs(self, current_dir: Directory):
        if len(current_dir.child_dirs) == 0:
            return [current_dir]
        else:
            temp = [current_dir]
            for dir in current_dir.child_dirs:
                temp.extend(self.__get_all_dirs(dir))
            return temp
            
        
    def first_part(self, filePath):
        commands = self.__get_lines(filePath)
        self.__process_commands(commands)
        self.__calculate_dir_sizes(self.root_dir)
        all_dirs = self.__get_all_dirs(self.root_dir)
        
        sum = 0
        for dir in all_dirs:
            if dir.size < 100000:
                sum += dir.size
        return sum
    
    def second_part(self, filePath):
        commands = self.__get_lines(filePath)
        self.__process_commands(commands)
        self.__calculate_dir_sizes(self.root_dir)
        all_dirs = self.__get_all_dirs(self.root_dir)
        
        total_disk_size = 70000000
        update_size = 30000000
        current_free_space = total_disk_size - self.root_dir.size
        needed_space = update_size - current_free_space
        
        result_size = 70000000
        for dir in all_dirs:
            if dir.size > needed_space and dir.size < result_size:
                result_size = dir.size
        return result_size
        