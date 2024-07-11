# Texet (v2.0.0)
Texet is a terminal-based text manipulation program that allows you to quickly and efficiently apply bulk changes to a piece of text.


## Usage

python3 texet.py -i 'target text' {options}
    
## GENERAL

-h, --help: Print this list

-i, --input: Specify the text that will be manipulated
    
## OPTIONS

-c, --case: Change the text case to [u]ppercase, [l]owercase, or [t]itlecase

-d, --divide: Divide text into a list by [w]ord or [c]haracter

-r, --remove: Remove a specified character from the text

-a, --array: Convert text to a Python array by [w]ord or [c]haracter

NOTE: Options will be applied in the order you enter them

## EXAMPLE

python3 texet.py -i 'Welcome to texet!' -c l -r e -a w

Result: ['wlcom', 'to', 'txt!']
