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

def count_valid_ingredents_in_ranges(ranges: list[IngRange]) -> int:
    """Merges ranges and counts valid ingredients between ranges"""
    if not ranges:
        return 0

    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    merged = [IngRange(sorted_ranges[0].start, sorted_ranges[0].end)]

    for r in sorted_ranges[1:]:
        last = merged[-1]
        if r.start <= last.end:
            last.end = max(last.end, r.end)
        else:
            merged.append(IngRange(r.start, r.end))

    total = 0
    for m in merged:
        total += (m.end - m.start + 1)

    return total

            
if __name__ == '__main__':
     # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    with open(filepath, 'r') as f:
        ranges_and_ingredients = separate_ranges_and_ingredients(f.readlines())

    ranges = create_ingredient_ranges(ranges_and_ingredients[0])

    result = count_valid_ingredents_in_ranges(ranges)

    print(f"The answer is: {result}")

