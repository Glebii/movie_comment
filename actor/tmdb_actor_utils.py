import requests
from django.conf import settings
from urllib.parse import urljoin


def get_actor_by_id(id: int):
    

    r = requests.get(
        urljoin(settings.TMDB_URL, f"/person/{id}"),
        params={"api_key": settings.TMDB_API_KEY,"language":"ru-RU"},
    )
    print(r.request.url)
    return r.json()