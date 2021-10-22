from functools import lru_cache
from typing import Any, cast

import requests

SWAPI_URL = "https://swapi.dev/api"


# @lru_cache
def get_person_data(person_id: int) -> dict[str, Any]:
    result = requests.get(f"{SWAPI_URL}/people/{person_id}")
    return cast(dict[str, Any], result.json())


@lru_cache
def get_planet_data(planet_id: int) -> dict[str, Any]:
    result = requests.get(f"{SWAPI_URL}/planets/{planet_id}")
    return cast(dict[str, Any], result.json())
