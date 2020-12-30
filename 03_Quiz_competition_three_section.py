points = 0

def multiple_check(guess, answer):
    attempt = 0
    global points
    think = True
    while think and attempt < 2:
        if guess == answer:
            points = points + 1
            print("Correct")
            think = False
        else:
            if attempt <= 1:
                guess = input("Your answer is wrong try again >>> ")
                attempt += 1
               
    if attempt == 2:
    	print("The correct answer is", answer, "\n")

def multiple_history_section():
    guess = str(input("In which year, Alexander the Great become the king of Macedonia ?\nA. 336 BC\nB. 323 BC\nC. 350 BC\nD. 200 BC\n").lower())
    multiple_check(guess, "a")
    guess1 = input("Who was the Emperor of Russia during Russia Revolution ?\nA. Alexander III\nB. Nicholas II\nC.Nicholas I\nD. Alexander II\n").lower()
    multiple_check(guess1, 'b')
    guess2 = input("When did the second Russian revolution start ?\nA. Auguest, 1950\nB. February, 1917\nC. October, 1917\nD. March, 1921\n").lower()
    multiple_check(guess2, "c")
    guess3 = input("Who is known as the founder of Tudor dynasty in England ?\nA. Elizabeth I\nB. Richard III\nC. Henry VII\nD. None of the above\n").lower()
    multiple_check(guess3, "c")
    guess4 = input("Leonardo da Vinci was born in the city of ?\nA.Rome\nB. Milan\nC. Florence\nD.Madrid\n").lower()
    multiple_check(guess4, "c")
    guess5 = input("In which year did the Suez Canal was open for trade ?\nA. 1869\nB. 1880\nC. 1774\nD. 1620\n")
    multiple_check(guess5, "a")
    guess6 = input("Who was the first Roman Emperor ?\nA. Caligula\nB. Claudius\nC. Augustus\nD. Nero\n").lower()
    multiple_check(guess6, "c")
    guess7 = input("Whichs one was the capital city of Byzantine Empire ?A.Venice\n  B. Rome\nC. Vienna\nD. Constantinople\n").lower()
    multiple_check(guess7, "d")
    guess8 = input("Who was the founder of the Ottaman Empire ?\nA. Osman I\nB. Orhan\nC. Mura I\nD. Bayezid I\n").lower()
    multiple_check(guess8, "a")
    guess9 = input("Crimean War was started in the year ?\nA. 1853\nB. 1857\nC. 1862\nD. 1870").lower()
    multiple_check(guess9, "a")
    print(f"Your total points in Multiple Choice History Section is {points} points")

def check(guess, answer):
    attempt = 0
    global points
    think = True
    while think and attempt < 3:
        if guess == answer:
            print("Correct \n")
            points += 1
            think = False
        else:
            if attempt <= 2:
               guess = input("Sorry your answer is like shit: ").lower()
               attempt = attempt + 1
    if attempt == 3:
       print("The right answer is ", answer , '\n')




def geographical_question():
    guess1 = input("Which is the smallest country in the world ? >>> ").lower()
    check(guess1, "vatican city")
    guess2 = input("Which is the hottest continent in the world ? >>> ").lower()
    check(guess2, 'africa')
    guess3 = input("Which is the largest country in the world ? >>> ").lower()
    check(guess3, "russia")
    guess4 = input("What colour is spotted in the middle of Japanese Flag ? >>> ").lower()
    check(guess4, "red")
    guess5 = input("What is the deepest lake in the world ? (Answer format: Lake(name) in (Country)) >>> ").lower()
    check(guess5, "lake baikel in russia")
    guess6 = input("Mount Everest is located in the border between in which two country ? (Answer format: Country One & Country Two ) >>> ").lower()
    check(guess6, "nebal & tibet")
    guess7 = input("In which coutry would you be if you visiting the 'Taj Mahal' ? >>> ").lower()
    check(guess7, "india")
    guess8 = input("Is Australia in the northern or the southern hemisphere ? >>> ").lower()
    check(guess8, "southern")
    guess9 = input("What is the  worlds largest continent ? >>> ").lower()
    check(guess9, "asia")
    guess10 = input("Which country has the most valcano's ? >>> ").lower()
    check(guess10, "indonesia")
    print(f"Your total points in Geograpical Section is {points} points")

def history_question():
    guess1 = input("In which year America got independence ? >>> ").lower()
    check(guess1, "1776")
    guess2 = input("Who is known as the Artist of the famous painting of 'Mona Lisa' ? >>> ").lower()
    check(guess2, "lenardo dav vinci")
    guess3 = input("'Boston Tea Party' protest was associated with revoultion of ? >>> ").lower()
    check(guess3, "america")
    guess4 = input("Nepolean was exiled to the Saint Helena after the defeat in the war of ").lower()
    check(guess4, "waterloo")
    guess5 = input("Industrial Revolution was started in which county ? >>> ").lower()
    check(guess5, "england")
    guess6 = input("Which city was recaptured at the end of the first war of Crusade ? >>> ").lower()
    check(guess6, "jerusalem")
    guess7 = input("Which year Christopher Columbus discover America ? >>> ").lower()
    check(guess7,"1492")
    guess8 = input("Who was the Chinese Emperor when Macro Polo visited china ? >>> ").lower()
    check(guess8, "kublai khan")
    guess9 = input("Who is the founder of Yuvan Dynasty in China ? >>> ").lower()
    check(guess9, "kublai khan")
    guess10 = input("which year William Shakespear was born ? >>> ").lower()
    check(guess10, "1564")
    print(f"Your total points in the History Section is {points} points")

def programming_fundamental():
    guess1 = input("Which language computers can understand ? >>> ").lower()
    check(guess1, "machine language")
    guess2 = input("What is IDE stands for ? >>> ").lower()
    check(guess2, "integrated development environment")
    guess3 = input("Who designed Python ? >>> ").lower()
    check(guess3, "guido van rossum")
    guess4 = input("Who designed JavaScript ? >>> ").lower()
    check(guess4, "brendan eich")
    guess5 = input("Who designed Java ? >>> ").lower()
    check(guess5, "james gosling")
    guess6 = input("Who designed C ? >>> ").lower()
    check(guess6, "dennis ritchie")
    guess7 = input("Who designed C++ ? >>> ").lower()
    check(guess7, "bjarne stroustrup")
    guess8 = input("Who designed Swift ? (Most of them know Apple invented but who designed ? >>> ").lower()
    check(guess8, "chris lattner")
    guess9 = input("Which company designed C# ? >>> ").lower()
    check(guess9,"microsoft corporation")
    guess10 = input("Who designed php ? >>> ").lower()
    check(guess10, "rasmus lerdof")
    print(f"Your total points in the Programming Fundamental Section is {points} points")

def multiple_choice_selector():
    mul_choi_sel = int(input("\nWhich section you want to choose: \n1. History Section\n"))
    if mul_choi_sel == 1: multiple_history_section()
    else: print("\nI think something wrong try again\n") ; multiple_choice_selector()

def true_or_false():
    pass

def section_selector():
    print("""\nList of Quiz sections are given below:
1. Geographical Section
2. History Section
3. Programming Fundamental Section """)
    section_selection = int(input("\nSelect which section that you want to solve the answer >>> "))
    if section_selection == 1: geographical_question()
    elif section_selection == 2 : history_question()
    elif section_selection == 3 : programming_fundamental()
    else: print("You pick the wrong section")

def quiz_types():
    print("""\nWhich type of Quiz you want to play ? 
1. No Choice Question
2. Multiple Choice Question
3. True or False Question """)
    quiz_types_selector = int(input("\nWhich type of Quiz that you want to solve ? "))
    if quiz_types_selector == 1 : section_selector()
    elif quiz_types_selector == 2 : multiple_choice_selector()
    elif quiz_types_selector == 3 : true_or_false()
    else: print("You pick the wrong question type")


def quit():
    print("""\nThanks for try our program.
if you want to give the feedback or anytype of suggestion.
Please contact mymail@gmail.com\n""")

print("Welcome to the World toughest quiz game\U0001f600")

print("""\nBefore we start, Read the instruction proparly
1. This quiz contains the more number of quiz than you expected
2. And this is a beginner project, So don't expect industry level user experienc
3. Updates always comming up \n""")

start = input("Lets start the Quiz: (Yes/No) >>> ").lower()
print("\n")
quiz_types() if start == "yes" else quit() if start == "no" else print("You must be type something wrong ")
