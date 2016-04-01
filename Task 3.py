# Task 3
# Stock Levels
# Mr M Ashton

import csv

### Open the CSV file and read into 'products'
##  with open("stock.csv") as csvfile:
##    stock = csv.reader(csvfile, delimiter=',')
##
##    # Empty lists to store each element of each row
##    gtin8s = []
##    descriptions = []
##    currentLevels = []
##    reOrderLevels = []
##    targetLevels = []
##    
##    # Read each element of each row into separate lists
##    for eachRow in stock:
##        gtin8 = eachRow[0]
##        description = eachRow[1]
##        currentLevel = eachRow[2]
##        reOrderLevel = eachRow[3]
##        targetLevel = eachRow[4]
##
##        # Append each element to the new lists
##        gtin8s.append(gtin8)
##        descriptions.append(description)
##        currentLevels.append(currentLevel)
##        reOrderLevels.append(reOrderLevel)
##        targetLevels.append(targetLevel)


def printAllStock():
    with open("stock.csv") as csvfile:
        stockLevels = csv.reader(csvfile, delimiter=',')
        for eachRow in stockLevels:
            print(eachRow[0],eachRow[1],eachRow[2],eachRow[3],eachRow[4],sep='\t')

def printCurrentStock():
    with open("stock.csv") as csvfile:
        stockLevels = csv.reader(csvfile, delimiter=',')
        for eachRow in stockLevels:
            print(eachRow[0],eachRow[1],eachRow[2],sep='\t')

def printReOrderLevels():
    with open("stock.csv") as csvfile:
        stockLevels = csv.reader(csvfile, delimiter=',')
        for eachRow in stockLevels:
            print(eachRow[0],eachRow[1],eachRow[3],sep='\t')

def printTargetLevels():
    with open("stock.csv") as csvfile:
        stockLevels = csv.reader(csvfile, delimiter=',')
        for eachRow in stockLevels:
            print(eachRow[0],eachRow[1],eachRow[4],sep='\t')

def calcBelow():
    with open("stock.csv") as csvfile:
        stockLevels = csv.reader(csvfile, delimiter=',')
        for eachRow in stockLevels:
            if eachRow[2] < eachRow[3]:
                print("Order new stock for {0}".format(eachRow[0]))
