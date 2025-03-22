###NEW SHARED
import re


def read_dat_file_to_lists(filename: str, skip_first_line: bool = False) -> list:
    nice_lists = []

    with open(filename) as f:
        raw_data = f.readlines()

    if skip_first_line:
        raw_data = raw_data[1:]

    # Initialize lists for the two columns
    nice_lists = [[] for _ in range(2)]

    # Process each line
    for line in raw_data:
        # Use str.split() without arguments to handle multiple spaces/tabs
        units = line.strip().split()

        # Skip lines that do not have exactly 2 columns
        if len(units) != 2:
            print(f"Warning: Skipping line with unexpected number of values: {line.strip()}")
            continue

        # Corrected loop
        for index, value in enumerate(units):
            try:
                typed_value = float(value)
                nice_lists[index].append(typed_value)
            except ValueError:
                print(f"Warning: Could not convert value to float: {value}")

    return nice_lists


def filenameToLatex(filename: str, strip_suffix: bool = True) -> str:
    # Remove file path and only take the last part (filename)
    compound_name = filename.split('/')[-1]

    # Check if 'ECN_' or other prefixes are part of the filename and if we need to strip them
    if strip_suffix:
        # Strip ECN_ and anything before the formula part (up to last underscore before formula)
        parts = compound_name.split('_')
        for part in parts:
            # Look for the part that contains numbers, assuming it's the chemical formula
            if re.search(r'\d', part):
                compound_name = part
                break

    # Remove any suffix like '_average.dat'
    compound_name = compound_name.split('_')[0]

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
