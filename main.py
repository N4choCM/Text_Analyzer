# Inputs
text = input("Please, enter your text: ").lower()
letters = [input("Please, enter your first letter: ").lower(), input("Please, enter your second letter: ").lower(),
           input("Please, enter your third letter: ").lower()]

# Shows the text and the letters given.
print("\nYOUR TEXT")
print(f"Your text is: \n{text}")

print("\nYOUR LETTERS")
print(f"Your first letter is '{letters[0]}', the second one is '{letters[1]}' and the last one '{letters[2]}'.")


# Gets the instances of each given letter in the text.
letter_1 = text.count(letters[0])
letter_2 = text.count(letters[1])
letter_3 = text.count(letters[2])

print("\nAMOUNT OF LETTERS")
print(f"Letter '{letters[0]}' appears {letter_1} times in the text.")
print(f"Letter '{letters[1]}' appears {letter_2} times in the text.")
print(f"Letter '{letters[2]}' appears {letter_3} times in the text.")

# Gets the total number of words in the text.
num_of_words = text.split()
print("\nAMOUNT OF WORDS")
print(f"Your text is composed of {len(num_of_words)} words.")

# Gets the total number of characters of the text.
num_of_chars = len(list(text))
print("\nTOTAL NUMBER OF CHARACTERS")
print(f"The total number of characters in the text is {num_of_chars}.")

# Gets the first and last characters of the text.
text_list = list(text)
print("\nFIRST AND LAST CHARACTERS")
print(f"The first character of your text is '{text_list[0]}' and the last one is '{text_list[-1]}'.")

# Gets the original text with the words reversed.
print("\nORIGINAL TEXT WITH WORDS REVERSED")
num_of_words.reverse()
reversed_text = ' '.join(num_of_words)
print(f"Your reversed text is:\n'{reversed_text}'.")

# Verifies if 'Python' appears in the text.
print("\n DOES THE TEXT CONTAIN THE WORD 'PYTHON'?")
is_Python = 'python' in text
dic = {True:"appears", False:"doesn't appear"}
print(f"The word 'Python' {dic[is_Python]} in your text.")
