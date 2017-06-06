#!/usr/bin/env python
# template.py

# -----------------------------------------------------------------------------
# template
# -----------------------------------------------------------------------------
def template(input_data):
    output = input_data
    return output



if __name__ == "__main__":
   from sys import argv
   try:
       script, input_data = argv
   except:
       print("Usage: This script is a sample that takes an argument" +\
                "and returns it.")
       exit()

   data = template(input_data)
   print(data)
