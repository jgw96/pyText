import sys
import functions


def main():

    arguments = sys.argv
    arg_one = str(arguments[1])
    file_name = str(arguments[2])

    if arg_one == "--read":
        functions.read_file(file_name)
    elif arg_one == "--write":
        functions.write_file(file_name)
    elif arg_one == "--append":
        functions.append_file(file_name)
    elif arg_one == "--help":
        print("To read a file use --read followed by a file name, to write a new file use --write followed by a file name, and to edit a file already exisiting use --append followed by the file name.")

main()
