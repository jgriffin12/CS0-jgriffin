"""
File I/O Lab with Dictionary

Update By: Janet Griffin

CSCI 110
Date: 04/25/2024

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.

"""


def readText():
    """
    opens a file reads its contents and
    creates a histogram of words based on frequency using dictionary data structure
    """
    fileOk = False
    fin = None
    hist = {}
    # stores data in this form: hist = {'and': 10, 'python':15}
    # where 'and' appears 10 times and
    # python appears 15 times

    while not fileOk:
        fileName = input('Enter input text file => ')
        try:
            fin = open(fileName, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occured: ', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()
        if line:
            # FIXED3
            # update words; split line into list of words and store the list into words object
            words = line.split()
            for word in words:
                # FIXED4
                # if word exists as key in hist dict, increment the value by 1
                # else add word as new key with value 1 in hist dict
                hist[word] = hist.get(word,0) +1          
    return hist


def reverseHistogramList(histDict):
    """
    given someDict,  returns list of tuples in descending order based 
    frequency of each word in histDict
    """
    reverseList = []
    for key, val in histDict.items():
        # FIXED5
        # append tuple with values in (val, key) order into reverseList list
        reverseList.append((val, key))
    # FIXED6
    # Sort the list reverseList in reverse order
        reverseList.sort(reverse = True)
    return reverseList

def main():
    histogram = readText()
    # FIXED7 - Comment the following statement out when done
    # print(histogram)  # see the output to understand what's going on so far

    aList = reverseHistogramList(histogram)
    # FIXED8 – print top 10 words with highest frequencies stored in aList
    for i in range(10):
        print(aList[i][1], aList[i][0])

if __name__ == "__main__":
    main()