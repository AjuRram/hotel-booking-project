from typing import List, Optional
from pydantic import BaseModel

class Parameter(BaseModel):
    password: str
    username: str
    CompanyID: int

class RequestData(BaseModel):
    languageCode: str
    optionsQuota: Optional[int] = 20
    parameters: Parameter
    SearchType: str
    StartDate: str
    EndDate: str
    Currency: str = "EUR"
    Nationality: str = "US"