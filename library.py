

books = ["Blue , Berry and Pancakes", "The Diary of a Wimpy Kid","Dog Man", "Computer Mouse"]


borrowed_books = []


while True:
    print("=============================================\n")
    print(("Welcome to OUR Library\n"))
    print("1. View available books")
    print("2. Borrow a book")   
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Exit\n")

    choice =  input("Enter your choice: ")

    if choice == "1":
        for book in books:
            print(book)
    


    elif choice == "2":
        book_name = input("Enter the name of the book you want to borrow:")
        
        if book_name in books:

            print("Book is available. Here you can take it.\n")
            borrowed_books.append(book_name)
            books.remove(book_name)

        elif book_name in borrowed_books:
            print("Sorry the book has already been borrowed\n")

        else:
            print("Sorry the book is not available in our library\n")



    elif choice == "3":
        book_name = input("Enter the name of the book you want to return: ")

        if book_name in borrowed_books: 
            print("Thank you for returning the book\n")
        else:
            print("This book is not from our library\n")



    elif choice == "4":
        book_name = input("Enter the name of the book you want to search: ")
        
        if book_name in books:
            print("This book is available in our library\n ")

        elif book_name in borrowed_books:
            print("Sorry the book has already been borrowed\n")

        else:
            print("Sorry the book is not available in our library\n")

    # Add the choice 5 by yourself coders !!



        


    


        