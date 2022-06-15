def reverse_string(string: str) -> str:
    reversed_chars_list = []

    for char in string:
        reversed_chars_list.insert(0, char)

    return ''.join(reversed_chars_list)


def main():
    input_string = str(input('Digite algo:\t'))
    reversed_string = reverse_string(input_string)
    print(f'Inversão:\t{reversed_string}')


main()
