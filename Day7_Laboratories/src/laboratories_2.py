import os

def split_list_into_list_of_list(lines: list[str]) -> list[list[str]]:
    result = []
    for line in lines:
        result.append(list(line))
    return result

def count_timelines(lines: list[list[str]]) -> int:
    counter = []
    for _ in lines[0]:
        counter.append(0)
    
    for line in lines:
        for i, c in enumerate(line):
            if c == "S":
                counter[i] = 1
                continue

            if c == "^":
                counter[i-1] += counter[i]
                counter[i+1] += counter[i]
                counter[i] = 0

    return sum(counter)

if __name__ == '__main__':
    # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    lines = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            lines.append(line)
    
    further_split = split_list_into_list_of_list(lines)
    result = count_timelines(further_split)

    print(f"The result is {result} timelines")