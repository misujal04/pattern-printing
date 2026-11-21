# Upper half
for i in range(5):

    # Left side stars
    for j in range(i + 1):
        print("*", end=" ")

    # Middle spaces
    for j in range(8 - (i * 2)):
        print("  ", end="")

    # Right side stars
    for j in range(i + 1):
        print("*", end=" ")

    print()


# Lower half
for i in range(3, -1, -1):

    # Left side stars
    for j in range(i + 1):
        print("*", end=" ")

    # Middle spaces
    for j in range(8 - (i * 2)):
        print("  ", end="")

    # Right side stars
    for j in range(i + 1):
        print("*", end=" ")

    print()