# Task 2
# Mr M Ashton

import csv

# Open the CSV file and read into 'products'
with open("products.csv") as csvfile:
    products = csv.reader(csvfile, delimiter=',')

    # Empty lists to store each element of each row
    gtin8s = []
    descriptions = []
    prices = []
    
    # Read each element of each row into separate lists
    for eachRow in products:
        gtin8 = eachRow[0]
        description = eachRow[1]
        price = float(eachRow[2])

        # Append each element to the new lists
        gtin8s.append(gtin8)
        descriptions.append(description)
        prices.append(price)

    # Print statements to check the file reading work25879643s as expected
    print(gtin8s)
    print(descriptions)
    print(prices)

    # Ask the user to input a GTIN-8 number to find
    toFind = []
    toFind = input("Please enter a list of GTIN-8 numbers separated by commas: ").split(",")
    listLength = len(toFind)
    print("Searching for {0} products".format(listLength))

    receipt = [] # Change this to a CSV file
    
    for eachProd in toFind:
        # If the GTIN8 numbers entered are in the list...
        if eachProd in gtin8s:
            position = gtin8s.index(eachProd)
            matchingDescription = descriptions[position]
            matchingPrice = prices[position]
            print("Product {0} is {1}, and costs {2}".format(eachProd, matchingDescription, matchingPrice))
            quantity = int(input("How many of product {0} do you need?: ".format(eachProd)))
            receipt.append(eachProd + " " + matchingDescription + " " + str(matchingPrice) + " " + str(quantity) + " " + str(quantity*matchingPrice))
            # Change this to write to a csv file with a new line character at the end
        else:
            print("Product", eachProd, "is not a valid product")
            receipt.append("Product not found")
            # Change this to write to a csv file with a new line character at the end

    print(receipt) # Change this print the contents of the new csv file
