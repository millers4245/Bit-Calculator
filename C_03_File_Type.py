# asks users for file type (integer / image / text / xxx)
def get_filetype():
    response = input("File type: ").lower()

     # check for 'i' or the exit code
    if response =="xxx" or response == "i":
        return response

    # check if it's a integer
    elif response in ['integer', 'int']:
        return "integer"


# Main routine goes here
file_type = get_filetype()
