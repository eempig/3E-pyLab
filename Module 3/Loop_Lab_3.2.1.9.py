# Initialize a variable to store the user's input
user_input = ""

# Start an infinite loop
while True:
    # Ask the user to enter a word and store it in the user_input variable
    user_input = input("Enter a word: ")

    # Check if the user_input is equal to "chupacabra"
    if user_input == "chupacabra":
        # If it is, print the exit message and break out of the loop
        print("You've successfully left the loop.")
        break

