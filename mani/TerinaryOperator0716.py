import urllib.request as url
from itertools import islice


# Ternary operator approach to find maximum of 3 no's.
def ternaryOperator(x, y, z):
    maxNo = x if (x>y and x>z) else (y if y>z else z) 
    print(maxNo)
   

# Read the file from the web and read it based on used input line no.
def readFileOnLineNumber(lineToRead):
    while(len(lineToRead) == 0 or lineToRead.isalpha()):
        print("Line Number should be numeric cannot be empty/alphabet")
        lineToRead = input('Enter the line number to read: ')

    # Approach 1
    # Using a package urllib.request to read a file from web
    with url.urlopen("https://raw.githubusercontent.com/swaathi/eda/master/data.csv") as demo:        
        for i, lines in enumerate(demo):
            if i == int(lineToRead)-1:
                print(lines)
                totalWords = len(str(lines).split(","))
                print("Total no. of comma seperated words: {}".format(totalWords))
                break

    # Approach 2:
    lineToRead = int(lineToRead)
    with url.urlopen("https://raw.githubusercontent.com/swaathi/eda/master/data.csv") as demo:
        # Return an iterator whose next() method returns selected values from an iterable. Works like a slice() on a list but returns an iterator.
        for line in islice(demo, lineToRead-1, lineToRead):
            print(line)


ternaryOperator(2000, 252, 318)
readFileOnLineNumber(input('Enter the line number to read: '))
