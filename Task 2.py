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

    # Print statements to check the file reading work as expected
    print(gtin8s)
    print(descriptions)
    print(prices)

    # Ask the user to input a GTIN-8 number to find
    toFind = []
    toFind = input("Please enter a list of GTIN-8 numbers separated by commas: ").split(",")
    print("Searching for {0} products".format(len(toFind)))

    receipt = [] # Write this to a CSV file later...
    receiptTotal = 0.00
    
    for eachProd in toFind:

        # If the GTIN8 numbers entered are in the list...
        if eachProd in gtin8s:
            position = gtin8s.index(eachProd)
            matchingDescription = descriptions[position]
            matchingPrice = prices[position]

            # Confirm to user and ask about quanity of each product
            print("Product {0} is {1}, and costs {2}".format(eachProd, matchingDescription, matchingPrice))
            quantity = int(input("H1479ow many of product {0} do you need?: ".format(eachProd)))

            # Calculate the subtotal for each product
            subtotal = quantity*matchingPrice

            # Keep a running total of the whole order
            receiptTotal += subtotal

            # Write each element back to a receiptLine list
            receiptLine = [eachProd,matchingDescription,matchingPrice,quantity,subtotal]
            
            # Append each receiptLine to the receipt 
            receipt.append(receiptLine)

        else:
            print("Product", eachProd, "is not a valid product")
            receiptLine = [eachProd,"Product not found",0.00,0,0.00]
            receipt.append(receiptLine)

    # Append the total cost of the order to the receipt
    totalLine = ["","TOTAL COST OF ORDER","","",receiptTotal]
    receipt.append(totalLine)

    # Write the contents of the receipt list(of lists) to a file
    with open("receipt.csv",mode="w",newline='') as receiptFile:
        writer = csv.writer(receiptFile)
        writer.writerows(receipt)

    
