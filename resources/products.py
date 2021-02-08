class Product:
    """
    Product Resource
    """

    def __init__(self, client):
        self.client = client

    def search(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produtos.pesquisa.php', data=payload
        )
        return self.client._handle_response(response)

    def get(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.obter.php', data=payload
        )
        return self.client._handle_response(response)

    def create(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.incluir.php', data=payload
        )
        return self.client._handle_response(response)

    def update(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.alterar.php', data=payload
        )
        return self.client._handle_response(response)

    def stock(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.obter.estoque.php', data=payload
        )
        return self.client._handle_response(response)

    def structure(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.obter.estrutura.php', data=payload
        )
        return self.client._handle_response(response)

    def tags(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.obter.tags', data=payload
        )
        return self.client._handle_response(response)

    def updates_list(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/lista.atualizacoes.produtos', data=payload
        )
        return self.client._handle_response(response)

    def stock_updates_list(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/lista.atualizacoes.estoque', data=payload
        )
        return self.client._handle_response(response)

    def update_stock(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/produto.atualizar.estoque.php', data=payload
        )
        return self.client._handle_response(response)

    def get_categories(self):
        payload = self.client._create_querystring()
        response = requests.post(
            f'{self.host}/produtos.categorias.arvore.php', data=payload
        )
        return self.client._handle_response(response)
