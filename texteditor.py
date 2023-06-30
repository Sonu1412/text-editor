import os

def create_file(filename):
    with open(filename, 'w') as file:
        print(f"Created file: {filename}")

def read_file(filename):
    with open(filename, 'r') as file:
        print(f"Contents of {filename}:")
        print(file.read())

def update_file(filename):
    with open(filename, 'a') as file:
        print(f"Enter text to append to {filename} (press Ctrl+D to save and exit):")
        while True:
            try:
                line = input()
                file.write(line + '\n')
            except EOFError:
                break
    print(f"Updated {filename}.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted file: {filename}")
    else:
        print(f"{filename} does not exist.")

def list_files():
    files = os.listdir()
    if files:
        print("Files in the current directory:")
        for file in files:
            print(file)
    else:
        print("No files found.")

def text_editor():
    while True:
        print("\n--- Text Editor ---")
        print("1. Create a new file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. List files")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the file name: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Enter the file name: ")
            read_file(filename)
        elif choice == '3':
            filename = input("Enter the file name: ")
            update_file(filename)
        elif choice == '4':
            filename = input("Enter the file name: ")
            delete_file(filename)
        elif choice == '5':
            list_files()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

text_editor()
