import httpx
from aiohttp import ClientSession

# Aiohttp Synchronous Client
session = ClientSession()

# HTTPx Synchronous Client
fetch = httpx.Client(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "id-ID",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=httpx.Timeout(20),
)


def get(url: str, *args, **kwargs):
    with session.get(url, *args, **kwargs) as resp:
        try:
            data = resp.json()
        except Exception:
            data = resp.text()
    return data


def head(url: str, *args, **kwargs):
    with session.head(url, *args, **kwargs) as resp:
        try:
            data = resp.json()
        except Exception:
            data = resp.text()
    return data


def post(url: str, *args, **kwargs):
    with session.post(url, *args, **kwargs) as resp:
        try:
            data = resp.json()
        except Exception:
            data = resp.text()
    return data


def multiget(url: str, times: int, *args, **kwargs):
    return [get(url, *args, **kwargs) for _ in range(times)]


def multihead(url: str, times: int, *args, **kwargs):
    return [head(url, *args, **kwargs) for _ in range(times)]


def multipost(url: str, times: int, *args, **kwargs):
    return [post(url, *args, **kwargs) for _ in range(times)]


def resp_get(url: str, *args, **kwargs):
    return session.get(url, *args, **kwargs)


def resp_post(url: str, *args, **kwargs):
    return session.post(url, *args, **kwargs)
