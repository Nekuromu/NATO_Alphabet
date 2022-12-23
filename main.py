import pandas

try:
    pa_dict = {row.letter: row.code for index, row in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
except FileNotFoundError:
    print("Error: Could not find the file 'nato_phonetic_alphabet.csv'.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()


def generate_phonetic():
    user_input = input("Enter a word: ").split()

    try:
        result = (" ".join([pa_dict[letter.upper()] for word in user_input for letter in word]))
    except KeyError:
        print(f"Error: numbers & symbols are not recognized letters in the NATO phonetic alphabet.")
        result = None
        generate_phonetic()

    print(result)
    generate_phonetic()


generate_phonetic()
