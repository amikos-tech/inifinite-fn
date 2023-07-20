import random
import string


def get_all_lodgings(location):
    """
    Returns list of logding options for a given location. The response includes hotels, guest houses, B&Bs and hostels.

    :param location: The location for which to return lodgings. E.g. "London"
    :return: Returns a list of lodgings
    """
    lodgings = []
    possible_amenities = ['Free WiFi', 'Parking', 'Breakfast', 'Pool', 'Gym']

    # Create 10 dummy lodgings for the given location
    for i in range(10):
        lodging_id = f'LODGE{i}'  # Create an ID like 'LODGE0', 'LODGE1', etc.
        lodging_name = 'Lodge-' + ''.join(random.choices(string.ascii_uppercase, k=5))
        lodging_price = round(random.uniform(50.0, 200.0), 2)
        lodging_rating = round(random.uniform(1.0, 5.0), 1)
        lodging_amenities = random.sample(possible_amenities, k=random.randint(1, len(possible_amenities)))

        # Add the lodging to the list
        lodgings.append({
            'id': lodging_id,
            'name': lodging_name,
            'location': location,
            'price': lodging_price,
            'rating': lodging_rating,
            'amenities': lodging_amenities
        })

    return lodgings


def get_lodging_by_id(lodging_id):
    """
    This function returns a specific lodging based on its id.

    :param lodging_id: The id of the lodging to return. E.g. "LODGE0"
    :return: Returns a dictionary representing a lodging or None if no such lodging exists
    """
    # Assume that all lodgings are in 'London' for this dummy data
    all_lodgings = get_all_lodgings('London')

    for lodging in all_lodgings:
        if lodging['id'] == lodging_id:
            return lodging  # Found the lodging

    # If we got here, no lodging with the given id was found
    return None


def filter_lodgings_by_price(lodgings, min_price, max_price):
    """
    This function filters the list of lodgings by price and returns lodgings in the given price range.

    :param lodgings: The list of lodgings to filter. Each lodging should be a dictionary with a 'price' key.
    :param min_price: The minimum price of the lodgings to return. E.g. 50.0
    :param max_price: The maximum price of the lodgings to return. E.g. 200.0
    :return: Returns a list of lodgings in the given price range
    """
    return [lodging for lodging in lodgings if min_price <= lodging['price'] <= max_price]


def filter_lodgings_by_rating(lodgings, min_rating):
    """
    This function filters the list of lodgings by rating and returns lodgings with a rating greater than or equal to the given rating.

    :param lodgings: The list of lodgings to filter. Each lodging should be a dictionary with a 'rating' key.
    :param min_rating: The minimum rating of the lodgings to return. E.g. 3.5
    :return: Returns a list of lodgings with a rating greater than or equal to the given rating
    """
    return [lodging for lodging in lodgings if lodging['rating'] >= min_rating]


def filter_lodgings_by_amenities(lodgings, amenities):
    """
    This function filters the list of lodgings by amenities and returns lodgings that offer all the given amenities.

    :param lodgings: The list of lodgings to filter. Each lodging should be a dictionary with an 'amenities' key, which is a list of strings.
    :param amenities: The list of amenities to filter by. E.g. ['Free WiFi', 'Parking']
    :return: Returns a list of lodgings that offer all the given amenities
    """
    return [lodging for lodging in lodgings if all(amenity in lodging.get('amenities', []) for amenity in amenities)]


def sort_lodgings_by_price(lodgings, ascending=True):
    """
    This function sorts the list of lodgings by price in ascending or descending order.

    :param lodgings: The list of lodgings to sort. Each lodging should be a dictionary with a 'price' key.
    :param ascending: Whether to sort in ascending order. Default is True.
    :return: Returns a list of lodgings sorted by price
    """
    return sorted(lodgings, key=lambda lodging: lodging['price'], reverse=not ascending)


def sort_lodgings_by_rating(lodgings, ascending=False):
    """
    This function sorts the list of lodgings by rating in ascending or descending order.

    :param lodgings: The list of lodgings to sort. Each lodging should be a dictionary with a 'rating' key.
    :param ascending: Whether to sort in ascending order. Default is False.
    :return: Returns a list of lodgings sorted by rating
    """
    return sorted(lodgings, key=lambda lodging: lodging['rating'], reverse=not ascending)


# A list of bookings. Each booking is a dictionary.
bookings = []


def book_lodging(lodging_id, user_id, start_date, end_date):
    """
    This function creates a booking for a specific lodging.

    :param lodging_id: The id of the lodging to book. E.g. "LODGE0"
    :param user_id: The id of the user making the booking. E.g. "USER123"
    :param start_date: The start date of the booking. E.g. "2023-07-01"
    :param end_date: The end date of the booking. E.g. "2023-07-07"
    :return: Returns a dictionary representing the new booking
    """
    global bookings
    # Create a unique booking id
    booking_id = f'BOOKING{len(bookings)}'
    new_booking = {
        'id': booking_id,
        'lodging_id': lodging_id,
        'user_id': user_id,
        'start_date': start_date,
        'end_date': end_date
    }
    bookings.append(new_booking)
    return new_booking


def cancel_booking(booking_id):
    """
    This function cancels a specific booking.

    :param booking_id: The id of the booking to cancel. E.g. "BOOKING0"
    :return: Returns a boolean indicating whether the cancellation was successful
    """
    global bookings
    for i, booking in enumerate(bookings):
        if booking['id'] == booking_id:
            del bookings[i]
            return True  # Cancelled successfully
    return False  # No booking with the given id was found


def get_user_bookings(user_id):
    """
    This function returns all bookings for a specific user.

    :param user_id: The id of the user to return bookings for. E.g. "USER123"
    :return: Returns a list of bookings for the given user
    """
    global bookings
    return [booking for booking in bookings if booking['user_id'] == user_id]
