MENU_PROMPT = "Enter 'add' to add a move, 'list' to see your movies, 'find' to find a movie by title, or 'quit' to quit:\n "
movies = []

def add_movie():
    title = input("Enter a move title:").strip().title()
    director = input("Enter the movie director:").strip().title()
    year = input("Enter the move release year:")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def show_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    search_title = input("Enter movie title you are looking for:")
    for movie in movies:
        if movie["title"] == search_title:

            print("movie found", movie)
        else:
            print("Movie not found")

user_options = {
    "add": add_movie,
    "list": show_movie,
    "find": find_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'quit':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command, Please try again ")

        selection = input(MENU_PROMPT)

menu()

