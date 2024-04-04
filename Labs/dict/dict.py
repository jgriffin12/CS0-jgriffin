"""
    CS110 Lab
    Dictionary Lab

    Updated By: Janet Griffin

    CSCI 110
    Date: 04/02/2023

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    # FIXED3 – add codes for the rest of the states
    'Arizona': 'AZ',
    'Alabama': 'AL',
    'Arkansas': 'AR',
    'Alaska': 'AK', 
    'Colorado': 'CO'
    }

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee'
}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'
# FIXED4: Add rest of the states’ capital cities to capitalCity dictionary
capitalCity['AZ'] = 'Phoenix'
capitalCity['AL'] = 'Montegomery'
capitalCity['AR'] = 'Little Rock'
capitalCity['AK'] = 'Juneau'
capitalCity['CO'] = 'Denver'

def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            # FIXME5 - complete menu option 2
            code = input('Enter a US code: ')
            if code in capitalCity:
                print('The capital for {} is {}.'.format(code, capitalCity[code]))
            else:
                print("Sorry, the code, {} was not found".format(code))
        # FIXED6 - complete menu option 3
        elif option == '3':
            state_name = input('Enter a US state name: ')
            if state_name in states:
                print('The capital for {} is {}.'.format(state_name, capitalCity[states[state_name]]))
            else: 
                print('Sorry, the capitol was not found for the state {}.'.format(state_name))
        # FIXED7 - handle the case where user enters invalid menu option
        else:
            print('Sorry, {} is not available.'.format(option))

        input()


if __name__ == "__main__":
    main()