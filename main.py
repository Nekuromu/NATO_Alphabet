import pandas

pa_dict = {row.letter : row.code for index, row in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

user_input = input("Enter a word: ").split()

result = [pa_dict[letter.upper()] for word in user_input for letter in word]

print(" ".join(result))
