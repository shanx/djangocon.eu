import datetime
from decimal import Decimal

from fixture_generator import fixture_generator

from .models import Hotel

@fixture_generator(Hotel)
def hotel():
    Hotel.objects.create(
        name = 'Ibis Hotel Amsterdam Centre',
        description = """Ibis Amsterdam Centre is situated next to the main
train station. Trains, metros, buses, trams and taxis all drop you right to the door. Schiphol airport is just 15 minutes away by train, the RAI center just 20 minutes by tram and the ArenA 15 minutes by metro. Other destinations such as the Beurs van Berlage, the Dam Square and the Grachtengordel are within walking distance. Breakfast is served daily from 4am to at least midday.""",
        nr_of_stars = 3,
        address = 'Stationsplein 49',
        postal_code = '1012 AB',
        place = 'Amsterdam',
        rate_single = Decimal('125.0'),
        rate_double = Decimal('140.0'),
        city_tax = Decimal('5.0'),
        breakfast = 'included in room rate',
        wifi = 'EUR 3,95 per connection per day (a maximum download speed of 458,5KB)',
        cancellation_policy = 'cancellation of the reservation is free of charge until 1 week prior to the date of arrival',
        date_available = datetime.date(2011, 4, 1)
    )

    Hotel.objects.create(
        name = 'M Gallery The Convent Hotel Amsterdam',
        description = """MGallery The Convent Hotel Amsterdam is a 4-star hotel with a unique history that makes it the perfect place to stay. Its location in the center of Amsterdam is ideal for visiting the city. It is a five-minute walk from Centraal Station, Dam Square and the Royal Palace. The hotel building previously housed 2 monasteries from the 13th & 14th centuries, plus a printing house.""",
        nr_of_stars = 4,
        address = 'Nieuwezijds Voorburgwal 67',
        postal_code = '1012 RE',
        place = 'Amsterdam',
        rate_single = Decimal('159.0'),
        rate_double = Decimal('179.0'),
        city_tax = Decimal('5.0'),
        breakfast = 'included in room rate',
        wifi = 'included in room rate (a maximum download speed of 2MB)',
        cancellation_policy = 'cancellation of the reservation is free of charge until 48 hours prior to the date of arrival',
        date_available = datetime.date(2011, 4, 1)
    )

    Hotel.objects.create(
        name = 'Park Plaza Victoria Hotel Amsterdam',
        description = """One of the top central Amsterdam hotels, the four-star deluxe Park Plaza Victoria Amsterdam is located in the heart of the city centre near shopping and business districts, opposite Central Station and just 15 minutes by train from Amsterdam Schiphol Airport. Housed in a historic building, Park Plaza Victoria Amsterdam offers 306 well-appointed guest rooms equipped with the modern decor and superior features expected of one of the finest hotels in Amsterdam. Hotel amenities include a Business Centre, Fitness Centre, free Wi-Fi in public spaces and a pool.""",
        nr_of_stars = 4,
        address = 'Damrak 1-5',
        postal_code = '1012 LG',
        place = 'Amsterdam',
        rate_single = Decimal('165.0'),
        rate_double = Decimal('165.0'),
        city_tax = Decimal('5.0'),
        breakfast = 'EUR 18 per person per day',
        wifi = 'included in room rate (a maximum download speed of 400KB)',
        cancellation_policy = 'cancellation of the reservation is free of charge until 1 week prior to the date of arrival',
        date_available = datetime.date(2011, 4, 1)
    )
