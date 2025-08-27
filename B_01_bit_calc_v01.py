# Generates headings ( ----- Heading ---- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Bit calculator
- Enter File type (Integer, Image, Text)
- Calculator will tell you the number of bits, etc.
- Instructions for each valid file type below  

- Type in Integer Number for the calculated bits needed to represent it
- Type in Dimensions of Image for the calculated number of pixels and bits
- Type in chosen Text for the calculated number of characters and bits 
    ''')



# asks users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

         # check for 'i' or the exit code
        if response =="xxx" or response == "i":
            return response

        # check if it's a integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check  for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response is invalid
        else:
            print("Please enter a valid file type")

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

# calculates how many bits are needed to represent a integer
def integer_calc():
    # Ask the user to enter an integer
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and find number of bits needed
    raw_binary = bin(integer)

    # remove '0b from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    #set up answer and return it
    answer = f"{integer} in binary its {binary}. We need {num_bits} bits to represent it."

    return answer

def calc_text_bits():

    # Get text from user
    response = input("Enter some text: ")
    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters. "
              f"\nWe need {num_chars} x 8 bits to represent it which is {num_bits} bits"
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine goes here


  # Display instructions if requested
want_instructions = input("Press <enter> to read the instructions  "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i' ask whether they want image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)
