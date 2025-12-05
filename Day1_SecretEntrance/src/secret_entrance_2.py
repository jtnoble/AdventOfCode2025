import os

class Dial:
    def __init__(
            self,
            lower_bound: int = 0,
            upper_bound: int = 99,
            starting_num: int = 50
        ) -> None:
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_num = starting_num

    def rotate_left(self, amount: int) -> int:
        """Decrement the current value of the dial by a specifed amount, handling going under bounds"""
        start = self.current_num
        if start != self.lower_bound:
            first = start
        else:
            first = self.upper_bound + 1
        zeros = 0
        if amount >= first:
            zeros = 1 + (amount - first) // (self.upper_bound + 1)
        self.current_num = (self.current_num - amount) % (self.upper_bound + 1)
        return zeros
    
    def rotate_right(self, amount: int) -> int:
        """Increment the current value of the dial by a specifed amount, handling going over bounds"""
        start = self.current_num
        first = (self.upper_bound + 1 - start) % (self.upper_bound + 1)
        if first == self.lower_bound:
            first = self.upper_bound + 1
        zeros = 0
        if amount >= first:
            zeros = 1 + (amount - first) // (self.upper_bound + 1)
        self.current_num = (self.current_num + amount) % (self.upper_bound + 1)
        return zeros

def turn_dial(dial: Dial, user_input: str) -> int:
    """Take in an input and turn dial accordling, return true if passing 0"""
    direction = user_input[0]
    amount = int(user_input[1:])

    match direction:
        case "L":
            return dial.rotate_left(amount)
        case "R":
            return dial.rotate_right(amount)
        
if __name__ == '__main__':
    dial = Dial()
    count = 0
    
    # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            count += turn_dial(dial, line)

    print(f'The password for part 2 of the puzzle is: {count}')

    