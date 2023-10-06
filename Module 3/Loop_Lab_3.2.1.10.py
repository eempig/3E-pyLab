# Prompt the user to enter a word and convert it to uppercase
user_word = input("Enter a word: ").upper()

# Create an empty string to store uneaten letters
word_without_vowels = ""

# Iterate through each character in the user's word
for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter in "AEIOU":
        # If it's a vowel, continue to the next iteration, skipping this vowel
        continue
    # If it's not a vowel, concatenate it to the word_without_vowels string
    word_without_vowels += letter

# Print the word without vowels
print("Word without vowels:", word_without_vowels)
