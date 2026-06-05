# Simple Recommendation System

movies = {
    "Action": ["Avengers", "Batman", "John Wick"],
    "Comedy": ["The Mask", "Mr. Bean", "Home Alone"],
    "Horror": ["The Conjuring", "Insidious", "IT"],
    "Sci-Fi": ["Interstellar", "Inception", "Avatar"]
}

print("=== Movie Recommendation System ===")
print("Available Categories:")
print("Action, Comedy, Horror, Sci-Fi")

user_choice = input("Enter your favorite category: ")

if user_choice in movies:
    print("\nRecommended Movies:")
    
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("Sorry! Category not found.")