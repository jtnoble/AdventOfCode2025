from dataclasses import dataclass
import os


@dataclass
class IngRange:
    start: int
    end: int

    @classmethod
    def from_string(cls, user_range: str) -> "IngRange":
        start, end = user_range.split("-")
        return cls(int(start), int(end))

def separate_ranges_and_ingredients(lines: str) -> list[list,list]:
    """String of inputs where ranges are first and ingredients are second, separated by an extra new line"""
    isRanges = True
    ranges = []
    ingredients = []
    for line in lines:
        if line == "\n":
            isRanges = False
            continue

        line = line.strip("\n")
        
        if isRanges:
            ranges.append(line)
        else:
            ingredients.append(int(line))

    return [ranges, ingredients]

def create_ingredient_ranges(ranges: list) -> list[IngRange]:
    """Turn ranges into IngRange objects"""
    return [IngRange.from_string(r) for r in ranges]

def ingredient_in_range(ranges: list[IngRange], ingredient: int) -> bool:
    for r in ranges:
        if r.start <= ingredient <= r.end:
            return True
    return False

def count_ingredients_in_range(ranges: list[IngRange], ingredients: list[int]) -> int:
    count = 0
    for ingredient in ingredients:
        if ingredient_in_range(ranges, ingredient):
            count += 1
    return count
           
            
if __name__ == '__main__':
     # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(filepath, 'r') as f:
        ranges_and_ingredients = separate_ranges_and_ingredients(f.readlines())

    ranges = create_ingredient_ranges(ranges_and_ingredients[0])
    ingredients = ranges_and_ingredients[1]

    result = count_ingredients_in_range(ranges, ingredients)
    print(f"The answer is: {result}")

