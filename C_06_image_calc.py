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
def image_calc():
    # get the image dimemsions
    width = int_check ("Width: ", 1)
    height = int_check("Height: ", 1)

# calculate the number of pixels and bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels:  {width} x {height} = {num_pixels} "
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

# Main routine goes here
image_ans = image_calc()
print(image_ans)
