from yandex_testing_lesson import is_prime


def test_palindrom():
    test_data = (
        (-3, None),
        (-1, None),
        (0, None),
        (1, None),
        (2, True),
        ('1', None),
        (21, False),
        (6, False),
        (5, True),
        (13, True),
    )
    for input_s, correct_output_s in test_data:
        try:
            # Вычисляем результат на входных данных
            # Есть вариант, что наша функция выбросит исключение,
            # поэтому делаем это в блоке try
            output_s = is_prime(input_s)
        except TypeError:
            if type(input_s) == int:
                print('NO')
                return False
        except ValueError:
            if input_s > 1:
                print('NO')
                return False
        except Exception:
            print('NO')
            return False
        else:
            if output_s != correct_output_s:
                print('NO')
                return False
    print('YES')
    return True


test_palindrom()