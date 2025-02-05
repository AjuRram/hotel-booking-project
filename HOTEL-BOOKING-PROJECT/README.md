*Overeview*
____________

The Hotel Booking XML-to-JSON Processor is a Python-based application designed to convert an XML request into a structured JSON response, adhering to various business and validation rules. The solution efficiently handles currency conversion, price calculations, and validation, while maintaining high performance and security standards. This project is designed for senior-level software engineers and focuses on aspects like asynchronous programming, performance optimization, security best practices, and proper testing.

*Features*
___________

1)XML-to-JSON Conversion: Parse and transform XML requests into JSON responses.
2)Currency Conversion: Supports multiple currencies with fallback to external APIs.
3)Price Calculation: Apply dynamic price calculation logic using markup percentages.
4)Business Rules Validation: Enforces validation rules for room bookings, dates, and passenger information.
5)Security: Implements encryption, password hashing, and logging for sensitive data.
6)Asynchronous Processing: Uses asyncio for handling external API calls and currency conversions.
7)Performance Optimization: Caching, connection pooling, and other techniques for high-speed performance.

*Table of contents*
___________________

Installation
Usage
Testing
Performance Benchmarks
Security
Changelog
License
Installation
Prerequisites
Python 3.9+: Ensure that Python is installed on your system.
Virtual Environment (Recommended): Use a virtual environment to manage dependencies.

*STEPS TO INSTALL*
_____________________

*Clone the repository:*
bash
Copy
Edit
git clone https://github.com/yourusername/hotel-booking-xml-json.git
cd hotel-booking-xml-json

*Create and activate a virtual environment:*
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For macOS/Linux

*Install the required dependencies:*
bash
Copy
Edit
pip install -r requirements.txt

Usage
Running the Application
To run the processor with an XML request, use the provided function:

python
Copy
Edit
from src.parser import parse_xml_request
from src.generator import generate_json_response

xml_data = "<AvailRQ>...</AvailRQ>"  # Replace with actual XML data
json_response = generate_json_response(parse_xml_request(xml_data))
print(json_response)
API Endpoint
If you want to use the processor as an API, you can set up a server with FastAPI  /

*process_request:*
python
Copy
Edit
from fastapi import FastAPI
from src.parser import parse_xml_request
from src.generator import generate_json_response

app = FastAPI()

@app.post("/process_request")
async def process_request(xml_data: str):
    parsed_data = parse_xml_request(xml_data)
    json_response = generate_json_response(parsed_data)
    return json_response

*To run the server*
bash
Copy
Edit
uvicorn main:app --reload

*Testing*
Running Tests

*This project uses pytest for unit testing. To run tests, activate the virtual environment and execute the following command:*
bash
Copy
Edit
pytest tests/

*You can also specify individual test files:*
bash
Copy
Edit
pytest tests/test_calculator.py

*Code Coverage*
___________________
Ensure you have at least 85% test coverage for the project. You can generate the coverage report with the following:

bash
Copy
Edit
pytest --cov=src tests/

*Performance Tests*
_____________________
Performance tests ensure that the processing time meets the specified benchmarks. To run the performance tests:

bash
Copy
Edit
pytest tests/performance/test_benchmarks.py
Performance Benchmarks

XML Parsing:
Goal: < 100ms for sample request
Test: Ensures efficient XML parsing.
Price Calculation:
Goal: < 50ms per hotel
Test: Validates price calculations.
Total Response Time:
Goal: < 200ms total
Test: Validates the entire processing flow.
Security

*Key Features*
_______________
1)Password Hashing: Passwords are hashed using PBKDF2 with SHA256.
2)Data Encryption: Sensitive data is encrypted using the Fernet symmetric encryption algorithm.
3)Security Logging: Logs security events like password changes or data encryption.
4)Exchange Rate Security: Caching and fallback mechanisms ensure secure handling of exchange rates.

*How Security Is Implemented*
_____________________________
1)Encryption: Sensitive data is encrypted using the cryptography package.
2)Hashing: Passwords are hashed using PBKDF2 with salt for added security.
3)Logging: Any significant security event is logged to ensure accountability.

*PERFORMANCE BENCHMARKS*

Name                            Stmts   Miss  Cover
---------------------------------------------------
src\__init__.py                     0      0   100%
src\async_utils.py                 12     12     0%
src\calculator.py                   5      4    20%
src\config\exchange_rates.py        1      1     0%
src\config\security_config.py       0      0   100%
src\models.py                      15     15     0%
src\parser.py                      17     12    29%
src\security.py                    14      4    71%
src\validator.py                   20     20     0%
---------------------------------------------------
TOTAL                              84     68    19%