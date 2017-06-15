#!/usr/bin/python
# compare_matches.py

# -----------------------------------------------------------------------------
# This script will compare the contents of two files and output the matches
# -----------------------------------------------------------------------------

# nothing to import

# -----------------------------------------------------------------------------
# compare_matches
# -----------------------------------------------------------------------------
def compare_matches(input_file1, input_file2):
    file1 = open(input_file1, 'r')
    file2 = open(input_file2, 'r')

    set1 = set()
    set2 = set()

    for line in file1:
        set1.add(line.strip().lower())

    for line in file2:
        set2.add(line.strip().lower())

    in_both_files = set1.intersection(set2)
    return in_both_files

if __name__ == "__main__":
    #--------------------------------------------------------------------------
    # get arguments
    #--------------------------------------------------------------------------
    from sys import argv
    try:
        script, input_file1, input_file2 = argv
    except:
        print("Usage: Run this script with two files are arugments. The " +\
                "output will be the lines that match.")
        exit()

    in_both_files = compare_matches(input_file1, input_file2)
    for item in in_both_files:
        print(item)
