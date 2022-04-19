from main import square, param_square

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


@param_square(path='log2')
def get_name(num):
    for doc in documents:
        if doc["number"] == num:
            return doc["name"]


@square
def get_shelf(num):
    for shelf in directories.items():
        if num in shelf[1]:
            return shelf[0]


@square
def get_list(doc):
    for person in doc:
        print(f'{person["type"]} "{person["number"]}" "{person["name"]}"')


@square
def add_doc(type, num, name, shelf):
    documents.append({"type": type, "number": num, "name": name})
    if shelf in directories.keys():
        directories[shelf].append(num)
    else:
        print('Указанной полки не существует')
        repeat_shelf = input(f'Введите номер полки из списка {list(directories.keys())}: \n')
        directories[repeat_shelf].append(num)


@square
def check_num(num):
    for shelf in directories.values():
        if num in shelf:
            return True
    print('Указанного номера не существует')
    print()


@square
def delete(num):
    for doc in documents.copy():
        if doc["number"] == num:
            documents.pop(documents.copy().index(doc))
    for shelf in directories.copy().items():
        if num in shelf[1]:
            shelf[1].remove(num)
            # directories.pop(f'{shelf[0]}')


@square
def move(num, sh):
    if sh in directories.keys():
        for shelf in directories.values():
            if num in shelf:
                shelf.remove(num)
        directories[sh].append(num)
    else:
        print('Указанной полки не существует')
        for shelf in directories.values():
            if num in shelf:
                shelf.remove(num)
        directories[input(f'Введите номер полки из списка {list(directories.keys())}: ')].append(num)


@square
def add_shelf(new_shelf):
    if new_shelf not in directories.keys():
        directories[new_shelf] = []
    else:
        print('Данная поллка уже существует')


@square
def main():
    while True:
        cmd = input('Введите команду: ')
        if cmd in comand.keys():
            if cmd == 'a':
                try:
                    docs = input('Введите тип документа, номер, имя и полку через запятую: ').split(', ')
                    comand[cmd](docs[0], docs[1], docs[2], docs[3])
                except IndexError:
                    print('Неверный формат ввода')
                print()
            elif cmd == 'p':
                number = input('Введите номер документа: ')
                if check_num(number):
                    print(comand[cmd](number))
                    print()
            elif cmd == 's':
                number = input('Введите номер документа: ')
                if check_num(number):
                    print(comand[cmd](number))
                    print()
            elif cmd == 'd':
                number = input('Введите номер документа: ')
                if check_num(number):
                    comand[cmd](number)
                    print()
            elif cmd == 'm':
                try:
                    num_sh = input('Введите номер документа и целевую полку через запятую: ').split(', ')
                    if check_num(num_sh[0]):
                        comand[cmd](num_sh[0], num_sh[1])
                except IndexError:
                    print('Неверный формат ввода')
                print()
            elif cmd == 'as':
                comand[cmd](input('Введите номер новой полки: '))
                print()
            else:
                comand[cmd](documents)
                print()
        elif cmd.lower() == 'exit':
            print('Выход из программы!')
            break
        else:
            print('Такой команды не существует. Существующие команды - p, s, l, a, d, m, as!')
            print()


if __name__ == '__main__':
    comand = {
        'p': get_name,
        's': get_shelf,
        'l': get_list,
        'a': add_doc,
        'd': delete,
        'm': move,
        'as': add_shelf
    }
    main()
