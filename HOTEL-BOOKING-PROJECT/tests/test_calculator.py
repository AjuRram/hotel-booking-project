import pytest
from src.calculator import calculate_price
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config.exchange_rates import EXCHANGE_RATES



@pytest.fixture
def sample_hotel_data():
    return {
        "hotelCodeSupplier": "39971881",
        "market": "US",
        "price": {
            "net": 100.0,  # Base price
            "currency": "EUR",  # Original currency
        },
        "markup": 5.0,  # 5% markup
        "request_currency": "USD"  # Requested currency
    }

def test_calculate_price_no_conversion(sample_hotel_data):
    """ Test price calculation when the request currency is the same as price currency """
    sample_hotel_data["request_currency"] = "EUR"  # No conversion needed
    result = calculate_price(sample_hotel_data)
    
    assert result["price"]["selling_price"] == pytest.approx(105.0, 0.01)  # 5% markup applied
    assert result["price"]["exchange_rate"] == 1.0  # No exchange rate applied

def test_calculate_price_with_conversion(sample_hotel_data):
    """ Test price calculation with currency conversion from EUR to USD """
    sample_hotel_data["request_currency"] = "USD"
    result = calculate_price(sample_hotel_data)
    
    expected_exchange_rate = EXCHANGE_RATES["EUR"]["USD"]
    expected_selling_price = 100.0 * expected_exchange_rate * 1.05  # Net price * exchange rate * markup

    assert result["price"]["selling_price"] == pytest.approx(expected_selling_price, 0.01)
    assert result["price"]["selling_currency"] == "USD"
    assert result["price"]["exchange_rate"] == expected_exchange_rate

def test_calculate_price_invalid_currency(sample_hotel_data):
    """ Test handling of an invalid currency """
    sample_hotel_data["request_currency"] = "INR"  # Unsupported currency
    
    with pytest.raises(ValueError, match="Unsupported currency: INR"):
        calculate_price(sample_hotel_data)

def test_calculate_price_zero_net(sample_hotel_data):
    """ Test calculation when net price is zero """
    sample_hotel_data["price"]["net"] = 0.0
    result = calculate_price(sample_hotel_data)
    
    assert result["price"]["selling_price"] == 0.0  # Selling price should remain zero
    assert result["price"]["exchange_rate"] == 1.0  # No exchange needed

def test_calculate_price_negative_net(sample_hotel_data):
    """ Test behavior when net price is negative """
    sample_hotel_data["price"]["net"] = -50.0
    
    with pytest.raises(ValueError, match="Net price cannot be negative"):
        calculate_price(sample_hotel_data)
