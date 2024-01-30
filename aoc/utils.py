import os
import urllib.request
from urllib.error import HTTPError, URLError

from dotenv import load_dotenv


def import_input(day: int) -> bytes:
    load_dotenv()
    session_cookie = "session=" + os.getenv('SESSION_COOKIE')
    url: str = "https://adventofcode.com/2023/day/3/input"
    headers: str = {'Cookie': session_cookie}
    request: urllib.request.Request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        return response.read()
