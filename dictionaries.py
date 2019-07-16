'''class_list = dict()
BookId = input('Enter column name & IdNumber separated by ":" \n')
temp = BookId.split(':')
class_list[temp[0]] = int(temp[1])
BookName = input('Enter column name & BookName separated by ":" \n')
temp1 = BookName.split(':')
class_list[temp[1]] = str(temp1[2])
AuthorName = input('Enter column name & AuthorName separated by ":" \n')
temp2 = AuthorName.split(':')
class_list[temp[2]] = str(temp2[3])
price = input('Enter column name & BookName separated by ":" ')
temp3 = price.split(':')
class_list[temp[3]] = float(temp3[4])
 
# Displaying the dictionary
for key, value in class_list.items():
	print('BookId: {}, Id: {}'.format(key, value))
    #print('BookName: {}, bname: {}'.format(key, value))
    #print('AuthorName: {}, aname: {}'.format(key, value))
    #print('Price: {}, bprice: {}'.format(key, value))'''

colname1 = input("enter the key 1\n")
Bookid = int(input("enter the bookid\n"))
colname2=input("enter the columnname 2\n")
bookname=input("enter the bookname\n")
colname3=input("enter columnname 3\n")
authorname=input("enter tke authorname\n")
colname4=input("enter columnname 4\n")
price=float(input("enter the price\n"))


class_list = {}

class_list[colname1] = Bookid
class_list[colname2] = bookname
class_list[colname3] = authorname
class_list[colname4] = price


print(class_list)
#for book in class_list:
    #print(book.items())