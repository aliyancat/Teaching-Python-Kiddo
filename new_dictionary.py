
movies = {

    "Avengers Endgame": 50,
    "The Lion King": 45,
    "Frozen  2  ": 40
}



while True:
    print("\n======ALI'S MOVIE THEATER======\n")
    print ("1. View remaining  seats")
    print ("2. Book a ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Remaining Tickets for each movie\n")

        for movie in movies:
            print(f"{movie} Seats Left: {movies[movie]}")

    elif choice == "2":
        movie_name = input("Enter the name  of the movie you want to watch")
        if movie_name not in movies:
            print("Sorry, this movie is not being featured here ")
        elif movie_name in movies:
            if movies[movie_name] > 0:
                movies[movie_name] = movies[movie_name] - 1
                print(f"You have successfully booked a ticket for {movie_name} ")
            else:
                print("Sorry, this movie is sold out !!")

    elif choice == "3":
        movie_name  = input("Enter the name of the  movie")

        if movie_name not in  movies:
            print("Sorry, this movie is not being featured here ")
        else:
            movies[movie_name] = movies[movie_name] + 1
            print(f"You have successfully cancelled your ticket for {movie_name} ") 

    elif choice == "4":
        print("Thank you for visiting our website. Goodbye !")
        break

        

            


    