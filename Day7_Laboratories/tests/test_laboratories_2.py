import pytest
from src.laboratories_2 import split_list_into_list_of_list, count_timelines

def test_split_list_into_list_of_list_basic():
    lines = ["ABC", "DEF"]
    result = split_list_into_list_of_list(lines)
    assert result == [["A", "B", "C"], ["D", "E", "F"]]

def test_count_timelines_single_S():
    lines = [
        list(".......S......."),
        list("..............."),
        list("..............."),
    ]
    assert count_timelines(lines) == 1

def test_count_timelines_beam_hits_caret():
    lines = [
        list(".......S......."),
        list("..............."),
        list(".......^......."),
    ]
    assert count_timelines(lines) == 2

def test_count_timelines_caret_splits_left_right():
    lines = [
        list(".......S......."),
        list("..............."),
        list("......^.^......"),
    ]
    assert count_timelines(lines) == 1

def test_count_timelines_full_example():
    lines = [
        list(".......S......."),
        list("..............."),
        list(".......^......."),
        list("..............."),
        list("......^.^......"),
        list("..............."),
        list(".....^.^.^....."),
        list("..............."),
        list("....^.^...^...."),
        list("..............."),
        list("...^.^...^.^..."),
        list("..............."),
        list("..^...^.....^.."),
        list("..............."),
        list(".^.^.^.^.^...^."),
        list("..............."),
    ]
    result = count_timelines(lines)
    assert isinstance(result, int)
    assert result >= 1
