import csv # Imported CSV module to handle csv filetypes

# Loading a CSV file using csv
def load_dictionary(csv_file):
    dictionary = {} # Creates an empty key-value pairs list for the dictionary
    with open(csv_file, mode='r') as file: # Uses open function to open csv file in read mode
        reader = csv.reader(file) # Create a CSV reader object
        next(reader)    # Line in case headers of CSV file include column titles

        # Itterate over each row in CSV file
        for row in reader:
            alphanum, code = row # Extract dictionary pairs over entire file, character to corresponding code
            dictionary[alphanum] = code # Add the character and code to the dictionary

    # Add a unique placeholder for spaces if not already in the dictionary
    if ' ' not in dictionary:
        dictionary[' '] = 'SPACE'

    return dictionary # Return the populated dictionary


# Encoding a message
def encode_message(message, dictionary):
    encoded_message = [] # List to hold encoded characters
    for char in message: # Iterate over each character
        if char in dictionary:  # Check if the character is in the dictionary
            encoded_message.append(dictionary[char])  # Append the encoded value to the list
        else:
            encoded_message.append(char) # If no corresponding value in dictionary, keep character as is
    return ' '.join(encoded_message)  # Join the list into a string with spaces between encoded characters


# Decoding a messsage
def decode_message(encoded_message, dictionary):
    reversed_dict = {v: k for k, v in dictionary.items()}  # Create a reversed dictionary for decoding (nescesary to be able to use reversed_dic[code])
    decoded_message = []
    for code in encoded_message.split(): # Split the encoded message by spaces and iterate over each code
        if code in reversed_dict:  # Check if the code is in the reversed dictionary
            decoded_message.append(reversed_dict[code])  # Append the decoded character to the list
        else:
            decoded_message.append(code) # Leave as is if cannot translate
    return ''.join(decoded_message) # Join list into a string with spaces between decoded chars


# User Interaction
def main():
    csv_file = input("Enter csv file name: ")
    try:
        code_dict = load_dictionary(csv_file)  # Load the dictionary from the user-specified CSV file
    except FileNotFoundError:
        print("Error: The specified file was not found, make sure it is in the same directory.")
        return
    while True: # Loop to continuously prompt the user until they choose to exit
        # Input cleaned (removed spaces in front and turned all characters lowercase to avoid errors)
        choice = input("Type 'encode' to encode a message or 'decode' to decode a message (or 'exit' to quit): ").strip().lower()
        if choice == 'encode': # User chose to code a string
            message = input("Enter the message to encode: ")
            encoded_message = encode_message(message, code_dict) # Runs encode_message def
            print(f"Encoded message: {encoded_message}")
        elif choice == 'decode': # User chose to decode string
            message = input("Enter the message to decode (use space between codes): ")
            decoded_message = decode_message(message, code_dict) # Runs decode_message def
            print(f"Decoded message: {decoded_message}")
        elif choice == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.") # In case user input is not 'encode', 'decode' or 'exit'

    
if __name__ == "__main__":
    main()  # Run the main function if this script is executed

