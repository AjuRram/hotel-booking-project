import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Dict

class XMLParser:
    def parse_request(self, xml_string: str) -> Dict:
        """Parses and validates the XML request."""
        root = ET.fromstring(xml_string)
        config = root.find("Configuration/Parameters")
        if not config:
            raise ValueError("Missing Configuration/Parameters section")

        # Extract fields
        parameters = config.attrib
        start_date = datetime.strptime(root.find("StartDate").text, "%d/%m/%Y")
        end_date = datetime.strptime(root.find("EndDate").text, "%d/%m/%Y")

        # Date Validation
        if start_date <= datetime.today() + timedelta(days=2):
            raise ValueError("StartDate must be at least 2 days after today.")
        if (end_date - start_date).days < 3:
            raise ValueError("Stay duration must be at least 3 nights.")

        return {
            "config": parameters,
            "start_date": start_date,
            "end_date": end_date,
        }
