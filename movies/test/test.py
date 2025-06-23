import requests
import os

APP_URL = os.getenv("APP_URL") or "http://localhost:80"


def get_movies() -> dict:
    try:
        res = requests.get(APP_URL + "/movie")
        if 200 <= res.status_code < 400:
            return res.json()
        else:
            raise RuntimeError("No movies found")
    except (requests.ConnectionError, RuntimeError) as e:
        print(e)
        return {}


def add_movie(movie: dict) -> None:
    try:
        res = requests.post(APP_URL + "/movie", json=movie)
        if 200 <= res.status_code < 400:
            return
        else:
            raise RuntimeError("POST request failed")
    except (requests.ConnectionError, RuntimeError) as e:
        print(e)


def check_movie_addition() -> bool:
    movie = {"name": 'The Princess Bride', 'length': 98, 'genre': 'comedy'}
    try:
        add_movie(movie=movie)
        for key, value in get_movies().items():
            if key == 'name':
                if value == "The Princess Bride":
                    return True
        return False
    except (requests.ConnectionError, RuntimeError) as e:
        print(e)
        return False


if __name__ == '__main__':
    assert check_movie_addition()
