def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line here.\n")
    except IOError as e:
        print("Error: Unable to create file:", e)


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("Error:", e)


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2.\n")
            file.write("123456789\n")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  # Displaying contents after appending
#created using chat GPT