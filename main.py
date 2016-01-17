import sys
import functions


def main():
    arguments = sys.argv

    if arguments[1] == "--read":
        functions.read_file(arguments[2])
    elif arguments[1] == "--write":
        functions.write_file(arguments[2])
    elif arguments[1] == "--append":
        functions.append_file(arguments[2])
    elif arguments[1] == "--read-remote":
        functions.read_remote_file()
    elif arguments[1] == "--help":
        print(
        "To read a file use --read followed by a file name, to read a file on a remote server use --read-remote, to write a new file use --write followed by a file name, and to edit a file already exisiting use --append followed by the file name.")


main()
