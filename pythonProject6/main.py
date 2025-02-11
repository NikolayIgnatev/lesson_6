def has_digit(password):
    return any([symbol.isdigit() for symbol in password])


def is_very_long(password):
    return len(password) >= 12


def has_upper_letters(password):
    return any([symbol.isupper() for symbol in password])


def has_lower_letters(password):
    return any([symbol.islower() for symbol in password])


def has_symbols(password):
    return any([not symbol.isdigit() and not symbol.isalpha()
                for symbol in password])


def main():
    password = input('введите пароль')
    score = 0
    functions = [
        has_digit(password),
        is_very_long(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]
    for function in functions:
        if function:
            score += 2
    print('Оценка пароля:', score)


if __name__ == '__main__':
    main()
