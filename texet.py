########################################
#
#  Name: Austin Schwalbe
#  Last updated: May 17, 2024
#  Description: Automatically turns a phrase into a list of words
#
########################################
import webbrowser

### class for user input
class userin:
    words = ""
    option = ""
    suboption = ""
    suboption2 = ""
    
### class of colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### function for getting input
def getInput(prompt):

    # print prompt
    print(colors.OKBLUE + prompt + colors.ENDC)

    # get user input
    getinput = input("> ")
    return getinput

### function for printing output line
def printOutput(output):

	# print header
	print(colors.BOLD + "\n<< OUTPUT >>" + colors.ENDC)
	
	# print output text
	print(output)
    
### function for responding to invalid input
def invalidInput():
	print("That is not a valid option...")
	exit(1)

### function for checking suboption input
def checkSuboption(sub):
    if sub in ["w", "word"]: return "w"
    elif sub in ["c", "char", "character"]: return "c"
    elif sub in ["1", "2", "3"]: return sub
    else: invalidInput()

### function for printing list
def printList(inp, opt):

    # print word output
    if opt == ("w"):
    	output = ""
    	words = inp.split()
    	for i in range(len(words)):
    		word = words[i]
    		if i == len(words)-1: output += f"{word}"
    		else: output += f"{word}\n"
    	printOutput(output)
    
    # print character output
    elif opt == ("c"):
    	output = ""
    	for i in range(len(inp)):
    		char = inp[i]
    		if i == len(inp)-1: output += f"{char}"
    		else: output += f"{char}\n"
    	printOutput(output)
    
    # otherwise, let the user know the input is invalid
    else: invalidInput()

### function for printing text between words
def printTextAdd(inp, opt, add):
    
    # print output for words
    if opt == "w":
    	output = inp.replace(" ", f"{add}")
    	printOutput(output)
    
    # print output for characters
    elif opt == "c":
    	 
    	 output = ""
    	 
    	 # iterate through input
    	 for i in range(len(inp)):
    	 	if i == len(inp)-1: output += inp[i]
    	 	else: output += f"{inp[i]}{add}"
    	 printOutput(output)

### function for changing text case
def printCase(inp, opt):
	
	# print UPPERCASE
	if opt == "1": printOutput(inp.upper())
	
	# print lowercase
	elif opt == "2": printOutput(inp.lower())
	
	# print Title Case
	elif opt == "3": printOutput(inp.title())
	
	# otherwise, let the user know the input is invalid
	else: invalidInput()

### function for removing characters
def removeChar(inp, char):
	
	output = ""
	
	# iterate through input...do not include entered character
	for c in inp:
		if c != char: output += c
	
	# print output
	printOutput(output)

### function for printing arrays
def printArray(inp, opt):

    # print word output
    if opt == ("w"):
        code_array = userin.words.split()
        printOutput(code_array)
    
    # print character output
    elif opt == ("c"):
        code_array = [char for char in inp]
        printOutput(code_array)
            
    # otherwise, let the user know the input is invalid
    else: invalidInput()

###################################################################
#########################   DRIVER CODE   #########################
###################################################################
    
# print header
print("\n    <><><><><><><><><><>" + colors.HEADER)
print(" ___   ___  _____  ___   ___")
print("|_ _| |__/  \   /  \__| |_ _|")
print(" |_|  |__\  /_/_\  /__|  |_|")
print(colors.ENDC)
print("    <><><><><><><><><><>")
print(colors.OKGREEN)
print("   Austin Schwalbe • V1.0\n\n" + colors.ENDC)

# prompt user for input
userin.words = getInput("Enter the text you want to process:")
print("")
userin.option = getInput("What would you like to do?\n" + 
                         "1. Make a list\n" + 
                         "2. Insert text\n" +
                         "3. Change case\n" +
                         "4. Remove character\n" +
                         "5. Generate Python array\n" +
                         "98. Leave feedback\n" +
                         "99. Exit program")

# select option based on input
# if "1", turn the input into a list divided by newlines
if userin.option == "1":
    userin.suboption = getInput("\nChoose whether to divide by [w]ord or [c]haracter:")
    userin.suboption = checkSuboption(userin.suboption)
    printList(userin.words, userin.suboption)

# if "2", add some text between each character or word in the input
elif userin.option == "2":
    userin.suboption = getInput(
    					"\nChoose whether to add text between each [w]ord or [c]haracter:")
    userin.suboption = checkSuboption(userin.suboption)
    userin.suboption2 = getInput("\nEnter the text you want to add:")
    printTextAdd(userin.words, userin.suboption, userin.suboption2)

# if "3", change case
elif userin.option == "3":
	userin.suboption = getInput("\nChoose how to apply case:\n" + 
    					"1. UPPERCASE\n" + 
    					"2. lowercase\n" +
    					"3. Title Case")
	userin.suboption = checkSuboption(userin.suboption)
	printCase(userin.words, userin.suboption)

# if "4", remove an inputted character
elif userin.option == "4":
	userin.suboption = getInput("\nType character you want to remove:")
	removeChar(userin.words, userin.suboption)

# if "5", turn text into a code array
elif userin.option == "5":
    userin.suboption = getInput("\nChoose whether to divide by [w]ord or [c]haracter:")
    userin.suboption = checkSuboption(userin.suboption)
    printArray(userin.words, userin.suboption)

# if "98", take users to a Google Form to enter feedback
elif userin.option == "98": webbrowser.open("https://forms.gle/Rv4cfGTRC17ek7YP7", new = 2, autoraise = True)

# if "99", exit the program
elif userin.option == "99": exit(0)

# if all else fails, exit the program
else: invalidInput()
