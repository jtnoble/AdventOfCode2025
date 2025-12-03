from src.gift_shop_2 import (
    split_number,
    check_sides_all_repeat,
    check_range,
    process_input,
    total_sum
)

import pytest

def test_split_number() -> None:
    """Check that numbers are split as strings based on a split amount"""
    s1 = 123123
    s2 = 51336513
    s3 = 123

    assert split_number(s1, 2) == ["123", "123"]
    assert split_number(s2, 2) == ["5133", "6513"]
    assert split_number(s3, 3) == ["1", "2", "3"]

def test_split_number_uneven_sides() -> None:
    """Try to split number as string with uneven sides, should return none"""
    s1 = 123
    s2 = 1234
    s3 = 12341234

    assert split_number(s1, 2) == None
    assert split_number(s2, 3) == None
    assert split_number(s3, 3) == None

def test_check_sides_all_repeat() -> None:
    """Check if sides from split_number are equal"""
    s1 = ["123","123"]
    s2 = ["122","312"]
    s3 = ["123", "122", "123"]
    print(set(s1))
    print(set(s2))

    assert check_sides_all_repeat(s1) == True
    assert check_sides_all_repeat(s2) == False
    assert check_sides_all_repeat(s3) == False

@pytest.mark.parametrize(
    ["start", "end", "test_result"],
    [
        (11, 22, [11, 22]),
        (123120, 123125, [123123]),
        (121, 122, None),
        (565653, 565659, [565656])
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
    t1 = "11-22, 123120-123126"
    t2 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    assert total_sum(t1) == 123156 # (123123 + 11 + 22)
    assert total_sum(t2) == 4174379265 # Yeah, I'm not making a good comment for this one.
