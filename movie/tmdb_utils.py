import requests
from django.conf import settings
from urllib.parse import urljoin


def get_movie_by_id(id: int):
    

    r = requests.get(
        urljoin(settings.TMDB_URL, f"3/movie/{id}"),
        params={"api_key": settings.TMDB_API_KEY},
    )
    print(r.request.url)
    return r.json()