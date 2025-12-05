from src.cafeteria_2 import (
    IngRange,
    separate_ranges_and_ingredients,
    create_ingredient_ranges,
    count_valid_ingredents_in_ranges,
)

def test_ingrange_from_string_basic():
    r = IngRange.from_string("3-8")
    assert r.start == 3
    assert r.end == 8

def test_ingrange_from_string_multi_digit():
    r = IngRange.from_string("100-250")
    assert r.start == 100
    assert r.end == 250

def test_separate_ranges_and_ingredients_basic():
    lines = [
        "1-4\n",
        "7-10\n",
        "\n",
        "5\n",
        "8\n",
    ]

    ranges, ingredients = separate_ranges_and_ingredients(lines)

    assert ranges == ["1-4", "7-10"]
    assert ingredients == [5, 8]

def test_separate_ranges_and_ingredients_no_ingredients():
    lines = [
        "2-3\n",
        "9-11\n",
        "\n"
    ]

    ranges, ingredients = separate_ranges_and_ingredients(lines)

    assert ranges == ["2-3", "9-11"]
    assert ingredients == []

def test_separate_ranges_and_ingredients_no_ranges():
    lines = [
        "\n",
        "4\n",
        "7\n",
    ]

    ranges, ingredients = separate_ranges_and_ingredients(lines)

    assert ranges == []
    assert ingredients == [4, 7]

def test_create_ingredient_ranges_creates_objects():
    ranges = ["1-5", "10-15"]
    result = create_ingredient_ranges(ranges)

    assert len(result) == 2
    assert isinstance(result[0], IngRange)
    assert result[0].start == 1
    assert result[0].end == 5

def test_count_valid_ingredients_no_ranges():
    assert count_valid_ingredents_in_ranges([]) == 0


def test_count_valid_ingredients_single_range():
    ranges = [IngRange(1, 5)]
    assert count_valid_ingredents_in_ranges(ranges) == 5

def test_count_valid_ingredients_non_overlapping():
    ranges = [
        IngRange(1, 3),
        IngRange(10, 12),
        IngRange(20, 25)
    ]
    # (3 - 1 + 1) = 3
    # (12 - 10 + 1) = 3
    # (25 - 20 + 1) = 6
    assert count_valid_ingredents_in_ranges(ranges) == 12

def test_count_valid_ingredients_full_overlap():
    ranges = [
        IngRange(1, 10),
        IngRange(3, 5),
        IngRange(2, 8)
    ]
    # Full merged range is 1–10
    assert count_valid_ingredents_in_ranges(ranges) == 10

def test_count_valid_ingredients_partial_overlap():
    ranges = [
        IngRange(1, 5),
        IngRange(3, 10),
    ]
    # Merged into 1–10 → 10 values
    assert count_valid_ingredents_in_ranges(ranges) == 10

def test_count_valid_ingredients_touching_ranges():
    ranges = [
        IngRange(1, 5),
        IngRange(6, 10)
    ]
    # → (5 - 1 + 1) = 5  
    # → (10 - 6 + 1) = 5  
    assert count_valid_ingredents_in_ranges(ranges) == 10

def test_count_valid_ingredients_unsorted_input():
    ranges = [
        IngRange(20, 30),
        IngRange(1, 5),
        IngRange(3, 12),
        IngRange(40, 50),
    ]
    # Merges 1–12 (12 total) and 20–30 (11 total) and 40–50 (11 total)
    assert count_valid_ingredents_in_ranges(ranges) == 34

def test_count_valid_ingredients_multiple_overlaps_chain():
    ranges = [
        IngRange(1, 4),
        IngRange(3, 6),
        IngRange(6, 10),
        IngRange(9, 15),
    ]
    # All merge into 1–15
    assert count_valid_ingredents_in_ranges(ranges) == 15

def test_full_example():
    lines = [
        "1-3\n",
        "5-7\n",
        "6-10\n",
        "\n",
        "3\n",
        "6\n",
        "9\n"
    ]

    ranges_raw, ingredients = separate_ranges_and_ingredients(lines)
    ranges = create_ingredient_ranges(ranges_raw)

    # merged ranges are 1–3 and 5–10
    total = count_valid_ingredents_in_ranges(ranges)

    # (3 - 1 + 1) = 3
    # (10 - 5 + 1) = 6
    assert total == 9
