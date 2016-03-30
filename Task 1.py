# Mr M J Ashton
# A453 - Material 2 - GTIN8
# 26 January 2016

# TASK ONE

# Functions 
def calcCheckDigit(code):     
    # Separate each number in the code and convert to integer
    first = int(code[0])
    second = int(code[1])
    third = int(code[2])
    fourth = int(code[3])
    fifth = int(code[4])
    sixth = int(code[5])
    seventh = int(code[6])

    # Multiply odd number positions by 3
    newFirst = first * 3
    newThird = third * 3
    newFifth = fifth * 3
    newSeventh = seventh * 3

    # Add together
    total = newFirst + second + newThird + fourth + newFifth + sixth + newSeventh

    # Work out the neareast equal or higher multiple of 10
    # % returns the remainder after dividing...
    if total % 10 == 0:
        multipleOfTen = total
    else:
        extra = 10 - (total % 10)
        multipleOfTen = total + extra

    # Subtract the total from this multiple of 10 to get the check digit
    checkDigit = multipleOfTen - total
    return checkDigit

def validate(code):
    # Separate each number in the code and convert to integer
    first = int(code[0])
    second = int(code[1])
    third = int(code[2])
    fourth = int(code[3])
    fifth = int(code[4])
    sixth = int(code[5])
    seventh = int(code[6])
    eighth = int(code[7])
    # Multiply odd number positions by 3
    newFirst = first * 3
    newThird = third * 3
    newFifth = fifth * 3
    newSeventh = seventh * 3
    # Add together
    total = newFirst + second + newThird + fourth + newFifth + sixth + newSeventh + eighth
    #Check validity
    if total % 10 == 0:
        return True
    else:
        return False


def displayMenu():
    print("")
    print("**** MAIN MENU ****")
    print("")
    print("1. Calculate a GTIN-8 number from a 7 digit code")
    print("2. Check the validity of a GTIN-8 barcode")
    print("3. QUIT the program")
    print("")
    
# MAIN PROGRAM

# Menu to be displayed to the user:

choice = 0

while choice != 3:

    displayMenu()
    choice = int(input("Please enter 1,2 or 3 from the list above: "))

    if choice == 1:
        # Ask the user to input the 7 digit code
        code7 = input("Please enter the 7 digit product code: ")
        # Call the function to calculate the check digit and save as a variable
        checkDigit = calcCheckDigit(code7)
        #Output the checkdigit value
        print("Check Digit is", checkDigit)
        #Output the full GTIN-8 barcode number
        print("The full GTIN-8 number is {0}{1}".format(code7,checkDigit))

    elif choice == 2:
        # Ask the user to input the GTIN-8 code
        gtin8 = input("Please enter the GTIN-8 barcode number: ")
        valid = validate(gtin8)
        if valid == True:
            print("This is a valid GTIN-8 number")
        else:
            print("This is NOT a valid GTIN-8 number")

    elif choice ==3:
        exit

    else:
        print("Sorry you did not enter 1 or 2")

    
