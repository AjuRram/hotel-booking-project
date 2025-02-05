from datetime import datetime, timedelta

from src.models import RequestData

VALID_LANGUAGES = {'en', 'fr', 'de', 'es'}
VALID_CURRENCIES = {'EUR', 'USD', 'GBP'}
VALID_NATIONALITIES = {'US', 'GB', 'CA'}
DEFAULT_MARKETS = {'ES'}

def validate_request(data: RequestData):
    if data.languageCode not in VALID_LANGUAGES:
        raise ValueError("Invalid language code")

    start_date = datetime.strptime(data.StartDate, "%d/%m/%Y")
    end_date = datetime.strptime(data.EndDate, "%d/%m/%Y")

    if start_date < datetime.today() + timedelta(days=2):
        raise ValueError("StartDate must be at least 2 days from today")
    
    if (end_date - start_date).days < 3:
        raise ValueError("Stay duration must be at least 3 nights")

    if data.Currency not in VALID_CURRENCIES:
        data.Currency = "EUR"

    if data.Nationality not in VALID_NATIONALITIES:
        data.Nationality = "US"

    return True
