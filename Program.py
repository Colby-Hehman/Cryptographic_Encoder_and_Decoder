# This is a program that can solve multiple different types of cryptographic puzzles. This will be updated in the future

import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase


def dict_encode(input_value, dict, punctuation_between=' '):
    final_value = ''
    for letter in input_value:
        if letter in dict.keys():
            final_value += dict[letter] + punctuation_between
    return final_value.strip(punctuation_between)


def dict_decode(input_value, dict, separator='', characters_per=0):
    final_value = ''
    input_split = input_value
    list_of_separators = ['   ', '  ', '+', ';', ':', '|', '*', '^', ' \\ ', '\\',
                          ' / ', '/' ', ', ',', ' ', '.', '-', '_']
    complete = False
    for sep in list_of_separators:
        if complete:
            break
        elif sep in input_value:
            input_split = input_value.split(sep)
            complete = True
    if complete is False and characters_per != 0:
        input_split = []
        current_value = ''
        index = 0
        for letter in input_value:
            if index < characters_per:
                current_value += letter
            else:
                input_split.append(current_value)
                index = 0
                current_value = str(letter)
            index += 1
        input_split.append(current_value)
        complete = True
    if complete is False:
        input_split = [input_split]
    dict_keys = list(dict.keys())
    dict_values = list(dict.values())
    for letter in input_split:
        decoded_word = ''
        i = 0
        index = 0
        for value in dict_values:
            if letter == value:
                index = i
            i += 1
        decoded_word += dict_keys[index]
        final_value += decoded_word + separator
    return final_value


morse_letters = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ':': '---...', '@': '.--.-.', '!': '-.-.--', '$': '...-..-', '&': '.-...', '=': '-...-',
    '+': '.-.-.', ';': '-.-.-.', '\'': '.----.', '"': '.-..-.'
}


def en_morse(phrase, punctuation_between=' '):
    phrase_encoded = ''
    for letter in phrase:
        if letter.upper() in morse_letters.keys():
            phrase_encoded += morse_letters[letter.upper()] + punctuation_between
        elif letter == ' ':
            phrase_encoded += '/ '
    return phrase_encoded.strip()


def de_morse(phrase, separator=' '):
    phrase_decoded = ''
    letter_encoded_list = []
    morse_letters_keys = list(morse_letters.keys())
    morse_letters_values = list(morse_letters.values())
    if '/' in phrase:
        letter_encoded_list = phrase.split(' / ')
    elif '  ' in phrase:
        letter_encoded_list = phrase.split('  ')
    else:
        letter_encoded_list = phrase
    phrase_split_twice = letter_encoded_list
    if type(phrase_split_twice) != list:
        list_form = []
        list_form.append(phrase_split_twice)
        phrase_split_twice = list_form
    for word in phrase_split_twice:
        word = word.split(' ')
        decoded_word = ''
        for letter in word:
            i = 0
            index = 0
            for value in morse_letters_values:
                if letter == value:
                    index = i
                i += 1
            decoded_word += morse_letters_keys[index]
        phrase_decoded += decoded_word + separator
    return phrase_decoded.strip()


binary_letters = {
    ' ': '00100000', '!': '00100001', '"': '00100010', '#': '00100011', '$': '00100100', '%': '00100101',
    '&': '00100110', '\'': '00100111', '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011',
    ',': '00101100', '-': '00101101', '.': '00101110', '/': '00101111', '0': '00110000', '1': '00110001',
    '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111',
    '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011', '<': '00111100', '=': '00111101',
    '>': '00111110', '?': '00111111', '@': '01000000', 'A': '01000001', 'B': '01000010', 'C': '01000011',
    'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001',
    'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111',
    'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101',
    'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', '[': '01011011',
    '\\': '01011100', ']': '01011101', '^': '01011110', '_': '01011111', '`': '01100000', 'a': '01100001',
    'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111',
    'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101',
    'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011',
    't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001',
    'z': '01111010', '{': '01111011', '|': '01111100', '}': '01111101', '~': '01111110'
}


def en_binary(phrase, punctuation_between=' '):
    return dict_encode(phrase, binary_letters, punctuation_between)


def de_binary(phrase, punctuation_between=''):
    return dict_decode(phrase, binary_letters, punctuation_between, 8)


ascii_letters = {
    ' ': '032', '!': '033', '"': '034', '#': '035', '$': '036', '%': '037', '&': '038', '\'': '039', '(': '040',
    ')': '041', '*': '042', '+': '043', ',': '044', '-': '045', '.': '046', '/': '047', '0': '048', '1': '049',
    '2': '050',
    '3': '051', '4': '052', '5': '053', '6': '054', '7': '055', '8': '056', '9': '057', ':': '058', ';': '059',
    '<': '060',
    '=': '061', '>': '062', '?': '063', '@': '064', 'A': '065', 'B': '066', 'C': '067', 'D': '068', 'E': '069',
    'F': '070',
    'G': '071', 'H': '072', 'I': '073', 'J': '074', 'K': '075', 'L': '076', 'M': '077', 'N': '078', 'O': '079',
    'P': '080',
    'Q': '081', 'R': '082', 'S': '083', 'T': '084', 'U': '085', 'V': '086', 'W': '087', 'X': '088', 'Y': '089',
    'Z': '090',
    '[': '091', '\\': '092', ']': '093', '^': '094', '_': '095', '`': '096', 'a': '097', 'b': '098', 'c': '099',
    'd': '100',
    'e': '101', 'f': '102', 'g': '103', 'h': '104', 'i': '105', 'j': '106', 'k': '107', 'l': '108', 'm': '109',
    'n': '110',
    'o': '111', 'p': '112', 'q': '113', 'r': '114', 's': '115', 't': '116', 'u': '117', 'v': '118', 'w': '119',
    'x': '120',
    'y': '121', 'z': '122', '{': '123', '|': '124', '}': '125', '~': '126'
}


def en_ascii(phrase, punctuation_between=' '):
    return dict_encode(phrase, ascii_letters, punctuation_between)


def de_ascii(phrase, punctuation_between=''):
    return dict_decode(phrase, ascii_letters, punctuation_between, 3)


hex_letters = {
    ' ': '20', '!': '21', '"': '22', '#': '23', '$': '24', '%': '25', '&': '26', '\'': '27', '(': '28', ')': '29',
    '*': '2A',
    '+': '2B', ',': '2C', '-': '2D', '.': '2E', '/': '2F', '0': '30', '1': '31', '2': '32', '3': '33', '4': '34',
    '5': '35',
    '6': '36', '7': '37', '8': '38', '9': '39', ':': '3A', ';': '3B', '<': '3C', '=': '3D', '>': '3E', '?': '3F',
    '@': '40',
    'A': '41', 'B': '42', 'C': '43', 'D': '44', 'E': '45', 'F': '46', 'G': '47', 'H': '48', 'I': '49', 'J': '4A',
    'K': '4B',
    'L': '4C', 'M': '4D', 'N': '4E', 'O': '4F', 'P': '50', 'Q': '51', 'R': '52', 'S': '53', 'T': '54', 'U': '55',
    'V': '56',
    'W': '57', 'X': '58', 'Y': '59', 'Z': '5A', '[': '5B', '\\': '5C', ']': '5D', '^': '5E', '_': '5F', '`': '60',
    'a': '61',
    'b': '62', 'c': '63', 'd': '64', 'e': '65', 'f': '66', 'g': '67', 'h': '68', 'i': '69', 'j': '6A', 'k': '6B',
    'l': '6C',
    'm': '6D', 'n': '6E', 'o': '6F', 'p': '70', 'q': '71', 'r': '72', 's': '73', 't': '74', 'u': '75', 'v': '76',
    'w': '77',
    'x': '78', 'y': '79', 'z': '7A', '{': '7B', '|': '7C', '}': '7D', '~': '7E'
}


def en_hex(phrase, punctuation_between=' '):
    return dict_encode(phrase, hex_letters, punctuation_between)


def de_hex(phrase, punctuation_between='', characters_per=0):
    return dict_decode(phrase, hex_letters, punctuation_between, characters_per)


A1Z26_letters = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11',
    'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21',
    'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6',
    'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16',
    'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
}


def en_a1z26(phrase):
    indexes = ''
    phrase = phrase.strip()
    for letter in phrase:
        if letter.upper() in uppercase_letters:
            indexes += str(uppercase_letters.index(letter.upper())) + ' '
        elif letter == ' ' or letter == '/':
            indexes += '/ '
    return indexes.strip()


def de_a1z26(phrase):
    phrase_decoded = ''
    letter_encoded_list = []
    if '/' in phrase:
        letter_encoded_list = phrase.split(' / ')
    elif '  ' in phrase:
        letter_encoded_list = phrase.split('  ')
    else:
        letter_encoded_list = phrase
    phrase_split_twice = []
    for letter in letter_encoded_list:
        if ',' in letter:
            phrase_split_twice.append(letter.split(','))
        else:
            phrase_split_twice.append(letter.split(' '))
    for word in phrase_split_twice:
        decoded_word = ''
        for letter in word:
            try:
                decoded_word += uppercase_letters[int(letter)]
            except:
                pass
        phrase_decoded += decoded_word + ' '
    return phrase_decoded.strip()


def caesar(phrase, letters_forward):
    phrase_encoded = ''
    for letter in phrase:
        if letter not in lowercase_letters and letter not in uppercase_letters:
            phrase_encoded += letter
        elif letter in lowercase_letters:
            index_of_letter = lowercase_letters.index(letter)
            new_index_of_letter = index_of_letter + letters_forward
            if new_index_of_letter < 0:
                new_index_of_letter += 26
            elif new_index_of_letter > 25:
                new_index_of_letter -= 26
            phrase_encoded += lowercase_letters[new_index_of_letter]
        else:
            index_of_letter = uppercase_letters.index(letter)
            new_index_of_letter = index_of_letter + letters_forward
            if new_index_of_letter < 0:
                new_index_of_letter += 26
            elif new_index_of_letter > 25:
                new_index_of_letter -= 26
            phrase_encoded += uppercase_letters[new_index_of_letter]
    return phrase_encoded


def caesar_all_rots(phrase):
    final_value = ''
    for i in range(26):
        final_value += str(i) + '. ' + caesar_cipher(phrase, i) + '\n'
    return final_value


# def_custom_dict turns words from a document into their index number (starting at 1). For instance, if you passed the
# US Constitution as the document, 'we', 'the', 'people' would become '1', '2', '3' regardless of capitalization. This
# dict cannot process punctuation though, and separates words after each space.


class CustomDict:
    def __init__(self, document):
        self.document = document
        self.document = self.document.split('\n')
        self.document = ' '.join(self.document)
        self.document = self.document.split('\t')
        self.document = ' '.join(self.document)
        def index_four_digs(ind):
            while len(str(ind)) < 5:
                ind = str(0) + str(ind)
            return ind
        new_doc = {}
        current_word = ''
        index = 1
        for letter in self.document:
            if letter in uppercase_letters or letter in lowercase_letters or letter =="'":
                current_word += letter.lower()
            else:
                if current_word != '':
                    if current_word in new_doc.keys():
                        previous_indexes = new_doc[current_word]
                        previous_indexes.append(index_four_digs(index))
                        new_doc[current_word] = previous_indexes
                        current_word = ''
                        index += 1
                    else:
                        new_doc[current_word] = [index_four_digs(index)]
                        current_word = ''
                        index += 1
        new_doc[current_word] = [index_four_digs(index)]
        self.document = new_doc

    def __repr__(self):
        return str(self.document)

    def encode(self, phrase, punctuation_between=' '):
        final_value = ''
        phrase = phrase.split('\n')
        phrase = ' '.join(phrase)
        phrase = phrase.split('\t')
        phrase = ' '.join(phrase)
        phrase_split = ''
        for letter in phrase:
            if letter in uppercase_letters or letter in lowercase_letters or letter == "'":
                phrase_split += letter.lower()
            else:
                if phrase_split[-1] != ' ':
                    phrase_split += ' '
        phrase_split = phrase_split.split(' ')
        for letter in phrase_split:
            if letter in self.document.keys():
                final_value += self.document[letter][0] + punctuation_between
        return final_value.strip(punctuation_between)

    def decode(self, phrase, separator=' '):
        final_value = ''
        input_split = phrase
        list_of_separators = ['   ', '  ', '+', ';', ':', '|', '*', '^', ' \\ ', '\\',
                              ' / ', '/' ', ', ',', ' ', '.', '-', '_']
        complete = False
        for sep in list_of_separators:
            if complete:
                break
            elif sep in phrase:
                input_split = phrase.split(sep)
                complete = True
        if complete is False and characters_per != 0:
            input_split = []
            current_value = ''
            index = 0
            for letter in input_value:
                if index < characters_per:
                    current_value += letter
                else:
                    input_split.append(current_value)
                    index = 0
                    current_value = str(letter)
                index += 1
            input_split.append(current_value)
            complete = True
        if complete is False:
            input_split = [input_split]
        dict_keys = list(self.document.keys())
        dict_values = list(self.document.values())
        for letter in input_split:
            decoded_word = ''
            i = 0
            index = 0
            for value in dict_values:
                if letter in value:
                    index = i
                i += 1
            decoded_word += dict_keys[index]
            final_value += decoded_word + separator
        return final_value


