from yandex_testing_lesson import is_palindrome


def test_palindrom():
    test_data = (
        ('abc', False),
        ('ab', False),
        ('', True),
        ('aba', True),
        ('a', True),
    )
    for input_s, correct_output_s in test_data:
        if is_palindrome(input_s) != correct_output_s:
            print('NO')
            return False
    print('YES')
    return True


test_palindrom()