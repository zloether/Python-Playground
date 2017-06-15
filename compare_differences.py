#!/usr/bin/python
# compare_differences.py

# -----------------------------------------------------------------------------
# This script will compare the contents of two files and output the differences
# -----------------------------------------------------------------------------

# nothing to import

# -----------------------------------------------------------------------------
# compare_differences
# -----------------------------------------------------------------------------
def compare_differences(input_file1, input_file2):
    file1 = open(input_file1, 'r')
    file2 = open(input_file2, 'r')

    set1 = set()
    set2 = set()

    for line in file1:
        set1.add(line.strip().lower())

    for line in file2:
        set2.add(line.strip().lower())

    unique_to_file1 = set1.difference(set2)
    return unique_to_file1

if __name__ == "__main__":
    #--------------------------------------------------------------------------
    # get arguments
    #--------------------------------------------------------------------------
    from sys import argv
    try:
        script, input_file1, input_file2 = argv
    except:
        print("Usage: Run this script with two files are arugments. The " +\
                "output will be the differences.")
        exit()

    unique_to_file1 = compare_differences(input_file1, input_file2)
    for item in unique_to_file1:
        print(item)
