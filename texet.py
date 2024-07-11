########################################
#
#  Name: Austin Schwalbe
#  Last updated: July 11, 2024
#  Description: Automatically turns a phrase into a list of words
#
########################################
import webbrowser, sys

### class for user input
class system:
    com_all = ['-h', '--help', '-i', '--input', '-r', '--remove', '-d', '--divide']
    com = ""    # entire command
    inp = ""    # inputted text
    orig = ""   # original text
    
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

### function for printing input text
def printInput(inp):

    # print header
    print(colors.BOLD + "\n<< INPUT >>" + colors.ENDC)
	
    # print input text
    print(inp)

### function for printing output line
def printOutput(output):

	# print header
	print(colors.BOLD + "\n<< OUTPUT >>" + colors.ENDC)
	
	# print output text
	print(output)
    
### function for responding to invalid input
def invalidInput(error_msg):
    print(colors.FAIL + f"\n{error_msg}" + colors.ENDC)
    exit(0)

### function for printing help menu
def printHelp():
    print("Texet 2.0 (by Austin Schwalbe)")
    print("Usage: python3 texet.py -i 'target text' {options}")
    
    print("\nGENERAL")
    print("=======")
    print("-h, --help: Print this list")
    print("-i, --input: Specify the text that will be manipulated")
    
    print("\nOPTIONS")
    print("=======")
    print("-c, --case: Change the text case to [u]ppercase, [l]owercase, or [t]itlecase")
    print("-d, --divide: Divide text into a list by [w]ord or [c]haracter")
    print("-r, --remove: Remove a specified character from the text")
    print("-a, --array: Convert text to a Python array by [w]ord or [c]haracter")
    print("NOTE: Options will be applied in the order you enter them")
    
    print("\nEXAMPLE")
    print("=======")
    print("python3 texet.py -i 'Welcome to texet!' -c l -r e -a w")
    print("Result: ['wlcom', 'to', 'txt!']")

######
######      FUNCTIONS FOR TEXT MANIPULATION
######

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
    	return output
    
    # otherwise, let the user know the input is invalid
    else: invalidInput("Please enter 'w' or 'c' to split by words or characters")
    
### function for changing text case
def printCase(inp, opt):
	
	# print UPPERCASE
	if opt == "u": inp = inp.upper()
	
	# print lowercase
	elif opt == "l": inp = inp.lower()
	
	# print Title Case
	elif opt == "t": inp = inp.title()
	
	# otherwise, let the user know the input is invalid
	else: invalidInput("Please enter 'u', 'l', or 't' to convert to UPPER CASE, lower case, or Title Case")

	# return the result
	return inp

### function for removing characters
def removeChar(inp, char):
	
	output = ""
	
	# iterate through input...do not include entered character
	for c in inp:
		if c != char: output += c
	
	# print output
	return output

### function for printing arrays
def printArray(inp, opt):

    # print word output
    if opt == ("w"):
        code_array = inp.split()
        return code_array
    
    # print character output
    elif opt == ("c"):
        code_array = [char for char in inp]
        return code_array
            
    # otherwise, let the user know the input is invalid
    else: invalidInput("Please enter 'w' or 'c' to split by words or characters")

###################################################################
#########################   DRIVER CODE   #########################
###################################################################

# ----- interate through list and find options ----- #
# run this process for each individual command to prevent duplicates

# get input from command line
system.com = sys.argv[1:]

# check for help first
for opt in system.com:

    # check for help
    if opt in ["-h", "--help"]:
        printHelp()
        exit(0)

# get input text from command line
for opt in system.com:

    if opt in ['-i', '--input']:
        loc = system.com.index(opt)
        try: system.inp = system.com[loc+1]
        except IndexError:
            print("Usage: python3 texet.py -i 'target text' {options}")
            exit(0)
        system.orig = system.inp
        if system.inp == "":
            print("Usage: python3 texet.py -i 'target text' {options}")
            exit(0)
        else: break
    else:
        print("Usage: python3 texet.py -i 'target text' {options}")
        exit(0)

# check for case
for opt in system.com:

    if opt in ["-c", "--case"]:
        
        loc = system.com.index(opt)
        try: param = system.com[loc+1]
        except IndexError:
            invalidInput("Please enter 'u', 'l', or 't' to convert to UPPER CASE, lower case, or Title Case")
            
        if param in ['u', 'l', 't']: system.inp = printCase(system.inp, param)

# check for divide
for opt in system.com:
    
    if opt in ["-d", "--divide"]:
        
        loc = system.com.index(opt)
        try: param = system.com[loc+1]
        except IndexError:
            invalidInput("Please enter 'w' or 'c' to split by words or characters")
            
        if param in ['w', 'c']: system.inp = printList(system.inp, param)


# check for remove
for opt in system.com:
    
    if opt in ["-r", "--remove"]:
        
        loc = system.com.index(opt)
        try: param = system.com[loc+1]
        except IndexError:
            invalidInput("Please enter a single character to remove")
            
        if (param not in system.com_all and len(param) == 1): system.inp = removeChar(system.inp, param)
        else: invalidInput("Please enter a single character to remove")

# check for array
for opt in system.com:
    
    if opt in ["-a", "--array"]:
        
        loc = system.com.index(opt)
        try: param = system.com[loc+1]
        except IndexError:
            invalidInput("Please enter 'w' or 'c' to split by words or characters")
            
        if param in ['w', 'c']: system.inp = printArray(system.inp, param)

# check if options were entered
if system.inp == system.orig:
    print("Usage: python3 texet.py -i 'target text' {options}")
    exit(0)

# ----- print the results ----- #
# this should only run if the command was successful are there were no errors

# print header
print("\n    <><><><><><><><><><>" + colors.HEADER)
print(" ___   ___  _____  ___   ___")
print("|_ _| |__/  \   /  \__| |_ _|")
print(" |_|  |__\  /_/_\  /__|  |_|")
print(colors.ENDC)
print("    <><><><><><><><><><>")
print(colors.OKGREEN)
print("   Austin Schwalbe • V2.0\n" + colors.ENDC)

# print the input
printInput(system.orig)

# finally, print the result
printOutput(system.inp)
