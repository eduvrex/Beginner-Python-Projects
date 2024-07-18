# Importing functions to facilitate program
import csv # Opens CSV files and reads/writes, also wraps code with "" when a comma was generated into a code.
import random # Capable of generating random codes
import string # Access string constants from ascii

def generate_random_code(length, complexity, existing_codes): # Creates a single instance of mapping (future code itterates over this)
    """
    Generate a random alphanumeric code of a given length and complexity.

    Parameters:
    length (int): The length of the random code.
    complexity (int): The complexity level of the random code (1: letters, 2: letters and numbers, 3: letters, numbers, and symbols).
    existing_codes (set): A set of already generated codes to avoid duplicates.
    
    Returns:
    str: The generated random code.
    """
    if complexity == 1:
        characters = string.ascii_letters  # Only letters (uppercase and lowercase)
    elif complexity == 2:
        characters = string.ascii_letters + string.digits  # Letters and digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and symbols
    else:
        raise ValueError("Complexity must be 1, 2, or 3")  # Handle invalid complexity values

    while True:
        # Generate a random string of the specified length
        code = ''.join(random.choice(characters) for _ in range(length))
        # Generates a random string by choosing 'length' number of characters from the 'characters' set.
        # The 'random.choice(characters)' function selects a random character from the 'characters' set.
        # The for loop runs 'length' times, and each time it adds a random character to the list.
        # The ''.join() function combines these characters into a single string.
        if code not in existing_codes:
            existing_codes.add(code)  # Add the new code to the set of existing codes
            return code  # Return the unique code


def build_dictionary(length, complexity):
    """
    Build a dictionary mapping each alphanumeric character to a random code.

    Parameters:
    length (int): The length of the random codes.
    complexity (int): The complexity level of the random codes.

    Returns:
    dict: The generated dictionary mapping characters to random codes.
    """

    characters = string.ascii_letters + string.digits + string.punctuation + ' ' # Alphanumeric characters and punctuation and "space"
    dictionary = {}  # Initialize an empty dictionary
    existing_codes = set()  # Initialize a set to keep track of existing codes

    for char in characters:
        dictionary[char] = generate_random_code(length, complexity, existing_codes)  # Generate code with specified length and complexity
    
    return dictionary  # Return the populated dictionary


def save_dictionary_csv(dictionary, filename):
    """
    Save the dictionary to a CSV file.

    Parameters:
    dictionary (dict): The dictionary to save.
    filename (str): The name of the CSV file.

    Returns:
    None
    """
    # Open the CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerow(['Character', 'Code'])  # Write the header row
        
        # Iterate over the dictionary items
        for char, code in dictionary.items():
            writer.writerow([char, code])  # Write each character-code pair to the CSV file

def main():
    """
    Main function to interact with the user and create the dictionary.
    """
    length = int(input("Enter the length of the random codes: "))  # Prompt user for length
    complexity = int(input("Enter the complexity (1: letters, 2: letters and numbers, 3: letters, numbers, and symbols): "))  # Prompt user for complexity
    filename = input("Enter the name of the CSV file to save the dictionary (e.g., 'custom_dictionary.csv'): ")  # Prompt user for filename
    
    dictionary = build_dictionary(length, complexity)  # Build the dictionary with specified length and complexity
    save_dictionary_csv(dictionary, filename)  # Save the dictionary to the specified CSV file
    
    print(f"Dictionary saved to {filename}")  # Inform user that the dictionary has been saved


if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly