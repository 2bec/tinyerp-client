class Contact:
    """
    Contact Resource
    """

    def __init__(self, client):
        self.client = client

    def search(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/contatos.pesquisa.php', data=payload
        )
        return self.client._handle_response(response)

    def get(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/contato.obter.php', data=payload
        )
        return self.client._handle_response(response)

    def create(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/contato.incluir.phpp', data=payload
        )
        return self.client._handle_response(response)

    def update(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/contato.alterar.php', data=payload
        )
        return self.client._handle_response(response)
