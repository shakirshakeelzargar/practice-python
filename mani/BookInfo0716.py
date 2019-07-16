bookList = []

# Get the book details from the user
def getBookDetails():
    bookDetails = True
    while bookDetails:
        bookId = input('Enter the Book id: ')
        while(len(bookId) == 0 or bookId.isalpha()):
            print("Book Id should be numeric/alphanumeric cannot be empty/alphabet")
            bookId = input('Enter the Book id: ')
        bookName = input('Enter the Book Name: ')
        while(len(bookName) == 0):
            print("Book Name should not be empty")
            bookName = input('Enter the Book Name: ')
        bookAuthorName = input('Enter the Book Author Name: ')
        while(len(bookAuthorName) == 0 or bookAuthorName.isdigit()):
            print("Book Author Name should be valid name cannot be empty/numerics")
            bookAuthorName = input('Enter the Book Author Name: ')
        bookPrice = input('Enter the price of the book: ')
        while(len(bookPrice) == 0 or bookPrice.isalpha()):
            print("Book Price should be a numeric value cannot be empty/alphabets.")
            bookPrice = input('Enter the Book Price: ')

        #Storing the prompted book details in the dictionary bookInfo
        bookInfo = {'Id': bookId, 'Name': bookName,
                    'Author': bookAuthorName, 'Price': bookPrice}
        #Appending the dict to a list                    
        bookList.append(bookInfo)

        #Prompting the user to check for the next book details
        anotherBookInput = input(
            "Do you want to enter another book details (Y or N): ").upper()
        if(anotherBookInput != "Y" and anotherBookInput != "YES"):
            bookDetails = False


#Print the book details retrieved from user
def printBookDetails():
    print("Following are the book details")
    # Approach 1:
    for bookInfo in bookList:
        print("Book Id : {b[Id]}, Name : {b[Name]}, Author : {b[Author]}, Price : {b[Price]} ".format(
            b=bookInfo))

    # Approach 2:
    for bookIndex in range(len(bookList)):
        print("Book Id : {b[Id]}, Name : {b[Name]}, Author : {b[Author]}, Price : {b[Price]} ".format(
            b=bookList[bookIndex]))


getBookDetails() 
printBookDetails()