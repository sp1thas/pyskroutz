from .client.base import SkroutzClient


def client(client_id=None, client_secret=None) -> SkroutzClient:
    return SkroutzClient(client_id=client_id, client_secret=client_secret)
