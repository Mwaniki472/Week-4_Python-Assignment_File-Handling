# File Read & Write Challenge with Error Handling

def main():
    # Step 1: Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify content (example: make everything uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
# File Read & Write Challenge with Error Handling

