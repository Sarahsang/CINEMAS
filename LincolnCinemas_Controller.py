# Lincoln Cinemas Controller
# Author: Miao Sang
# Purpose: To provide a controller for the Lincoln Cinemas application.
# Date: 28/09/2023
from LincolnCinemas_Model import *
from typing import List

class CinemaController:
    """! Controller class to handle the functionalities."""
    
    def search_movies(self, title: str, language: str, genre: str, release_date: str) -> List[Movie]:
        """! Search movies based on given criteria.
        @param title: The title to search for.
        @param language: The language to search for.
        @param genre: The genre to search for.
        @param release_date: The release date to search for.
        @return: List of movies that match the criteria.
        """
        pass

    def book_ticket(self, customer: Customer, screening: Screening, seats: List[Seat]) -> bool:
        """! Book a ticket for a particular screening.
        @param customer: The customer who is booking the ticket.
        @param screening: The screening to book the ticket for.
        @param seats: The seats to book.
        @return: Confirmation status.
        """
        pass


class AdminController(CinemaController):
    """! Controller for Admin functionalities."""
    
    def add_new_movie(self, movie_details: dict) -> bool:
        """! Adds a new movie.
        @param movie_details: The details of the movie to be added.
        """
        pass
    
    def add_new_screening(self, screening_details: dict) -> bool:
        """! Adds a new screening for a movie.
        @param screening_details: The details of the screening to be added.
        """
        pass

    def cancel_screening(self, screening_id: int) -> bool:
        """! Cancels a screening.
        @param screening_id: The ID of the screening to be cancelled.
        """
        pass


class FrontDeskStaffController(CinemaController):
    """! Controller for Front Desk Staff functionalities."""
    
    def make_ticket_booking(self, booking_details: dict) -> bool:
        """! Makes a ticket booking.
        @param booking_details: The details of the booking.
        """
        pass

    def cancel_ticket_booking(self, booking_id: int) -> bool:
        """! Cancels a ticket booking.
        @param booking_id: The ID of the booking to be cancelled.
        """
        pass


class CinemaController:
    """! Represents the main controller for the cinema."""
    
    def display_available_screenings(self, movie: Movie) -> List[Screening]:
        """! Displays the available screenings for a selected movie.
        @param movie: The movie to display screenings for.
        """
        pass

    def select_screening(self, screening_id: int) -> Optional[Screening]:
        """! Allows customers to select a screening at a particular date and time.
        @param screening_id: The ID of the screening to select.
        """
        pass

    def show_seating_arrangement(self, hall_id: int) -> List[Seat]:
        """! Shows the seating arrangement of the cinema hall.
        @param hall_id: The ID of the cinema hall.
        """
        pass

    def apply_discount_coupon(self, coupon_code: str) -> bool:
        """! Allows customers to add a discount coupon to their payment.
        @param coupon_code: The discount coupon code.
        """
        pass

    def make_payment(self, payment_method: str) -> bool:
        """! Allows customers to pay with credit card or cash or debit card.
        @param payment_method: The payment method ('Credit Card', 'Cash', 'Debit Card').
        """
        pass

    def send_notification(self, message: str) -> bool:
        """! Sends notifications to customers for new movies, bookings, and cancellations.
        @param message: The notification message.
        """
        pass
