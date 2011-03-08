import datetime
from decimal import Decimal

from fixture_generator import fixture_generator

from .models import Hotel

@fixture_generator(Hotel)
def create_hotels():
    Hotel.objects.create(
        name = 'Ibis Hotel Amsterdam Centre',
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
