# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the user's word to uppercase
user_word = user_word.upper()

# Iterate through each character in the word
for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter in "AEIOU":
        # If it's a vowel, continue to the next iteration, skipping this vowel
        continue
    # If it's not a vowel, print the letter
    print(letter)
