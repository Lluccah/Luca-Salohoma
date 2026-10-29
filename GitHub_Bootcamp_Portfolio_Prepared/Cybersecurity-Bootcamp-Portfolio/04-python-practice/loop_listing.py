# Creat a list containing five of your favorite movies
favorite_movies = ["Inception",
                   "The Matrix",
                   "Interstellar",
                   "The Dark Knight",
                   "Pulp Fiction"   
]
# loop through each movie in the list
for movie in favorite_movies:
    # print the word "Movie:" followed by the name of the movie
    print("Movie:", movie)

    # print a blank line to separate each movie in the output
    print()

    # Use enumerate() to get both the movie and its position
    # start=1 makes the numbering begin at 1 instaed of 0
    for number, movie in enumerate(favorite_movies, start=1):

        # print the movie number and its name 

        print("Movie", number, ":", movie)

