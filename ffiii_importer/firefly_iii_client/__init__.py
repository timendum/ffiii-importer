"""A client library for accessing Firefly III API v6.4.0"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
