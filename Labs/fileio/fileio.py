"""
File I/O Lab
By: Janet Griffin   

CSCI 110
Date: 04/09/2024

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

totalInts = 10


def readData():
    intList = []
    # FIXED1 (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    fileName = input("Please enter file name: ")
    try:
        with open(fileName, 'r+') as f:
            for line in f:
                intList.append(int(line.strip()))
    # If file is not found...
    except FileNotFoundError:
        print("File not found.")
    return intList
       
def sortListInAscendingOrder(lstInts):
    # FIXED2
    # sort lstInts list in ascending order
    lstInts.sort()


def sortListInDescendingOrder(lstInts):
    # FIXED3
    # sort lstInts in descending order
    lstInts.sort(reverse = True)
    return lstInts


def printList(printFile, lstInts):
    for i in lstInts:
        # FIXED4
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(str(i) + "\n")
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXED5
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXED6
    # Write the sorted list in descending order to the output file 
    printFile.write("Numbers in Descending Order: \n")
    printList(printFile, integers)

    # FIXED7
    # Print the largest number to the output file
    printFile.write("Largest Number in File: {}\n".format(max(integers)))

    # FIXED8
    # Print the smallest number to the output file
    printFile.write("Smallest Number in File: {}\n".format(min(integers)))

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXED9
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()