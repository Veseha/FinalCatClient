import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate1():
    with pytest.raises(ValueError):
        is_under_queen_attack('c3', 'd4d')


def test_wrong_coordinate_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")