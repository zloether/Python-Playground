#!/usr/bin/env python
# luhn10.py

# -----------------------------------------------------------------------------
# luhn10
# derived from source, with modifications:
# http://code.activestate.com/recipes/172845-python-luhn-checksum-for-credit-card-validation/
# -----------------------------------------------------------------------------
def luhn10(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    card_number_digits = card_number.replace("-", "").replace(" ", "")

    sum = 0
    num_digits = len(card_number_digits)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number_digits[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )



if __name__ == "__main__":
   from sys import argv
   try:
       script, credit_card_number = argv
   except:
       print("Usage: This script takes a credit card number as an argument" +\
                "and returns if the number passes luhn10 validation.")
       exit()

   print(luhn10(credit_card_number))
