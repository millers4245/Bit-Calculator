# ask user for width and loop until they
# enter a number that is more than zero
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


# calculates how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter an integer
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and find number of bits needed
    raw_binary = bin(integer)

    # remove '0b from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    #set up answer and return it
    answer = f"{integer} in binary its {binary}. We need {num_bits} to represent it."

    return answer

# Main rountine goes here
integer_ans = integer_calc()
print(integer_ans)
