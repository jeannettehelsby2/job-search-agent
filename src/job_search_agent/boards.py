from abc import ABC,  abstractmethod
from .models import Job
import json
import urllib.request

class JobBoard(ABC):
    def __init__(self, company: str, slug: str):
        self.company = company
        self.slug = slug

           
    def _get_json(self, url: str):
        with urllib.request.urlopen(url, timeout=20) as response:
            return json.loads(response.read())

    def fecth (self) -> list [Job]:
        """Download jobs and return them as Job objects."""

class GreenhouseBoard(JobBoard):
    def fetch (self) -> list[Job]:

        url = f"https://boards-api.greenhouse.io/v1/boards/{self.slug}/jobs"
        #data = json.loads(urllib.request.urlopen(url).read())
        data = self._get_json(url)
        jobs = []
        for item in data["jobs"]:
            job = Job(
                id=f"greenhouse-{self.slug}-{item['id']}",
                company=self.company,
                title=item["title"],
                location=item["location"]["name"],
                url=item["absolute_url"],
                posted=item.get("updated_at", "")[:10], )         
            jobs.append(job)
        return jobs