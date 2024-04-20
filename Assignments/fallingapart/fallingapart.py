'''
Name: Janet Griffin
Date: 04/18/2024
Program: Kattis Problem - Falling Apart https://open.kattis.com/problems/fallingapart
Description: Couple Bob and Alice are separating. For the divorce settlement, they must split their shared integer. Both parties like to pick 
the largest integer and so on (Alice picks first).
'''

# Function sorts the integer list from highest to lowest value. Returns sorted pieces in descending order. 
def sort_pieces(pieces):
    ints = pieces[0]
    ints = [int(pieces) for pieces in ints]
    sorted_pieces = sorted(ints)
    sorted_pieces.sort(reverse= True)
    return sorted_pieces
        
# Function that determines which integers are Alice's and which ones are Bob's
def share(pieces):
    sortedList = sort_pieces(pieces)
    sumAlice = sortedList[::2]
    sumBob = sortedList[1::2]
    totalAlice = 0
    totalBob = 0
    for i in range(0, len(sumAlice)):
        totalAlice = totalAlice + int(sumAlice[i])
    for i in range(0, len(sumBob)):
        totalBob = totalBob + int(sumBob[i])
    print(totalAlice, totalBob)

def test_sort_pieces1():
    pieces = [['0', '2' , '5', '6']]
    ans = sort_pieces(pieces)
    assert ans == ([6, 5, 2, 0]), f"Test case 1 failed: expected result ([6, 5, 2, 0]), got {ans}."

def test_sort_pieces2():
    pieces = [['15', '2' , '-2', '6']]
    ans = sort_pieces(pieces)
    assert ans == ([15, 6, 2, -2]), f"Test case 1 failed: expected result ([15, 6, 2, -2]), got {ans}."

def test_sort_pieces3():
    pieces = [['0', '50' , '5', '1']]
    ans = sort_pieces(pieces)
    assert ans == ([50, 5, 1, 0]), f"Test case 1 failed: expected result ([50, 5, 1, 0]), got {ans}."

def main():
    test_sort_pieces1()
    test_sort_pieces2()
    test_sort_pieces3()
    pieces = []
    num_pieces = int(input())
    integers = input().split()
    pieces.append(integers)
    sort_pieces(pieces)
    share(pieces)


# Calling main function
main()