from dataclasses import dataclass

@dataclass(frozen=True)
class Job:
    id: str
    company: str
    title: str
    location: str
    url: str
    posted: str = ""
    description: str = ""
