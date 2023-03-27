"""Write a program to read names from keyboard and store into text file"""
# Open the file for writing
with open("26program.txt", "w") as f:
    # Prompt the user for names
    while True:
        name = input("Enter a name (or press Enter to finish): ")
        # Exit the loop if the user presses Enter without entering a name
        if name == "":
            break
        # Write the name to the file
        f.write(name + "\n")
