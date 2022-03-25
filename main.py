morse_code_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' '
}

reversed_morse_code_dict = {v: k for (k, v) in morse_code_dict.items()}

direction = input('Translation Menu. \n1) Enter "yes" to translate to Morse code.\n2) Enter "no" to translate from Morse '
                  'code.\n').lower()

translated_message = ''

if direction == 'yes':
    message = input('\nEnter message\n')
    for char in message:
        translated_message = translated_message + morse_code_dict[char.lower()] + ' '

elif direction == 'no':
    morse_message = input('\nEnter Morse code message(enter commas between morse letter combinations and spaces)\n')
    print(morse_message.split(','))
    for char in morse_message.split(','):
        translated_message = translated_message + reversed_morse_code_dict[char]

else:
    print('\nInvalid Input')

print(translated_message)

