import pytest
from validator import validate_request

def test_valid_request():
    request_data = {
        "timeoutMilliseconds": 25000,
        "source": {"languageCode": "en"},
        "optionsQuota": 20,
        "Configuration": {"Parameters": {"password": "test", "username": "user", "CompanyID": 123456}},
        "SearchType": "Multiple",
        "StartDate": "14/10/2024",
        "EndDate": "18/10/2024",
        "Currency": "USD",
        "Nationality": "US"
    }
    
    validated_data = validate_request(request_data)
    assert validated_data.Currency == "USD"
    assert validated_data.Nationality == "US"

def test_invalid_currency():
    request_data = {"Currency": "INR"}
    validated_data = validate_request(request_data)
    assert validated_data.Currency == "EUR"
