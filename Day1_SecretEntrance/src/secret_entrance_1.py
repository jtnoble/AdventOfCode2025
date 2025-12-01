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
        self.current_num = (self.current_num - amount) % (self.upper_bound + 1)
        return self.current_num
    
    def rotate_right(self, amount: int) -> int:
        """Increment the current value of the dial by a specifed amount, handling going over bounds"""
        self.current_num = (self.current_num + amount) % (self.upper_bound + 1)
        return self.current_num

def turn_dial(dial: Dial, user_input: str) -> bool:
    """Take in an input and turn dial accordling, return true if passing 0"""
    direction = user_input[0]
    amount = int(user_input[1:])

    match direction:
        case "L":
            new_value = dial.rotate_left(amount)
        case "R":
            new_value = dial.rotate_right(amount)

    return new_value == 0
        
if __name__ == '__main__':
    dial = Dial()
    count = 0
    
    # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            if turn_dial(dial, line):
                count += 1

    print(f'The password for part 1 of the puzzle is: {count}')

    