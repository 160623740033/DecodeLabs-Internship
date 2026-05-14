def recommend_movie():
    print("🎬 Welcome to AI Movie Recommendation System")

    print("\nChoose a genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Romance")
    print("4. Horror")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nRecommended Movies:")
        print("- Avengers")
        print("- John Wick")
        print("- Mad Max")

    elif choice == "2":
        print("\nRecommended Movies:")
        print("- Mr. Bean")
        print("- The Mask")
        print("- Hangover")

    elif choice == "3":
        print("\nRecommended Movies:")
        print("- Titanic")
        print("- The Notebook")
        print("- La La Land")

    elif choice == "4":
        print("\nRecommended Movies:")
        print("- Conjuring")
        print("- Annabelle")
        print("- It")

    else:
        print("Invalid choice. Please try again.")

# Run
recommend_movie()