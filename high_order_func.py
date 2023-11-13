'''high order functions accepts functions as parameter and run them inside their body'''

def greet():
    print("hello")

def before_and_after(func):
    print("Before....")
    func()
    print("After....")

before_and_after(greet)

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Tiger Zinda Hai", "director": "Kabir Khan"},
    {"name": "The Irish Man", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]

def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie

find_by = input("What property are we searching by ?") # name or director
looking_for = input("What are you looking for ?")
print(find_movie(looking_for, lambda movie: movie[find_by]))
