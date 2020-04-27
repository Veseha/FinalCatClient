from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test_palindrom():
    test_data = (
        ('79991122333', False),
        ('91231122333', False),
        ('877711223333', False),
        ('8777112233', False),
        ('8(7771)122333', False),
        ('87771122333', True),
        ('+77771122333', True),
        ('8(777)1122333', True),
        ('8777 1-1223-33', True),
    )
    for input_s, correct_output_s in test_data:
        if is_correct_mobile_phone_number_ru(input_s) != correct_output_s:
            print('NO')
            return False
    print('YES')
    return True


test_palindrom()