# Upper half
for i in range(5):
    for j in range(4 - i):
        print("  ", end="")

    for k in range(1 + (i * 2)):
        print("*", end=" ")

    print()

# Lower half
for i in range(1, 5):
    for j in range(i):
        print("  ", end="")

    for k in range(9 - (i * 2)):
        print("*", end=" ")

    print()