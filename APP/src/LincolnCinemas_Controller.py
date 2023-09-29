"""! @brief Lincoln Cinemas program with Doxygen style comments"""

##
# @mainpage Lincoln Cinemas Application project
# 
# @section description_main description
# an python program that allows users to book tickets for movies at Lincoln Cinemas.
#
# @section requirements_main requirements
# @subsection requirements_functional_main Functional Requirements
# - The system shall allow users to search for movies based on title, language, genre, and release date.
# - The system shall allow users to book tickets for a particular screening.
# - The system shall allow users to cancel their ticket bookings.
# - The system shall allow users to apply discount coupons to their bookings.
# - The system shall allow users to pay for their bookings using credit card, debit card, or cash.
# - The system shall allow users to receive notifications for new movies, bookings, and cancellations.
# - The system shall allow admins to add new movies.
# - The system shall allow admins to add new screenings for movies.
# - The system shall allow admins to cancel screenings.
# - The system shall allow front desk staff to make ticket bookings for customers.
# - The system shall allow front desk staff to cancel ticket bookings for customers.
#
# @subsection requirements_nonfunctional_main Non-Functional Requirements
# - The system shall be available 24/7.
# - The system shall be able to handle 4 concurrent halls.
# - The system shall be able to handle 400 concurrent seats.
#
# @section assumptions_main assumptions
# - The system will be used by customers, admins, guest, system and front desk staff.
#
# @section constraints_main constraints
# - The system will be developed using Python.
# - The system will be developed using the MVC architecture.
# - The system will be developed using the GitHub repository.
# - The system will be developed using the Doxygen documentation system.

##
# @file LincolnCinemas_Controller.py
# @brief This file contains the controller classes for the Lincoln Cinemas application.
# @details This file contains the controller classes for the Lincoln Cinemas application.
# @section description_controller description
# Implementation for Lincoln Cinemas application
# @section requirements_main requirements
#
# @section author_main author
# - Created by Miao Sang on 29/09/2023

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
