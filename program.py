def check_password(s, n):
    has_digit = False
    has_capital = False
    if n < 4:
        return 0
    if s[0].isdigit():
        return 0
    for ch in s:
        if ch == ' ' or ch == '/':
            return 0
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_capital = True
    if has_digit and has_capital:
        return 1
    else:
        return 0