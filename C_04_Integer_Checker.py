def int_check(question, low):
    error = f"Please enter a number that is more or equal to {low}\n"
    while True:

        try:
            response = int(input(question))

            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine
for item in range(0, 2):
    integer = int_check ("Integer: ", 0)
print(integer)

print()

for item in range(0, 2):
    width = int_check ("Width: ", 1)
print(width)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)