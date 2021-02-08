import requests

from urllib.parse import urlencode

from resources.products import Product
from resources.contacts import Contact
from resources.notes import Note


class TinyErpClient:
    """
    TinyErp client to consume REST API

    You need a token from TinyErp Token API extensions.
    https://tiny.com.br/ajuda/api/api2-gerar-token-api

    Use:

    client = TinyErpClient($TINYERP_TOKEN))
    """

    host = 'https://api.tiny.com.br/'

    def __init__(self, token, version='api2', format='json'):
        self.token = token
        self.version = version
        self.format = format

    def _handle_response(self, response):
        response.raise_for_status()

        try:
            json_response = response.json()
        except ValueError:
            json_response = None

        return json_response

    def _querystring_token(self):
        return '&'.join([f'token={self.token}'])

    def _querystring_format(self):
        return '&'.join([f'format={self.format}'])

    def _create_querystring(self, *args, **kwargs):
        querystring = '&'.join([
            self._querystring_token(),
            self._querystring_format(),
            urlencode(args),
            urlencode(kwargs),
        ])
        return querystring

    @property
    def product(self):
        return Product(self)

    @property
    def note(self):
        return Note(self)

    @property
    def contact(self):
        return Contact(self)
