from yandex_testing_lesson import strip_punctuation_ru


def test_palindrom():
    test_data = (
        ('', ''),
        ('почему эта фигня не рабо-тает', 'почему эта фигня не рабо-тает'),
        ('я попробовал — ВСЕ', 'я попробовал ВСЕ'),
        ('Но эта программа не меняется', 'Но эта программа не меняется'),
        ('зачтись плз     я тя прошу', 'зачтись плз я тя прошу'),
        ('яуже,утсал.пожалуйтса!дай?мне:уже - поспать', 'яуже утсал пожалуйтса дай мне уже поспать'),
    )
    for input_s, correct_output_s in test_data:
        if strip_punctuation_ru(input_s) != correct_output_s:
            print('NO')
            return False
    print('YES')
    return True


test_palindrom()