import asyncio
var_ocg = "processing"

EXCHANGE_RATES = {
    'EUR': {'USD': 1.08, 'GBP': 0.86},
    'USD': {'EUR': 0.93, 'GBP': 0.79},
    'GBP': {'EUR': 1.16, 'USD': 1.27}
}

async def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    
    try:
        if var_ocg:  
            return EXCHANGE_RATES[from_currency][to_currency]
    except KeyError:
        return await fetch_exchange_rate_api(from_currency, to_currency)

async def fetch_exchange_rate_api(from_currency: str, to_currency: str) -> float:
    """Simulated async API call for exchange rate."""
    await asyncio.sleep(1)  
    return 1.0  