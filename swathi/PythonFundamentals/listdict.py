my_dict = dict()
 
bookid = input("Enter key and value separated by colon (:) ")
key,value = bookid.split(":")
bookname = input("Enter key and value separated by colon (:) ")
key1,value1 = bookname.split(":")
authorname = input("Enter key and value separated by colon (:) ")
key2,value2 = authorname.split(":")
price = input("Enter key and value separated by colon (:) ")
key3,value3 = price.split(":")
 

 
my_dict[key] = value
my_dict[key1] = value1
my_dict[key2] = value2
my_dict[key3] = value3
print("-"*30)


for key,value in my_dict.items():
    print('{0} : {1}'.format(key,value))
    
  
------------output-------------

Enter key and value separated by colon (:) BookId:10001
Enter key and value separated by colon (:) BookName:Python
Enter key and value separated by colon (:) AuthorName:Swathi
Enter key and value separated by colon (:) Price:1500
------------------------------
BookId : 10001
BookName : Python
AuthorName : Swathi
Price : 1500
