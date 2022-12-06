class Solution:
    
    def __readLines(self, filePath):
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return [line.split(' ') for line in lines]
        
    def firstPart(self, filePath):
        lines = self.__readLines(filePath)
        
        your_move_mapping = {
            'X': 1, # Rock
            'Y': 2, # Paper
            'Z': 3  # Scissors
        }
        
        # Opponents move - A: Rock, B: Paper, C Scissors
        
        score_map = {
            1: { 'A': 3, 'B': 0, 'C': 6 }, # Rock
            2: { 'A': 6, 'B': 3, 'C': 0 }, # Paper
            3: { 'A': 0, 'B': 6, 'C': 3 }  # Scissors
        }
        
        score = 0
        
        for line in lines:
            opponent_move = line[0]
            your_move = your_move_mapping[line[1]]
        
            score += your_move
            score += score_map[your_move][opponent_move]
            
        return score
    
    def secondPart(self, filePath):
        lines = self.__readLines(filePath)
        
        opponent_move_mapping = {
            'A': 1, # Rock
            'B': 2, # Paper
            'C': 3, # Scissors
        }
        
        needed_result_map = {
            'X': 0, # you need to lose
            'Y': 3, # draw
            'Z': 6, # you need to win
        }
        
        needed_move_map = { # now the opponent is the first and my move is calculated based on needed result
            1: { 3: 1, 6: 2, 0: 3 }, # Rock
            2: { 0: 1, 3: 2, 6: 3 }, # Paper
            3: { 6: 1, 0: 2, 3: 3 }  # Scissors
        }
        
        score = 0
        
        for line in lines:
            opponent_move = opponent_move_mapping[line[0]]
            needed_result = needed_result_map[line[1]]
            my_move_will_be = needed_move_map[opponent_move][needed_result]
        
            score += my_move_will_be
            score += needed_result
            
        return score
