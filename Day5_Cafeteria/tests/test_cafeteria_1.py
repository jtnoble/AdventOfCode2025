from src.cafeteria_1 import (
    IngRange,
    separate_ranges_and_ingredients,
    create_ingredient_ranges,
    ingredient_in_range,
    count_ingredients_in_range,
)

def test_ingrange_from_string_parses_correctly():
    r = IngRange.from_string("5-10")
    assert r.start == 5
    assert r.end == 10

def test_ingrange_handles_multi_digit_numbers():
    r = IngRange.from_string("100-250")
    assert r.start == 100
    assert r.end == 250

def test_separate_ranges_and_ingredients_simple():
    lines = [
        "1-5\n",
        "6-10\n",
        "\n",
        "3\n",
        "9\n"
    ]
    result = separate_ranges_and_ingredients(lines)

    assert result == [
        ["1-5", "6-10"],
        [3, 9]
    ]

def test_separate_ranges_and_ingredients_no_ingredients():
    lines = [
        "2-4\n",
        "5-7\n",
        "\n"
    ]
    result = separate_ranges_and_ingredients(lines)

    assert result == [
        ["2-4", "5-7"],
        []
    ]

def test_create_ingredient_ranges_creates_objects():
    ranges = ["1-3", "10-20"]
    objs = create_ingredient_ranges(ranges)

    assert len(objs) == 2
    assert objs[0].start == 1
    assert objs[0].end == 3

def test_ingredient_in_range_true():
    ranges = [IngRange(1, 5), IngRange(10, 20)]
    assert ingredient_in_range(ranges, 4) is True
    assert ingredient_in_range(ranges, 15) is True

def test_ingredient_in_range_false():
    ranges = [IngRange(1, 5), IngRange(10, 20)]
    assert ingredient_in_range(ranges, 8) is False
    assert ingredient_in_range(ranges, -1) is False

def test_count_ingredients_in_range_basic():
    ranges = [IngRange(1, 5), IngRange(10, 20)]
    ingredients = [1, 3, 11, 25]
    assert count_ingredients_in_range(ranges, ingredients) == 3

def test_count_ingredients_in_range_zero():
    ranges = [IngRange(100, 200)]
    ingredients = [1, 2, 3]
    assert count_ingredients_in_range(ranges, ingredients) == 0


def test_count_ingredients_in_range_duplicates():
    ranges = [IngRange(5, 10)]
    ingredients = [6, 6, 9]
    assert count_ingredients_in_range(ranges, ingredients) == 3
