from random import choice
from string import punctuation

# List of adjective that can be used in password
adjective = ["attractive","bald","beautiful","chubby","clean","dazzling","drab","elegant","fancy","fit","flabby","glamorous","gorgeous","handsome","long","magnificent","muscular","plain","plump","quaint","scruffy","shapely","short","skin","stocky","ugly","unkempt","unsightly"]

# List of noun that can be used in  password
noun = ["people","history","way","art","world","information","map","two","family","government","health","system","computer","meat","year","thanks","music","person","reading","method","data","food","understanding"] 

# Range of number that can be used in the password 
number = range(0,2001)

# For symbols we can import the string module for python inbuild library 
print("Welcome to Password Generator..... You will get 1000's of uncrackable password and easy to remembe...\n")


# We set while as true and if we want to get out of the loop break the loop using break statement.
while True:

    # Use for loop to loop for 10 times 
    for i in range(0,10):

        # If we create continuously 10 passwords that wont be look good, so we ask user to give input as 
        # enter to give one by one
        user = input("\nPress enter to get more passowrd: \n")

        # Use random module to pick a choice for each time, to present the different password
        adjective_new = choice(adjective)
        noun_new = choice(noun)

        # number is a integer we can't add with string so make it as string using str function
        number_new = str(choice(number))

        # For symbols we use string module to generate punctuation and use random choice to choose one 
        symbols = choice(punctuation)

        # And then print them in a single line 
        print(adjective_new + noun_new + number_new + symbols)

    # After finishing 10 times we ask if he\she want to stop if he want's to stop then press n o no
    again_user = input("\nDo you still want to see more password (if no please type  'n' or 'no'): \n")
    
    # If he\she press no or n it break out of the loop and the program finish.
    if again_user == "no"or again_user == "n":
        break


