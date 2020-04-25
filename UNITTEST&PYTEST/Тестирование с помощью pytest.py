import pytest

from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''
    
def test_single_char():
    assert reverse('a') == 'a'

def test_palindrome():
    assert reverse('aba') == 'aba'

def test_common():
    assert reverse('abc') == 'cba'

def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)

def test_wrong_type_iterable():
    with pytest.raises(TypeError):
        reverse(['a', 'b', 'c'])
