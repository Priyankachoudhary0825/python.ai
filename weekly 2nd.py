# admin.py

# Data list
data = [
    {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]


# Function to get integer input
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter an integer greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Function to get non-empty string input
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Input cannot be empty.")


# Function to add movie
def add_movie():
    name = input_something("Enter movie name: ")
    year = input_int("Enter release year: ")
    duration = input_int("Enter duration (minutes): ")

    genres = []
    print("Enter genres (type 'done' to finish):")
    while True:
        genre = input_something("Genre: ")
        if genre.lower() == "done":
            if len(genres) == 0:
                print("You must enter at least one genre.")
            else:
                break
        else:
            genres.append(genre)

    new_movie = {
        "name": name,
        "year": year,
        "duration": duration,
        "genres": genres
    }

    data.append(new_movie)
    print(f"{name} added successfully.\n")


# Function to list movies
def list_movies():
    if len(data) == 0:
        print("No movies saved.\n")
    else:
        for i, movie in enumerate(data, start=1):
            print(f"{i}) {movie['name']} ({movie['year']})")
        print()


# Function to search movies
def search_movies():
    if len(data) == 0:
        print("No movies saved.\n")
        return

    term = input_something("Enter search term: ").lower()

    found = False
    for i, movie in enumerate(data, start=1):
        if term in movie["name"].lower():
            print(f"{i}) {movie['name']} ({movie['year']})")
            found = True

    if not found:
        print("No matching movies found.")
    print()


# Function to view movie details
def view_movie():
    if len(data) == 0:
        print("No movies saved.\n")
        return

    index = input_int("Enter movie index number: ")

    if index < 1 or index > len(data):
        print("Invalid index number.\n")
    else:
        movie = data[index - 1]
        print(f"\nName: {movie['name']}")
        print(f"Year: {movie['year']}")
        print(f"Duration: {movie['duration']} minutes")
        print("Genres:", ", ".join(movie["genres"]))
        print()


# Function to delete movie
def delete_movie():
    if len(data) == 0:
        print("No movies saved.\n")
        return

    index = input_int("Enter movie index number: ")

    if index < 1 or index > len(data):
        print("Invalid index number.\n")
    else:
        removed = data.pop(index - 1)
        print(f"{removed['name']} deleted successfully.\n")


# Main program loop
while True:
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("Enter choice: ").lower()

    if choice == "a":
        add_movie()
    elif choice == "l":
        list_movies()
    elif choice == "s":
        search_movies()
    elif choice == "v":
        view_movie()
    elif choice == "d":
        delete_movie()
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")