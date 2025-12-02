from src.gift_shop import (
    split_number,
    check_sides_equal,
    check_range,
    process_input,
    total_sum
)

import pytest

def test_split_number() -> None:
    """Check that numbers are split as strings directly down the middle"""
    s1 = 123123
    s2 = 51336513

    assert split_number(s1) == ["123", "123"]
    assert split_number(s2) == ["5133", "6513"]

def test_split_number_odd_sides() -> None:
    """Try to split number as string with odd sides, should return none"""
    s1 = 123

    assert split_number(s1) == None

def test_check_sides_equal() -> None:
    """Check if sides from split_number are equal"""
    s1 = ["123","123"]
    s2 = ["122","312"]

    assert check_sides_equal(s1) == True
    assert check_sides_equal(s2) == False

@pytest.mark.parametrize(
    ["start", "end", "test_result"],
    [
        (11, 22, [11, 22]),
        (123120, 123125, [123123]),
        (121, 122, None)
    ]
)
def test_check_range(start: int, end: int, test_result: list[str] | None) -> None:
    """Check a range of numbers with split_number/check_sides, 
    Return list of true check_sides_equal results
    """
    
    result = check_range(start, end)
    assert result == test_result

def test_process_input() -> None:
    """Check that CSV values and ranges are properly separated"""
    user_input = "123123-123127,122-129"
    result = process_input(user_input)

    assert result == [[123123, 123127], [122, 129]]

def test_total_sum() -> None:
    """Uses every other function to get total sum of matching ranges"""
    user_input = "123123-123127,122-129, 11-22"
    result = total_sum(user_input)
    
    assert result == 123156 # (123123 + 11 + 22)