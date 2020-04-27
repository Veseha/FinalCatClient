def func(s):
    a = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    strr = ""
    for char in s:
        if char in a:
            strr += ' '
        else:
            strr += char
    return strr


def strip_punctuation_ru(s):
    words = s.split()
    words = filter(lambda x: x not in '—-', words)
    words = map(func, words)
    return " ".join(words)