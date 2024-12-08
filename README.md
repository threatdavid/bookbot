# BookBot

For my first project at Boot.dev, I developed a command-line application in Python designed to perform static analysis on text files, including full-length novels such as Frankenstein.

## Features

- Reads a text file and counts the total number of words.
- Computes the frequency of each character (case-insensitive).
- Outputs a formatted report with word count and character frequency.

## Prerequisites

- Python 3.7 or higher
- A text file to analyze (default: `book/frankenstein.txt`)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/threatdavid/bookbot.git
   cd <repository-folder>
2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

## Usage
1. Place the text file to be analyzed in the `book/` directory (default: `book/frankenstein.txt`)
2. Run the script:

    ```bash
    python3 main.py
3. The report will be printed to the console.


## Example Output
For a sample file like `book/frankenstein.txt`, the output might look like this:
    
    
    --- Begin report of book/frankenstein.txt ---
    12345 words found in the document

    The 'e' character was found 1678 times
    The 't' character was found 1456 times
    ...
    --- End report ---

## File Structure

    .
    ├── book/
    │   └── frankenstein.txt  # Sample text file
    ├── main.py               # Main script
    └── README.md             # Documentation

## Notes
1. Ensure the file path in the `main.py` script points to the correct file.
2. Feel free to modify main.py to analyze different files or customize the output.
