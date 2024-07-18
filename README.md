# Beginner-Python-Projects

A repository for all of my beginner projects as I learn Python.

## Files:

### CoderAndDecoder.py
**Alphanumeric Encoder and Decoder**

This Python script provides functionalities to encode and decode messages using customizable encoding dictionaries. The user can load a dictionary from a CSV file, encode messages into custom codes, and decode encoded messages back to their original form while preserving spaces.

#### Features:
- **Load Dictionary**: Load an encoding dictionary from a CSV file.
- **Encode Messages**: Convert alphanumeric messages into encoded messages using the loaded dictionary.
- **Decode Messages**: Convert encoded messages back to their original alphanumeric form using the loaded dictionary.
- **Space Preservation**: Ensures that spaces in the original message are encoded and decoded accurately.

#### Usage:
1. Run the script.
2. Load a dictionary from a CSV file.
3. Choose to encode or decode a message.
4. Enter the message to encode or decode.

### DictionaryMaker.py
**Encoding Dictionary Builder**

This Python script allows users to generate CSV files containing encoding dictionaries with user-defined code lengths and complexities. The user can specify the length and complexity of the random codes, and the script will create a dictionary mapping alphanumeric characters to randomized codes.

#### Features:
- **Customizable Complexity**: Users can choose from three levels of complexity for the generated codes:
  - Level 1: Letters only
  - Level 2: Letters and numbers
  - Level 3: Letters, numbers, and symbols
- **Avoid Duplicates**: Ensures that generated codes are unique.
- **CSV Output**: Saves the generated dictionary as a CSV file for use in encoding and decoding messages.

#### Usage:
1. Run the script.
2. Specify the length and complexity of the random codes.
3. Save the generated dictionary as a CSV file.

## Example

1. Generate a dictionary and save it as `custom_dictionary.csv` using `DictionaryMaker.py`.
2. Encode a message using `custom_dictionary.csv` with `CoderAndDecoder.py`.
3. Decode the encoded message back to its original form with `CoderAndDecoder.py`.

## Installation

Ensure you have Python installed. Clone this repository and run the provided scripts.

## Running the Scripts

### To generate a dictionary:

```bash
python DictionaryMaker.py
