from __future__ import annotations # This is here because we wna to type hint class itself

class Directory:
    def __init__(self, name: str, parrent_dir: Directory=None) -> None:
        self.name: str = name
        self.parrent: Directory|None = parrent_dir
        self.child_dirs: list[Directory] = []
        self.child_files: list[File] = []
        self.size: int = 0
        
    def add_child_dir(self, new_dir: Directory):
        filtered = list(filter(lambda dir: dir.name == new_dir.name, self.child_dirs))
        if len(filtered) == 0:
            self.child_dirs.append(new_dir)
    
    def get_child_dir(self, dir_name: str):
        return list(filter(lambda dir: dir.name == dir_name, self.child_dirs))[0]
    
    def total_files_size(self) -> int:
        sum = 0
        for file in self.child_files:
            sum += int(file.size)
        return sum
        
class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size