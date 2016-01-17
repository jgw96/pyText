import sys
import functions


def main():

    arguments = sys.argv
    try:
        if arguments[1] == "--read":
            functions.read_file(arguments[2])
        elif arguments[1] == "--write":
            functions.write_file(arguments[2])
        elif arguments[1] == "--append":
            functions.append_file(arguments[2])
        elif arguments[1] == "--help":
            print("To read a file use --read followed by a file name, to write a new file use --write followed by a file name, and to edit a file already exisiting use --append followed by the file name.")
    except:
        print("You must supply at'least one argument, for help use --help")
        


main()
