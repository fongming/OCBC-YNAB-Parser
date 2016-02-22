import csv
import sys

file1 = open(sys.argv[1], "rb") # opens the csv file to read
file2 = open(sys.argv[1][:-4]+"_YNAB.csv", "wt") # opens the csv file to write
reader = csv.reader(file1)
writer = csv.writer(file2)
csvList = list(reader)

def bankAccount (myList):

    myList = filter(None, myList[6:])   # remove header lines of account information from file
                                        # also removes empty rows
    for row in myList:
        del row[1]                      # remove "Value date" column
        row.insert(4, "")               # insert empty column at end for "Payee"

    for i in range(0,len(myList)):
        if myList[i][0] == '':          # copy description of transaction to previous row's "Payee" column
            myList[i-1][4] = myList[i][1]

    myList = [row for row in myList if row[0] != ""]    # remove rows with empty first cell

    writer.writerow(("Date", "Memo", "Outflow", "Inflow", "Payee"))
    writer.writerows(myList)
    
    return

def creditCard (myList):

    myList = filter(None, myList[7:])   # remove header lines of account information from file

    myList = [row for row in myList if row[0][0].isdigit()] # remove header lines of supp cards

    writer.writerow(("Date", "Payee", "Outflow", "Inflow"))
    writer.writerows(myList)
    
    return

if csvList[1][0] == "Available ":

    bankAccount (csvList)
    
elif csvList[1][0] == "Credit limit":

    creditCard (csvList)

else:

    print "File is not recognized."

file1.close()
file2.close()

