from art import logo

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
              '-': '-....-', '(': '-.--.', ')': '-.--.-', "'": '.____.', ' ': '|'
              }


def turn_into_morse_code(string):
    for char in string:
        if char not in morse_code:
            return "Invalid character, try again."
        for key in morse_code:
            if char == key:
                converted_string.append(morse_code[key])


print(f"{logo}"
      f"\nWelcome to the Morse Code Converter!"
      "\n- '|' indicates spaces between words"
      "\n- To exit Morse Code Converter type '#'")

converter_on = True
converted_string = []
while converter_on:
    string_to_convert = input("Please write here a text you would like to convert to Morse Code: ").upper()
    turn_into_morse_code(string_to_convert)
    if len(converted_string) != 0:
        print(f"Your string ('{string_to_convert}') in morse code is: {' '.join(converted_string)}")
    elif string_to_convert[0] == "#":
        converter_on = False
        print("Goodbye!")
    else:
        print("Invalid character, try again.")
    converted_string.clear()
