list1=[]

BookId=input("enter the bookid\n")
if(BookId.isdigit()):
    print("you entered number")
else:
    print("it is a string! please enter the number")
BookName=input("enter the bookname\n")

AuthorName=input("Enter the Authorname\n")
Price=float(input("enter the price\n"))
list1.append(BookId)
list1.append(BookName)
list1.append(AuthorName)
list1.append(Price)
print('-'*30)

for books in list1:
    print(books)
    
----------output---------

enter the bookid
1001
you entered number
enter the bookname
python
Enter the Authorname
swathi
enter the price
1000
------------------------------
1001
python
swathi
1000.0
