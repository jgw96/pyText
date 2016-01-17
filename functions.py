import os


# read a files contents
def read_file(file_name):
    file_to_read = open(file_name, "r")
    contents = file_to_read.read()
    print(contents)
    file_to_read.close()


# open new file and write to it
def write_file(file_name):
    file_to_write = open(file_name, "w")
    text_to_write = input("Write here: ")
    save_option = input("Would you like to save this file?(yes or no) ")
    if save_option == "yes":
        file_to_write.write(text_to_write)
        file_to_write.close()
    elif save_option == "no":
        os.remove(file_name)


# append text to a file that already exists
def append_file(file_name):
    file_to_write = open(file_name, "a")

    # always write a new line first to avoid formatting issues
    file_to_write.write("\n")

    text_to_write = input("Write here: ")
    save_option = input("Would you like to save this file?(yes or no) ")
    if save_option == "yes":
        file_to_write.write(text_to_write)
        file_to_write.close()
    elif save_option == "no":
        os.remove(file_name)