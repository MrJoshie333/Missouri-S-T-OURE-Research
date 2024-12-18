###NEW SHARED, after chat gpt update
import re


def read_dat_file_to_lists(filename: str, type_of_split, skip_first_line: bool = False) -> list:
    nice_lists = []

    with open(filename) as f:
        raw_data = f.readlines()

    if skip_first_line:
        raw_data = raw_data[1:]

    # Determine the split character
    split = " " if type_of_split == " " else "\t"

    # Initialize lists based on the first line
    first_line = raw_data[0].strip().split(split)
    values_per_row = len(first_line)
    nice_lists = [[] for _ in range(values_per_row)]

    # Process each line
    for line in raw_data:
        units = line.strip().split(split)

        # Skip lines that do not have the correct number of columns
        if len(units) != values_per_row:
            print(f"Warning: Skipping line with unexpected number of values: {line.strip()}")
            continue

        # Corrected loop
        for index, value in enumerate(units):
            typed_value = value.replace("\n", "")
            try:
                typed_value = float(typed_value)
            except ValueError:
                pass
            nice_lists[index].append(typed_value)

    return nice_lists


def filenameToLatex(filename: str) -> str:
    # Split the filename by "/" and take the first part
    compound_name = filename.split('/')[0]

    # Use regex to find numbers and add LaTeX subscript formatting
    latex_compound = re.sub(r'(\d+)', r'$_{\1}$', compound_name)

    return latex_compound


def extract_density(input_string: str) -> float:
    # Use regex to find the part starting with 'd' and extract the numbers after it
    match = re.search(r'd(\d+)p(\d+)', input_string)
    if match:
        # Extract the two groups of digits (before and after 'p')
        whole_part = match.group(1)  # digits before 'p'
        decimal_part = match.group(2)  # digits after 'p'

        # Combine them to form a float number
        density = float(f"{whole_part}.{decimal_part}")
        return density
    else:
        print(f"Warning: '{input_string}' does not contain a valid density pattern.")
        return None  # Return None if the pattern is not found
