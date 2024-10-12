INTERNATIONAL_MORSE_CODE = {
        '''
        1. Len of a dot is one unit
        2. A dash is three units
        3. The space between parts of the same letter is one unit.
        4. The space between letters is three units.
        5. The space between words is seven units.
        '''
        'A': '. ---',
        'B': '--- . . .',
        'C': '--- . --- .',
        'D': '--- . .',
        'E': '.',
        'F': '. . --- .',
        'G': '--- --- .',
        'H': '. . . .',
        'I': '. .',
        'J': '. --- --- ---',
        'K': '--- . ---',
        'L': '. --- . .',
        'M': '--- ---',
        'N': '--- .',
        'O': '--- --- ---',
        'P': '. --- --- .',
        'Q': '--- --- . ---',
        'R': '. --- .',
        'S': '. . .',
        'T': '---',
        'U': '. . ---',
        'V': '. . . ---',
        'W': '. --- ---',
        'X': '--- . . ---',
        'Y': '--- . --- ---',
        'Z': '--- --- . .',
        '1': '. --- --- --- ---',
        '2': '. . --- --- ---',
        '3': '. . . --- ---',
        '4': '. . . . ---',
        '5': '. . . . .',
        '6': '--- . . . .',
        '7': '--- --- . . .',
        '8': '--- --- --- . .',
        '9': '--- --- --- --- .',
        '0': '--- --- --- --- ---',
        ' ': '    '
    }


def main():
    def read_file(name):
        with open(name, 'r') as src:
            data = src.read().strip()
            return data

    def return_morse_letter(letter: str):
        return "   " + INTERNATIONAL_MORSE_CODE[letter]

    def process_data(data):
        result_string = ""
        for char in data:
            char = char.upper()
            if char in INTERNATIONAL_MORSE_CODE.keys():
                result_string += return_morse_letter(char)
            else:
                print(f'\nChar "{char}" not known! Skipping.')

        print(f"Your result code is:\n{result_string.strip()}")

    def initialisation():
        decision = input("Enter full name of .txt file with morse code or enter it in:\n")
        if decision[-4:] == ".txt":
            data = read_file(decision)
        else:
            data = decision

        process_data(data)

    initialisation()


if __name__ == '__main__':
    main()
