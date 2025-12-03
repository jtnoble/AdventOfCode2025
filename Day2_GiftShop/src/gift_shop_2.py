import time

def split_number(num: int, split_amount: int) -> list[str] | None:
    """Split number into two separate strings down based on split_amount value
    E.g., 123123, 2 -> ["123", "123"] | 1234, 4 -> ["1", "2", "3", "4"]
    Returns None if odd, e.g., 1234, 3 -> None
    """
    num_str = str(num)
    if len(str(num)) % split_amount != 0:
        return None # Sides not equal
    split_at = round(len(num_str) / split_amount)
    split_str = []
    start_index = 0
    for end_index in range(len(num_str)):
        if (end_index + 1) % split_at == 0:
            split_str.append(num_str[start_index:end_index + 1])
            start_index = end_index + 1

    return split_str

def check_sides_all_repeat(sides: list[str]) -> bool:
    """Returns true if all numbers in the list are repeating"""
    return len(set(sides)) == 1

def check_range(start: int, end: int) -> list[int] | None:
    """Returns a list of numbers in range that have equal sides
    E.g., start=11, end=22 -> [11, 22]
    Returns None if no numbers in range have equal sides
    """
    result = set()
    for num in range(start, end + 1):
        for i in range(2, len(str(num)) + 1):
            num_split = split_number(num, i)
            if not num_split:
                continue
            equal = check_sides_all_repeat(num_split)
            if equal:
                result.add(num)
    return list(result) if result else None

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
    start_time = time.time() # Tracking runtime
    result = total_sum(user_input)
    end_time = time.time()
    print(f'The result is: {result}\nRuntime: {round(end_time - start_time, 2)} seconds')