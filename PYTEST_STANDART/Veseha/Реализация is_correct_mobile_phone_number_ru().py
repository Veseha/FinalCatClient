def is_correct_mobile_phone_ru(n):
    if n[:1] == '8':
        a = n[1:]
    elif n[:2] == '+7':
        a = n[2:]
    else:
        print('NO')
        return False
    a = a.replace(' ', '')
    a = a.replace('-', '')
    if a[0] == '(' and a[4] == ')':
        a = a[1:4] + a[5:]
    if len(a) != 10:
        print('NO')
        return False
    if a.isdigit():
        print('YES')
        return True
    print('NO')
    return False


is_correct_mobile_phone_ru(input())