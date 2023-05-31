# =======CODE HUNTERS========
# GROUP MEMBERS ARE:
# 1.AMINA
# 2.LINTA
# 3.NOOR
# 4.NADIA
# 5.TAQADUS
# 6.SAMREEN
# GROUP NUMBER 5
# TICKET BOOKING SYSTEM

class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def display_details(self):
        print(f"Movie Title: {self.title}")
        print(f"Genre: {self.genre}")


class ActionMovie(Movie):
    def __init__(self, title):
        super().__init__(title, "Action")


class ComedyMovie(Movie):
    def __init__(self, title):
        super().__init__(title, "Comedy")


class DramaMovie(Movie):
    def __init__(self, title):
        super().__init__(title, "Drama")


class User:
    def __init__(self, name):
        self.name = name

    def book_ticket(self, movie):
        try:
            print(f"Welcome, {self.name}!")
            print("Let's book a movie ticket for you.")
            print("Here are the available movies:")
            movie.display_details()
        except Exception as e:
            print("Oops! An error occurred while booking the ticket.")
            print(f"Error Details: {str(e)}")


def main():
    try:
        # Create movies
        action_movies = [ActionMovie("The Avengers"), ActionMovie("Mission: Impossible"), ActionMovie("John Wick")]
        comedy_movies = [ComedyMovie("Anchorman"), ComedyMovie("Superbad"), ComedyMovie("The Hangover")]
        drama_movies = [DramaMovie("The Shawshank Redemption"), DramaMovie("Forrest Gump"), DramaMovie("Fight Club")]

        print("==== Movie Ticket Booking System ====")
        user_name = input("Please enter your name: ")
        user = User(user_name)

        print("Great, let's explore the movie options:")
        print("Action Movies:")
        for i, movie in enumerate(action_movies, start=1):
            print(f"{i}. {movie.title}")

        print("\nComedy Movies:")
        for i, movie in enumerate(comedy_movies, start=len(action_movies) + 1):
            print(f"{i}. {movie.title}")

        print("\nDrama Movies:")
        for i, movie in enumerate(drama_movies, start=len(action_movies) + len(comedy_movies) + 1):
            print(f"{i}. {movie.title}")

        while True:
            selected_movie = input("Enter the number corresponding to your preferred movie (or 'q' to quit): ")
            if selected_movie.lower() == "Q":
                break

            try:
                selected_movie = int(selected_movie)
                if 1 <= selected_movie <= len(action_movies):
                    user.book_ticket(action_movies[selected_movie - 1])
                    break
                elif len(action_movies) + 1 <= selected_movie <= len(action_movies) + len(comedy_movies):
                    user.book_ticket(comedy_movies[selected_movie - len(action_movies) - 1])
                    break
                elif len(action_movies) + len(comedy_movies) + 1 <= selected_movie <= len(action_movies) + len(comedy_movies) + len(drama_movies):
                    user.book_ticket(drama_movies[selected_movie - len(action_movies) - len(comedy_movies) - 1])
                    break
                else:
                    print("Invalid movie selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid movie number or 'q' to quit.")
    except Exception as e:
        print("Oops! An error occurred while running the program.")
        print(f"Error Details: {str(e)}")


if __name__ == "__main__":
    main()
