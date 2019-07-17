#Largest of three numbers using Ternary Operation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largestNum=num1 if (num1 > num2) and (num1 > num3) else num2 if (num2 > num1) and (num2 > num3) else num3
print("The largest number is : {}".format(largestNum))


#Dictionary with user input
try:
    n=int(input("Enter no of books"))
    d={}

    i=1

    while(i<=n):
        bid=[]
        bname=[]
        bauthor=[]
        bprice=[]
        d1={}
        bookid=input("Enter book id : ")
        bookname=input("Enter book name : ")
        bookauthor=input("Enter book author : ")
        bookprice=input("Enter book price : ")
        bid.append(bookid)
        bname.append(bookname)
        bauthor.append(bookauthor)
        bprice.append(bookprice)
        for a in range(1):
            d1['BookId']=bid[a]
            d1['Book Name']=bname[a]
            d1['Book Author']=bauthor[a]
            d1['Book Price']=bprice[a]
            d[(i)]=d1  
        #print("Book Details Are ", d)
        i=i+1
        del d1
    #for det in d.items():
        #print(det)
    #print("Book Details Are ", d)
    #for det in d.items():
              #print(det)
            #for fulldet in det:
               # print(fulldet)
except:
    print("Invalid number of books/error")
else:
    
    for det in d:
        print("{}".format(det))
        print('Book Id : ' + d[det]['BookId'])
        print('Book name : ' +d[det]['Book Name'])
        print('Book Authorr : ' +d[det]['Book Author'])
        print('Book Priceee : ' +d[det]['Book Price'])
        print("=========================")


#output
'''
Enter no of books2
Enter book id : 10000
Enter book name : 1stbook
Enter book author : firstauthor
Enter book price : 1000
Enter book id : 20000
Enter book name : 2ndbook
Enter book author : secondauthor
Enter book price : 2000
1
Book Id : 10000
Book name : 1stbook
Book Authorr : firstauthor
Book Priceee : 1000
=========================
2
Book Id : 20000
Book name : 2ndbook
Book Authorr : secondauthor
Book Priceee : 2000
=========================
'''


#Read file by line(user input)
prompt=input("Enter 'read' to read or 'write' to write the file : ")
if(prompt=='read'):
    try:
        lineNum=int(input("Enter the line you wish to read : "))
        with open("d:/demodata/data.csv","r") as f:
            fileByLine = f.read().split('\n')[lineNum]
    except:
        print('Invalid row')
    else:
        print(fileByLine)
        f.close()
elif(prompt=='write'):
    writeText=input("Enter the text you want to write in the file : ")
    with open("d:/demodata/data.csv","a") as f:
        f.write(writeText + " \n")
        f.close()
else:
    print("Invalid entry")

#output
'''
Enter 'read' to read or 'write' to write the file : read
Enter the line you wish to read : 1464
rrrrrrrrrrrr 
'''


#To see the csv file from reverse
for line in reversed(list(open("d:/demodata/data.csv","r"))):
    print(line.rstrip()


#MethoD2 to read csv file from url
#https://github.com/swaathi/eda/blob/master/data.csv
from urllib.request import urlopen, Request
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
file_url = "https://raw.githubusercontent.com/swaathi/eda/master/data.csv"
req = Request(url=file_url) 
file = str(urlopen(req).read())
print(file)


#Read CSV file using csv library
import csv
with open("d:/demodata/data.csv","r")as f:
    data = csv.reader(f)
    for row in data:
        print(row)


#iterating dictionary with index,keys and values
personAddress = { 
                     'Rahul' : 'Haryana', 
                     'Shakir' : 'Srinagar', 
                     'Swathi' : 'Chennai', 
                     'Divya' : 'Chennai',
                     'Sachin':'Mumbaii'
                    } 
for i, (k, v) in enumerate(personAddress.items()):
    print("index: {}, key: {}, value: {}".format(i, k, v))


        
    
