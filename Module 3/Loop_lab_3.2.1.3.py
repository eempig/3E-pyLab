secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
+================================+
""")

# Use a while loop to repeatedly ask the user for input
while True:
    # Get the user's guess as an integer
    user_guess = int(input("So, what is the secret number? "))

    # Check if the user's guess matches the secret number
    if user_guess == secret_number:
        # Print a congratulatory message and break out of the loop
        print("Well done, muggle! You are free now.")
        break
    else:
        # If the guess is incorrect, inform the user and continue the loop
        print("Ha ha! You're stuck in my loop!")
