
Bookid = int(input("enter the bookid\n"))

bookname=input("enter the bookname\n")

authorname=input("enter tke authorname\n")

price=float(input("enter the price\n"))


class_list = {}

class_list['BookId'] = Bookid
class_list['BookName'] = bookname
class_list['AuthorName'] = authorname
class_list['Price'] = price


print(class_list)

------------------------o/p---------------------------

enter the bookid
1001
enter the bookname
Python
enter tke authorname
swathi
enter the price
1000
{'BookId': 1001, 'BookName': 'Python', 'AuthorName': 'swathi', 'Price': 1000.0}
