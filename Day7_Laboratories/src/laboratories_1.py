import os

# Split lines into lists
# if character is S: check next line. If next line at index is . then make it |
# if character is ^, check previous and next characters. if . then make it |
# if character is ., check if previous line is | then make current character |
# Count | characters

def split_list_into_list_of_list(lines: list[str]) -> list[list[str]]:
    result = []
    for line in lines:
        result.append(list(line))
    return result

def process_input(lines: list[list[str]]) -> dict:
    split_count = 0
    for i in range(len(lines)):
        for x, c in enumerate(lines[i]):

            if c == "S" and i + 1 < len(lines) and lines[i+1][x] == ".":
                lines[i+1][x] = "|"

            elif c == "^":
                if x - 1 >= 0 and lines[i][x-1] == ".":
                    lines[i][x-1] = "|"
                if x + 1 < len(lines[i]) and lines[i][x+1] == ".":
                    lines[i][x+1] = "|"
                if i > 0 and lines[i-1][x] == "|":
                    split_count += 1 # Counts if the ^ receives a beam to them split

            elif c == "." and i > 0 and lines[i-1][x] == "|":
                lines[i][x] = "|"
    result = {"split_count": split_count, "lines": lines}
    return result

if __name__ == '__main__':
    # Quick file read for inputting file into the turn_dial function
    filepath = f'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    lines = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            lines.append(line)
    
    further_split = split_list_into_list_of_list(lines)

    output = process_input(further_split)
    split_count = output.get("split_count")

    # output the lines because it looks cool finished.
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/output.txt', 'w') as f:
        for line in output.get("lines"):
            for c in line:
                f.write(c)
            f.write("\n")

    print(f"The result is {split_count} splits")
