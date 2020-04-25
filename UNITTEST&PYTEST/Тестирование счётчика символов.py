import pytest

from yandex_testing_lesson import count_chars


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)
        
def test_empty():
    counts = count_chars('')
    assert counts == {}

def test_common():
    counts = count_chars('aabccc')
    assert counts == {'a': 2, 'b': 1, 'c': 3}