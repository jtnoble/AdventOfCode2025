def split_number(num: int) -> list[str] | None:
    """Split number into two separate strings down the middles
    E.g., 123123 -> ["123", "123"]
    Returns None if odd
    """
    num_str = str(num)
    length = len(num_str)
    split_str = [num_str[0:length//2], num_str[length//2:length]]

    if len(split_str[0]) != len(split_str[1]):
        return None
    return split_str

def check_sides_equal(sides: list[str]) -> bool:
    """Returns true if first element and second element of list are equal"""
    return sides[0] == sides[1]

def check_range(start: int, end: int) -> list[int] | None:
    """Returns a list of numbers in range that have equal sides
    E.g., start=11, end=22 -> [11, 22]
    Returns None if no numbers in range have equal sides
    """
    result = []
    for num in range(start, end + 1):
        num_split = split_number(num)
        if num_split == None:
            continue
        equal = check_sides_equal(num_split)
        if equal:
            result.append(num)
    
    return result if result != [] else None

def process_input(user_input: str) -> list[list[int]]:
    """Processes input to split commas, followed by splitting dashes to return ranges"""
    csv_entires = user_input.split(',')
    ranges = []
    for entry in csv_entires:
        split_entry = entry.split('-')
        entries_as_int = [int(split_entry[0]), int(split_entry[1])]
        ranges.append(entries_as_int)
    return ranges

def total_sum(user_input: str) -> int:
    """Takes an input, processes it, checks the ranges
    and returns values with matching sides
    E.g., 123122-123125,11-22 -> 123156
    """
    separated_vals = process_input(user_input)
    nums = []
    for val in separated_vals:
        ranges = check_range(val[0], val[1])
        if ranges == None:
            continue
        nums.append(sum(ranges))
    return sum(nums)

if __name__ == '__main__':
    user_input = input("Input your ranges from input.txt (Copy/Paste recommended!): ")
    result = total_sum(user_input)
    print(f'The result is: {result}')