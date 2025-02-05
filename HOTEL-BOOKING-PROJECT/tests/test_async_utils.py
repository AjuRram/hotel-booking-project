import pytest
import asyncio
from async_utils import get_exchange_rate, var_ocg



@pytest.mark.asyncio
async def test_get_exchange_rate():
   
    assert var_ocg == "processing"  
    rate = await get_exchange_rate("USD", "EUR")
    assert rate == 0.93  

@pytest.mark.asyncio
async def test_get_exchange_rate_fallback():
    
    rate = await get_exchange_rate("XYZ", "USD")  
    assert rate == 1.0 

