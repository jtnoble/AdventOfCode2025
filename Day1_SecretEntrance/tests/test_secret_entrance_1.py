from src.secret_entrance_1 import Dial, turn_dial

import pytest

def test_create_dial() -> None:
    """Test that the dial has a lower bound of 0 and an upper bound of 99, and that it starts at 50"""
    dial = Dial()
    assert dial.lower_bound == 0
    assert dial.upper_bound == 99
    assert dial.current_num == 50

@pytest.fixture()
def dial() -> Dial:
    """Dial fixture to be used with all tests pertaining to dials"""
    return Dial()

def test_rotate_left(dial: Dial) -> None:
    """Rotate the dial left a few times, expecting dial to decrease by value"""
    dial.rotate_left(amount=10)
    assert dial.current_num == 40
    dial.rotate_left(amount=10)
    assert dial.current_num == 30
    dial.rotate_left(amount=10)
    assert dial.current_num == 20

def test_rotate_left_out_of_bounds(dial: Dial) -> None:
    """Rotate the dial under the lower bound, causing the dial to cross to the upper bound"""
    dial.rotate_left(amount=60)
    assert dial.current_num == 90

def test_rotate_left_out_of_bounds_multiple_bound_passes(dial: Dial) -> None:
    """Rotate the dial under the lower bound multiple times"""
    dial.rotate_left(amount=200)
    assert dial.current_num == 50
    dial.rotate_left(amount=803)
    assert dial.current_num == 47

def test_rotate_right(dial: Dial) -> None:
    """Rotate the dial right a few times, expecting dial to increase by value"""
    dial.rotate_right(amount=10)
    assert dial.current_num == 60
    dial.rotate_right(amount=10)
    assert dial.current_num == 70
    dial.rotate_right(amount=10)
    assert dial.current_num == 80

def test_rotate_right_out_of_bounds(dial: Dial) -> None:
    """Rotate the dial over the upper bound, causing the dial to cross to the lower bound"""
    dial.rotate_right(amount=60)
    assert dial.current_num == 10

def test_rotate_right_out_of_bounds_multiple_bound_passes(dial: Dial) -> None:
    """Rotate the dial over the upper bound multiple times"""
    dial.rotate_right(amount=200)
    assert dial.current_num == 50
    dial.rotate_right(amount=803)
    assert dial.current_num == 53

def test_turn_dial_output_values(dial: Dial) -> None:
    """Check for user input to turn the dial"""
    turn_dial(dial=dial, user_input="R30")
    assert dial.current_num == 80
    turn_dial(dial=dial, user_input="L40")
    assert dial.current_num == 40

def test_turn_dial_returns_true(dial: Dial) -> None:
    """Check that when turning the dial to 0, it returns true"""
    result = turn_dial(dial=dial, user_input="L50")
    assert result

def test_turn_dial_returns_false(dial: Dial) -> None:
    """Check that when turning the dial to 0, it returns false"""
    result = turn_dial(dial=dial, user_input="L51")
    assert not result
