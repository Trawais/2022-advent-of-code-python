import operator
import math

class Monkey:
    def __init__(self,
                 items: list[int],
                 operator: str,
                 value: int,
                 divisible_by: int,
                 if_true: int,
                 if_false: int
                 ) -> None:
        self.items: list[int] = items
        self.operator: str = operator
        self.value: int = value
        self.divisible_by: int = divisible_by
        self.if_true: int = if_true
        self.if_false: int = if_false
        self.inspected_items_counter: int = 0

        
    def inspect_an_item(self, item: int):
        operators = {
            '*': operator.mul,
            '+': operator.add,
            '^': operator.pow
        }
        self.inspected_items_counter += 1
        return operators[self.operator](item, self.value)
        
    def get_borred(self, item: int):
        return item // 3
    
    def throw_item_to_monkey(self, item: int) -> int:
        if item % self.divisible_by == 0:
            return self.if_true
        return self.if_false
