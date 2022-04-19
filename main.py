from datetime import datetime


def square(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('log', 'a', encoding='utf-8') as f:
            f.write(f'Дата и время вызова функции: {datetime.now().strftime("%d/%m/%y %H:%M")}\n')
            f.write(f'Имя функции: {old_function.__name__}\n')
            f.write(f'Позиционные аргументы: {args}, Именнованные аргументы: {kwargs}\n')
            f.write(f'Возвращаемое значение: {result}\n' + '*' * 50 + '\n')
        return result

    return new_function


def param_square(path):
    def square(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Дата и время вызова функции: {datetime.now().strftime("%d/%m/%y %H:%M")}\n')
                f.write(f'Имя функции: {old_function.__name__}\n')
                f.write(f'Позиционные аргументы: {args}, Именнованные аргументы: {kwargs}\n')
                f.write(f'Возвращаемое значение: {result}\n' + '*' * 50 + '\n')
            return result

        return new_function

    return square


# @square
# def func(a, b):
#     return a ** b


# @param_square(path='log2')
# def func(a, b):
#     return a ** b


