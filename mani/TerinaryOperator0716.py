import urllib.request as url
from itertools import islice


# Ternary operator approach to find maximum of 3 no's.
def ternaryOperator(x, y, z):
    maxNo = x if (x > y and x > z) else (y if y > z else z)
    print(maxNo)


# Read the file from the web and read it based on used input line no.
def readFileOnLineNumber(lineToRead):
    while(len(lineToRead) == 0 or lineToRead.isalpha()):
        print("Line Number should be numeric cannot be empty/alphabet")
        lineToRead = input('Enter the line number to read: ')

    # Approach 1
    # Using a package urllib.request to read a file from web
    with url.urlopen("https://raw.githubusercontent.com/swaathi/eda/master/data.csv") as infile:
        for i, lines in enumerate(infile):
            if i == int(lineToRead)-1:
                print(lines)
                totalWords = len(str(lines).split(","))
                print("Total no. of comma seperated words: {}".format(totalWords))
                break

    # Approach 2:
    lineToRead = int(lineToRead)
    with url.urlopen("https://raw.githubusercontent.com/swaathi/eda/master/data.csv") as infile:
        # Return an iterator whose next() method returns selected values from an iterable. Works like a slice() on a list but returns an iterator.
        for line in islice(infile, lineToRead-1, lineToRead):
            print(line)


ternaryOperator(200, 2520, 318)
readFileOnLineNumber(input('Enter the line number to read: '))

'''
Output:
-------------
Max no using ternary operator: 2000

##File read execerise
Enter the line number to read: 10
b'9,50,RM,51,6120,Pave,NA,Reg,Lvl,AllPub,Inside,Gtl,OldTown,Artery,Norm,1Fam,1.5Fin,7,5,1931,1950,Gable,CompShg,BrkFace,Wd Shng,
None,0,TA,TA,BrkTil,TA,TA,No,Unf,0,Unf,0,952,952,GasA,Gd,Y,FuseF,1022,752,0,1774,0,0,2,0,2,2,TA,8,Min1,2,TA,Detchd,1931,Unf,2,468,Fa,
TA,Y,90,0,205,0,0,0,NA,NA,NA,0,4,2008,WD,Abnorml,129900\n'
Total no. of comma seperated words: 81
'''
