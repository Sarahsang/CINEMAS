# Lincoln Cinemas Model
# Author: Miao Sang
# Purpose: To provide a model for the Lincoln Cinemas application.
# Date: 28/09/2023

class User:
    """! Represents a generic user."""
    
    def __init__(self, username: str, password: str) -> None:
        """! Initialize the User object.
        @param username: The username of the user.
        @param password: The password of the user.
        """
        pass


class Admin(User):
    """! Represents an administrator."""
    
    def __init__(self, username: str, password: str) -> None:
        """! Initialize the Admin object.
        @param username: The username of the admin.
        @param password: The password of the admin.
        """
        super().__init__(username, password)


class FrontDesk(User):
    """! Represents a front desk staff member."""
    
    def __init__(self, username: str, password: str) -> None:
        """! Initialize the FrontDesk object.
        @param username: The username of the front desk staff member.
        @param password: The password of the front desk staff member.
        """
        super().__init__(username, password)


class Customer(User):
    """! Represents a customer."""
    
    def __init__(self, username: str, password: str, email: str) -> None:
        """! Initialize the Customer object.
        @param username: The username of the customer.
        @param password: The password of the customer.
        @param email: The email of the customer.
        """
        super().__init__(username, password)
        self.email = email


class Guest(User):
    """! Represents a guest user."""
    
    def __init__(self) -> None:
        super().__init__(None, None)


class Movie:
    """! Represents a movie."""
    
    def __init__(self, title: str, genre: str, rating: str, duration: int, releaseDate: str) -> None:
        """! Initialize the Movie object.
        @param title: The title of the movie.
        @param genre: The genre of the movie.
        @param rating: The rating of the movie.
        @param duration: The duration of the movie.
        @param releaseDate: The release date of the movie.
        """
        self.title = title
        self.genre = genre
        self.rating = rating
        self.duration = duration
        self.releaseDate = releaseDate


class Screening:
    """! Represents a screening of a movie in a particular hall."""
    
    def __init__(self, movie: Movie, hall_number: int, time: str) -> None:
        """! Initialize the Screening object.
        @param movie: The movie to be screened.
        @param hall_number: The hall number where the movie will be screened.
        @param time: The time of the screening.
        """
        pass


class Seat:
    """! Represents a seat in a movie hall."""
    
    def __init__(self, row: int, column: int, is_booked: bool) -> None:
        """! Initialize the Seat object.
        @param row: The row number of the seat.
        @param column: The column number of the seat.
        @param is_booked: Whether the seat is booked or not.
        """
        pass


class System:
    """! Represents the system for handling notifications and other system-level tasks."""
    
    def send_notification(self, user: User, message: str) -> None:
        """! Send a notification to a specific user.
        @param user: The user to send the notification to.
        @param message: The message to send.
        """
        pass

class Movie:
    """! Represents a movie."""
    
    def search_by_title(self, title: str) -> List[Movie]:
        """! Searches movies by their title.
        @param title: The title to search for.
        """
        pass

    def search_by_language(self, language: str) -> List[Movie]:
        """! Searches movies by their language.
        @param language: The language to search for.
        """
        pass

    def search_by_genre(self, genre: str) -> List[Movie]:
        """! Searches movies by their genre.
        @param genre: The genre to search for.
        """
        pass

    def search_by_release_date(self, release_date: str) -> List[Movie]:
        """! Searches movies by their release date.
        @param release_date: The release date to search for.
        """
        pass
