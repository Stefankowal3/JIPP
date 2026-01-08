movies = {"Finding Nemo":[5,2], "Moana":[6,3], "Batman":[18,5], "The Lion King":[10,4]}

while True:
    movie_title = input("Enter movie title: ").strip().title()
    
    if movie_title in movies:
        age = int(input("Enter your age: "))
        
        if age >= movies[movie_title][0]:
            if movies[movie_title][1] > 0:
                movies[movie_title][1] -= 1
                print(f"Ticket booked! Available tickets: {movies[movie_title][1]}")
            else:
                print("Sorry, no tickets available!")
        else:
            print(f"Sorry, you are too young. This movie is for ages {movies[movie_title][0]}+")
    else:
        print("Movie not found!")

