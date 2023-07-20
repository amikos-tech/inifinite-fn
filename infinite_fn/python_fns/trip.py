"""
This file contains functions related to trip organization which include finding the distance between two locations, finding the types of transportation between two locations, and finding the cost of transportation between two locations.
It also includes booking  of a trip.
"""
import random
import uuid


def distance_between_two_locations(location1: str, location2: str) -> int:
    """
    Find the distance between two locations.

    :param location1: The first location
    :param location2: The second location
    :return: The distance between the two locations in kilometers
    """
    return random.randint(1, 1000)


def types_of_transportation_between_two_locations(location1: str, location2: str):
    """
    Provides transportation options between two locations.

    :param location1: The first location
    :param location2: The second location
    :return: A list of transportation types which can be used to travel between the two locations. Possible values are "car", "bus", "train", and "plane".
    """
    transportation_types = ["car", "bus", "train", "plane"]
    return [transportation_types[x - 1] for x in range(random.randint(1, len(transportation_types)))]


def cost_of_transportation_between_two_locations(location1: str, location2: str, transportation_type: str,
                                                 currency: str = "$") -> int:
    """
    Find the cost of transportation between two locations within the same geographical region.

    :param location1: The name of the first location such as a city or airport or place
    :param location2: The name of the second location such as a city or airport or place
    :param transportation_type: The type of transportation
    :param currency: The currency to use for the cost
    :return: The cost of transportation between the two locations in currency
    """
    return f"{random.randint(1, 1000)} {currency}"


trip_bookings = {}


def book_trip(location1: str, location2: str, transportation_type: str, cost: int, date: str) -> str:
    """
    Book a trip between two locations.

    :param location1: The first location
    :param location2: The second location
    :param transportation_type: The type of transportation
    :param cost: The cost of transportation between the two locations in dollars
    :param date: The date of the trip. This is a string in the format "YYYY-MM-DD HH:MM:SS"
    :return: A string containing the booking information
    """
    booking_id = str(uuid.uuid4())

    trip_bookings[booking_id] = (location1, location2, transportation_type, cost, date)
    return f"Booking ID: {booking_id}\nLocation 1: {location1}\nLocation 2: {location2}\nTransportation Type: {transportation_type}\nCost: {cost}"


def cancel_trip(booking_id: str) -> str:
    """
    Cancel a trip by booking ID.

    :param booking_id: The booking ID
    :return: A string containing the cancellation information
    """
    if booking_id in trip_bookings:
        del trip_bookings[booking_id]
        return f"Booking ID: {booking_id} cancelled."
    else:
        return f"Booking ID: {booking_id} not found."
