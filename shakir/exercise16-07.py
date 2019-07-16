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


        
    
