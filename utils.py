from datetime import date
from typing import NamedTuple


class Experience(NamedTuple):
    job_title: str
    company: str
    summary: str
    start_date: date
    end_date: date = None


class Qualification(NamedTuple):
    name: str
    issuing_org: str
    issue_date: date
    expiration_date: date
