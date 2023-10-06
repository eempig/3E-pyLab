blocks = int(input("Enter the number of blocks: "))

height = 0  # Initialize the height of the pyramid to 0
layer_blocks = 1  # Initialize the number of blocks in the current layer to 1

while blocks >= layer_blocks:
    height += 1  # Increment the height by 1 for each layer added
    blocks -= layer_blocks  # Deduct the blocks used for the current layer
    layer_blocks += 1  # Increase the number of blocks in the next layer

print("The height of the pyramid:", height)
