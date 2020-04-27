def is_prime(a):
    if type(a) != int:
        raise TypeError()
    elif a <= 1:
        raise ValueError()
    for divisor in range(2, int(a ** 0.5) + 1):
        if a % divisor == 0:
            return False
    return True


def test_palindrom():
    try:
        a = int(input())
        b = is_prime(a)
    except Exception:
        print('NO')
        return False
    if b:
        print('YES')
        return True
    else:
        print('NO')
        return False


test_palindrom()