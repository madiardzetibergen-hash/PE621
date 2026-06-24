def print_line():
    print("-" * 40)

def input_number(message):
    while True:
        value = input(message)

        if value.isdigit():
            return int(value)
        print("Ошибка: нужно ввести число")