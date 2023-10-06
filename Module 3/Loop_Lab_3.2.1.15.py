# Prompt the user to enter a natural number and convert it to an integer.
c0 = int(input("Enter a natural number: "))

# Initialize a variable to count the steps.
steps = 0

# Start a while loop that continues until c0 becomes equal to 1.
while c0 != 1:
    # Check if c0 is even (divisible by 2).
    if c0 % 2 == 0:
        # If c0 is even, divide it by 2 using integer division.
        c0 = c0 // 2
    else:
        # If c0 is odd, apply the Collatz formula: c0 = 3 * c0 + 1.
        c0 = 3 * c0 + 1
    
    # Print the updated value of c0 in each step.
    print(c0)
    
    # Increment the steps counter.
    steps += 1

# When the loop exits (c0 becomes 1), print the total number of steps taken.
print("steps =", steps)
