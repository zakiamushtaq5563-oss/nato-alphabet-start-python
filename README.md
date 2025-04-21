# NATO Phonetic Alphabet Converter

A simple Python application that converts text input to NATO phonetic alphabet code words.

## Description

This project reads the NATO phonetic alphabet from a CSV file and provides a way to convert any word or text into its NATO phonetic alphabet representation.

For example, "Hello" becomes "Hotel Echo Lima Lima Oscar".

## Features

- Reads NATO alphabet codes from CSV file
- Converts user input to corresponding NATO phonetic code words
- Handles uppercase and lowercase letters

## Requirements

- Python 3.8+
- pandas 1.0.5+

## Installation

This project uses Poetry for dependency management.

```bash
# Install dependencies
poetry install
```

## Usage

Run the program with:

```bash
python main.py
```

Then enter any word when prompted, and the program will output the NATO phonetic code words.

## Data Source

The NATO phonetic alphabet codes are loaded from the included `nato_phonetic_alphabet.csv` file.
