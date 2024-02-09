'''
Name: Janet Griffin
Date: 2/7/2024
Due Date: 02/09/2024
Assignment: Standard Input Output - Stdio
Description: This program will prompt the user to enter their name, store their name into a variable, and greet the user using their name. 
In addition, variables will be created to store 4 different pieces of ASCII art. This program will display seasons throughout the year. 
'''

# Prompts user to enter name 
name: str = input("Please enter your name: ")

# Greets user 
print("Nice to meet you,", name, end = '\n\n')

# Notify user about ASCII Art
print("Here is some ASCII Art representing the different seasons throughout the year. Enjoy!" '\n\n')

# Stores Spring Flower ASCII art into the variable called spring. 
spring = '''                                           Spring Flowers                    
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            |\|\|\|\|         _()()_         |\|\|\|\|       
                            |       |        (_)00(_)        |       |       
                            \_______/         ()()()         \_______/      
                                |               |                |          
                            __  |  __       __  |  __        __  |  __      
                           {\ \ | / /}     {\ \ | / /}      {\ \ | / /}     
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Displays Spring ASCII Art
print(spring ,'\n')
 
# Stores Summer ASCII art into variable called summer. 
summer = '''                                           Summer Waves                    
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                      ///            ////        ///        
                                   //// /          //// /      /// /       /
                                //////        //////        /////         //
                             ///////////     /////////     ////////      ///
                          //////////////  ////////////  ////////////  //////
                        ////////////////////////////////////////////////////                    
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Displays Summer ASCII art 
print(summer,'\n')

# Stores Fall ASCII art into variable called fall. 

fall = '''                                            Fall Pumpkin                    
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                 __                           
                                     ___________||||___________               
                                   /    /    _   |    _    \    \             
                                  /    /    /_\  |   /_\    \    \            
                                 |    |         /_\          |    |           
                                 |    |   ____  _|_  _____   |    |           
                                 |    |   \||||_|||_||||/    |    |           
                                  \    \    \||||||||||/    /    /           
                                   \_____\__ ____|_________/____/            
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Displays Fall Ascii art
print(fall, '\n\n')
 
# Stores Winter ASCII art into variable called winter. 
winter ="""                                            Winter Snowmen                           
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
                           ________           ________          ________         
                           \||||||/           \||||||/          \||||||/          
                           _\||||/_           _\||||/_          _\||||/_         
                           /  o o  \          /  o o  \         /  o o  \        
                          |  . < .  |        |  . < .  |       |  . < .  |       
                           \  '''  /          \  '''  /         \  '''  /        
                       \/  ::::::::: \/    \/ ::::::::: \/  \/  ::::::::: \/     
                         \/   :: ::\/       \/   :: ::\/      \/   :: ::\/       
                         |   ::: :::|       |    ::: :::|     |    ::: ::|       
                          \    o   /         \    o    /       \    o   /        
                          /    o    \        /    o    \       /    o    \       
                         |     o     |      |     o     |     |     o     |      
                          \    o    /        \    o    /       \    o    /       
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
"""

# Displays Winter ASCII Art 
print(winter)