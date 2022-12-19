from monkey import Monkey
import math
import os

class Solution:
    def __init__(self) -> None:
        self.monkeys: list[Monkey] = []
        self.debug = False if os.environ.get('DEBUG') == None else True
    
    def __get_input(self, filePath) -> None:
        file = open(filePath, 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        for i in range(0, len(lines), 7):
            items = [int(item) for item in lines[i+1].split(': ')[1].split(', ')]
            (operator, value) = lines[i+2].split('old ')[1].split(' ')
            if operator == '*' and value == 'old':
                operator = '^'
                value = 2
            else:
                value = int(value)
            divisible_by = int(lines[i+3].split('by ')[1])
            if_true = int(lines[i+4].split('monkey ')[1])
            if_false = int(lines[i+5].split('monkey ')[1])
            new_monkey = Monkey(items, operator, value, divisible_by, if_true, if_false)
            self.monkeys.append(new_monkey)
    
    def __print_pretty_output(self, rounds: int):
        if self.debug:
            print('State After', rounds, 'rounds')
            for index, monkey in enumerate(self.monkeys):
                print('monkey:', index, 'items:', monkey.items, 'items inspected:', monkey.inspected_items_counter)
            
    def __print_pretty_output_part_2(self, rounds: int):
        if self.debug:
            print('State After', rounds, 'rounds')
            for index, monkey in enumerate(self.monkeys):
                print('monkey:', index, 'items inspected:', monkey.inspected_items_counter)
    
    def __get_final_result(self) -> int:
        inspected_items = [monkey.inspected_items_counter for monkey in self.monkeys]
        inspected_items.sort(reverse=True)
        return inspected_items[0] * inspected_items[1]
    
    def first_part(self, filePath) -> int:
        self.__get_input(filePath)
        rounds = 20
        for round in range(0, rounds):
            for monkey in self.monkeys:
                while len(monkey.items) > 0:
                    item = monkey.items.pop(0)
                    item = monkey.inspect_an_item(item)
                    item = monkey.get_borred(item)
                    next_monkey = monkey.throw_item_to_monkey(item)
                    self.monkeys[next_monkey].items.append(item)
        
        self.__print_pretty_output(rounds)
            
        return self.__get_final_result()
    
    def second_part(self, filePath) -> int:
        self.__get_input(filePath)
        modulo = math.prod([monkey.divisible_by for monkey in self.monkeys])
        rounds = 10000
        for round in range(0, rounds):
            if self.debug and round % 100 == 0:
                print('Round:', round)
            for monkey in self.monkeys:
                while len(monkey.items) > 0:
                    item = monkey.items.pop(0)
                    item = monkey.inspect_an_item(item)
                    item = item % modulo # decreasing worry level
                    next_monkey = monkey.throw_item_to_monkey(item)
                    self.monkeys[next_monkey].items.append(item)
        
        self.__print_pretty_output_part_2(rounds)
        
        return self.__get_final_result()