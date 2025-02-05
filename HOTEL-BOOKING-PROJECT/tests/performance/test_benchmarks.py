import pytest
from src.parser import XMLParser
from time import time

def measure_performance(func, *args):
    start = time()
    func(*args)
    return time() - start

def test_xml_parsing_performance():
    xml_parser = XMLParser()
    sample_xml = "<AvailRQ><Configuration><Parameters password='xxx' username='yyy' CompanyID='123'/></Configuration></AvailRQ>"
    assert measure_performance(xml_parser.parse_request, sample_xml) < 0.1