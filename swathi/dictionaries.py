


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

----------output--------------

enter the bookid
1100
enter the bookname
Python
enter tke authorname
Swathi
enter the price
2000
{'BookId': 1100, 'BookName': 'Python', 'AuthorName': 'Swathi', 'Price': 2000.0}
