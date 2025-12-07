from src.laboratories_1 import split_list_into_list_of_list, process_input

def test_split_list_into_list_of_list_basic():
    lines = ["ABC", "DEF"]
    result = split_list_into_list_of_list(lines)

    assert result == [["A", "B", "C"], ["D", "E", "F"]]

def test_process_input_S_creates_vertical_beam():
    lines = [
        list("S.."),
        list("..."),
    ]
    output = process_input(lines)["lines"]

    # The S at (0,0) should make (1,0) a vertical beam
    assert output[1][0] == "|"

def test_process_input_caret_creates_side_beams():
    lines = [
        list(".^."),
    ]
    output = process_input(lines)["lines"]

    assert output[0][0] == "|"  # left side becomes beam
    assert output[0][2] == "|"  # right side becomes beam

def test_process_input_vertical_continuation():
    lines = [
        list(".|."),
        list("..."),
    ]
    output = process_input(lines)["lines"]

    # (1,1) becomes "|" because above it is a beam
    assert output[1][1] == "|"

def test_process_input_split_count_increments():
    lines = [
        list(".|."),
        list(".^."),
    ]
    result = process_input(lines)

    assert result["split_count"] == 1

def test_process_input_example_scenario():
    lines = [
        list("S.^."),
        list("...."),
        list("..^."),
    ]

    result = process_input(lines)
    output = result["lines"]

    assert output[1][0] == "|"

    # ^ creates side beams
    assert output[0][1] == "|"   # left of first ^
    assert output[0][3] == "|"   # right of first ^

    # Vertical continuation of beam
    assert output[2][0] == "|"   # beam continuing from S

    # split_count returned as integer
    assert isinstance(result["split_count"], int)
