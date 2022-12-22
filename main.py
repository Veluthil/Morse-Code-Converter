from art import logo, goodbye

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
              '-': '-....-', '(': '-.--.', ')': '-.--.-', "'": '.____.', ' ': ''
              }


def turn_into_morse_code(string):
    for char in string:
        if char not in morse_code:
            return "Invalid character, try again."
        for key in morse_code:
            if char == key:
                converted_string.append(morse_code[key])


def turn_into_string(string):
    string_list = string.split(' ')
    for symbols in string_list:
        if symbols not in morse_code.values():
            return "Invalid character, try again."
        for value in morse_code.values():
            key_list = list(morse_code.keys())
            val_list = list(morse_code.values())
            if symbols == value:
                position = val_list.index(value)
                converted_string.append(key_list[position])


# ------------ INTRODUCTION AND RULES --------------
print(f"{logo}"
      "\nWelcome to the Morse Code Converter!"
      "\n"
      "\nFirst choose a mode: "
      "\n- type 'M' if you want to convert Morse Code to text,"
      "\n- type 'T' if you want to convert text to Morse Code."
      "\nRules and additional options:"
      "\n- '  ' (double space) indicates spaces between words in Morse Code -"
      " when converting Morse Code to a string use double space as a break between single words."
      "\n- To exit Morse Code Converter type '#'"
      "\n")


# -------------- FUNCTIONALITY -----------------------
converter_on = True
converted_string = []
while converter_on:
    mode = input("Choose a mode by typing 'M' or 'T': ").upper()
    if mode == "T":
        string_to_convert = input("Please write here your text you would like to convert to Morse Code: ").upper()
        turn_into_morse_code(string_to_convert)
        if len(converted_string) != 0:
            print(f"Your text ({string_to_convert}) in Morse Code is: {' '.join(converted_string)}")
        elif string_to_convert[0] == "#":
            converter_on = False
            print(goodbye)
        else:
            print("Invalid character, try again.")
    elif mode == "M":
        mc_to_convert = input("Please write here Morse Code you would like to convert to text: ")
        turn_into_string(mc_to_convert)
        if len(converted_string) != 0:
            print(f"Your Morse Code ({mc_to_convert}) converted to text is: {''.join(converted_string)}")
        elif mc_to_convert[0] == "#":
            converter_on = False
            print(goodbye)
        else:
            print("Invalid character, try again.")
    elif mode == "#":
        converter_on = False
        print(goodbye)
    converted_string.clear()
