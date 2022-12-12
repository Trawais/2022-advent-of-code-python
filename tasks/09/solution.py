class Solution:

    def __init__(self) -> None:
        # self.grid: list[list[bool]] = [[]] # we probably do not need this
        self.head: dict[str, int] = { 'x': 0, 'y': 0 }
        self.tail: dict[str, int] = { 'x': 0, 'y': 0 }
        self.visited: set[tuple[int, int]] = set()

    def __get_lines(self, filePath):
        file = open(filePath, 'r')
        motions = []
        for line in file.readlines():
            stripped = line.strip()
            splitted = stripped.split(' ')
            motions.append({ 'direction': splitted[0], 'steps': int(splitted[1]) })
        file.close()
        return motions

    def __move_tail(self):
        xdiff = self.head['x'] - self.tail['x']
        ydiff = self.head['y'] - self.tail['y']
        if ydiff == 0 and abs(xdiff) == 2:
            self.tail['x'] = int(self.tail['x'] + 0.5 * xdiff)
        elif xdiff == 0 and abs(ydiff) == 2:
            self.tail['y'] = int(self.tail['y'] + 0.5 * ydiff)
        elif abs(ydiff) == 1 and abs(xdiff) == 2:
            self.tail['x'] = int(self.tail['x'] + 0.5 * xdiff)
            self.tail['y'] = self.head['y']
        elif abs(xdiff) == 1 and abs(ydiff) == 2:
            self.tail['x'] = self.head['x']
            self.tail['y'] = int(self.tail['y'] + 0.5 * ydiff)

    def first_part(self, filePath):
        motions = self.__get_lines(filePath)
        for motion in motions:
            for i in range(0, motion['steps']):
                if motion['direction'] == 'R':
                    self.head['x'] += 1
                elif motion['direction'] == 'L':
                    self.head['x'] -= 1
                elif motion['direction'] == 'U':
                    self.head['y'] += 1
                else: # 'D'
                    self.head['y'] -= 1
                self.__move_tail()
                self.visited.add((self.tail['x'], self.tail['y']))
        return len(self.visited)

    def second_part(self, filePath):
        pass