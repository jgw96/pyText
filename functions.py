import os
import paramiko
import base64


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
        print("New file written: " + file_name)
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
        print(file_name + " successfully edited and saved.")
    elif save_option == "no":
        os.remove(file_name)


def connect_to_server():
    rsa_key = input("Where is your RSAKey: ")
    key = paramiko.RSAKey(data=base64.decodestring(rsa_key))
    client = paramiko.SSHClient()

    server = input("What is the url or ip of the server you are tyring to connect to: ")
    client.get_host_keys().add(server, 'ssh-rsa', key)
    username = input("Username please: ")
    password = input("Password please: ")
    
    client.connect(server, username=username, password=password)
    sftp_client = client.open_sftp()
    file_name = input("Path to the file you are trying to read: ")
    remote_file = sftp_client.open(file_name)

    return remote_file


def read_remote_file():
    remote_file = connect_to_server()
    read_file(remote_file)