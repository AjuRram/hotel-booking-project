from src.config.exchange_rates import EXCHANGE_RATES
def calculate_price(net_price: float,markup: float,from_currency: str,to_currency: str)-> dict:
        exchnage_rate = EXCHANGE_RATES.get(from_currency,{}).get(to_currency,1)
        selling_price=net_price*(1+markup/100)*exchnage_rate
        return{
                "net":net_price,
                "selling_price": round(selling_price, 2),
                "markup":markup,
                "exchange_rate":exchnage_rate,
                "selling_currency":to_currency
        }

    