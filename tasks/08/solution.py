class Solution:
    
    
    def __get_forest_from_file(self, filePath):
        self.forest: list[list[int]] = []
        file = open(filePath, 'r')
        for line in file.readlines():            
            row = list(map(lambda x: int(x), line.strip()))
            self.forest.append(row)
        file.close()
    
    
    # returns 1 if tree is visible
    # returns 0 if tree is NOT visible
    def __is_visible(self, irow: int, icol:int) -> int:
        # check from left
        for i in range(0, icol):
            if self.forest[irow][i] >= self.forest[irow][icol]:
                break
        else:
            return 1
        # check from right
        for i in range(icol+1, len(self.forest[0])):
            if self.forest[irow][i] >= self.forest[irow][icol]:
                break
        else:
            return 1
        # check from top
        for i in range(0, irow):
            if self.forest[i][icol] >= self.forest[irow][icol]:
                break
        else:
            return 1
        # check from bottom
        for i in range(irow+1, len(self.forest)):
            if self.forest[i][icol] >= self.forest[irow][icol]:
                break
        else:
            return 1
        
        return 0
    
    
    def __get_scenic_score(self, irow: int, icol:int) -> int:
        left = 0
        for i in reversed(range(0, icol)):
            left += 1
            if self.forest[irow][i] >= self.forest[irow][icol]:
                break
        
        right = 0
        for i in range(icol+1, len(self.forest[0])):
            right += 1
            if self.forest[irow][i] >= self.forest[irow][icol]:
                break

        top = 0
        for i in reversed(range(0, irow)):
            top += 1
            if self.forest[i][icol] >= self.forest[irow][icol]:
                break
        
        bottom = 0
        for i in range(irow+1, len(self.forest)):
            bottom += 1
            if self.forest[i][icol] >= self.forest[irow][icol]:
                break
        
        return left * right * top * bottom
    
    
    def first_part(self, filePath):
        self.__get_forest_from_file(filePath)
        visible_trees = 0
        for irow in range(0, len(self.forest)):
            for icol in range(0, len(self.forest[0])):
                visible_trees += self.__is_visible(irow, icol)
        return visible_trees
        
    
    def second_part(self, filePath):
        self.__get_forest_from_file(filePath)
        best_scenic_score = 0
        for irow in range(0, len(self.forest)):
            for icol in range(0, len(self.forest[0])):
                score = self.__get_scenic_score(irow, icol)
                if score > best_scenic_score:
                    best_scenic_score = score
        return best_scenic_score