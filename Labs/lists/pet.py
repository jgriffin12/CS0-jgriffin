"""
Lists and Unittest Lab
Updated By: Janet Griffin
CSCI 110 Lab
Date: 03/14/2024

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
    1. Create a list to store the total scores of each contestant
    2. Repeat 5 times:
        i. Read the input line
        ii. Split the line into a list of numbers
        iii. Convert the list of strings into a list of ints
        iv. Sum the list of ints
        v. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""


from typing import List

def main() -> None:
    """Main function that solves the problem
    """
    # step 1. create a list to store the total scores of each contestant
    totalScores = []

    # FIXME1 - repeat step 2-4 5 times
    for _ in range (5):
        # FIXED2 - read the input line as a list of integers using get_data function
        individualScores = get_data()

        # FIXED3 - find the sum of scores using list_sum function
        sum_indiv = list_sum(individualScores)

        # FIXED4 - append the sum to the list of scores
        totalScores.append(sum_indiv)

    # FIXED5 - print the final output calling answer function
    result = answer(totalScores)
    print(result)   

def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Args:
        None
    Returns:
        List[int]: list of ints
    """
    # FIXED6: convert str_nums as list of ints and return it
    str_nums = input().split()  # list of string number
    return [int(number) for number in str_nums]

def list_sum(numbers: List[int]) -> int:
    """Finds and returns sum of the numbers in the list.
    Args:
        numbers: List[int]: # takes a list of numbers as a parameter

    Returns:
        int: sum of the numbers in the list
    """
    # FIXED7: find the sum of the numbers in the list and return it
    return sum(numbers)


def answer(scores: List[int]) -> str:
    """Find and return the answer as a string.
    Args:
        scores (List[int]): List of 5 contestants scores
    Returns:
        str: index of the max score + 1 and the max score as a string
    """
    max_score = max(scores)
    index = scores.index(max_score)
    # FIXED8: return the index+1 and the max number in the list as a string
    return f"{index + 1} {max_score}"

if __name__ == "__main__":
    main()