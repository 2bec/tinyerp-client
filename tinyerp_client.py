import requests

from urllib.parse import urlencode


class TinyErpClient:
    """
    TinyErp client to consume REST PI

    You need a token from TinyErp Token API extensions.
    https://tiny.com.br/ajuda/api/api2-gerar-token-api

    Use:

    client = TinyErpClient($TINYERP_TOKEN)
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

    """
    START PRODUTOS REST API
    """

    def search_product(self, product):
        payload = self._create_querystring({'product': product})
        response = requests.post(
            f'{self.host}/produtos.pesquisa.php', data=payload
        )
        return self._handle_response(response)

    def get_product(self, product_id):
        payload = self._create_querystring({'id': product_id})
        response = requests.post(
            f'{self.host}/produto.obter.php', data=payload
        )
        return self._handle_response(response)

    def create_product(self, product):
        payload = self._create_querystring({'product': product})
        response = requests.post(
            f'{self.host}/produto.incluir.php', data=payload
        )
        return self._handle_response(response)

    def update_product(self, product):
        payload = self._create_querystring({'product': product})
        response = requests.post(
            f'{self.host}/produto.alterar.php', data=payload
        )
        return self._handle_response(response)

    def stock_product(self, product_id):
        payload = self._create_querystring({'id': product_id})
        response = requests.post(
            f'{self.host}/produto.obter.estoque.php', data=payload
        )
        return self._handle_response(response)

    def struct_product(self, product_id):
        payload = self._create_querystring({'id': product_id})
        response = requests.post(
            f'{self.host}/produto.obter.estrutura.php', data=payload
        )
        return self._handle_response(response)

    def get_product_tags(self, product_id):
        payload = self._create_querystring({'id': product_id})
        response = requests.post(
            f'{self.host}/produto.obter.tags', data=payload
        )
        return self._handle_response(response)

    def get_product_updates_list(self, date, page=1):
        payload = self._create_querystring(
            {'dataAlteracao': date, 'pagina': page}
        )
        response = requests.post(
            f'{self.host}/lista.atualizacoes.produtos', data=payload
        )
        return self._handle_response(response)

    def get_stock_product_updates_list(self, date, page=1):
        payload = self._create_querystring(
            {'dataAlteracao': date, 'pagina': page}
        )
        response = requests.post(
            f'{self.host}/lista.atualizacoes.estoque', data=payload
        )
        return self._handle_response(response)

    def update_stock_product(self, stock):
        payload = self._create_querystring({'estoque': stock})
        response = requests.post(
            f'{self.host}/produto.atualizar.estoque.php', data=payload
        )
        return self._handle_response(response)

    def get_categories_product(self):
        payload = self._create_querystring()
        response = requests.post(
            f'{self.host}/produtos.categorias.arvore.php', data=payload
        )
        return self._handle_response(response)

    """
    END PRODUTOS REST API
    """

    """
    START CONTACTS REST API
    """

    def search_contact(self, *args, **kwargs):
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/contatos.pesquisa.php', data=payload
        )
        return self._handle_response(response)

    def get_contact(self, contact_id):
        payload = self._create_querystring({'id': contact_id})
        response = requests.post(
            f'{self.host}/contato.obter.php', data=payload
        )
        return self._handle_response(response)

    def create_contact(self, contact):
        payload = self._create_querystring({'contact': contact})
        response = requests.post(
            f'{self.host}/contato.incluir.phpp', data=payload
        )
        return self._handle_response(response)

    def update_contact(self, contact):
        payload = self._create_querystring({'contact': contact})
        response = requests.post(
            f'{self.host}/contato.alterar.php', data=payload
        )
        return self._handle_response(response)
    """
    END CONTACTS REST API
    """

    """
    START NOTAS FISCAIS REST API
    """

    def search_nf(self, *args, **kwargs):
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/notas.fiscais.pesquisa.php', data=payload
        )
        return self._handle_response(response)

    def get_nf(self, nf_id):
        payload = self._create_querystring({'id': nf_id})
        response = requests.post(
            f'{self.host}/nota.fiscal.obter.php', data=payload
        )
        return self._handle_response(response)

    def create_nf(self, nf):
        payload = self._create_querystring({'nota': nf})
        response = requests.post(
            f'{self.host}/nota.fiscal.incluir.php', data=payload
        )
        return self._handle_response(response)

    def create_nf_consumer(self, nf):
        payload = self._create_querystring({'nota': nf})
        response = requests.post(
            f'{self.host}/nota.fiscal.consumidor.incluir.php', data=payload
        )
        return self._handle_response(response)

    def get_nf_xml(self, nf_id):
        payload = self._create_querystring({'id': nf_id})
        response = requests.post(
            f'{self.host}/nota.fiscal.obter.xml.php', data=payload
        )
        return self._handle_response(response)

    def get_nf_link(self, nf_id):
        payload = self._create_querystring({'id': nf_id})
        response = requests.post(
            f'{self.host}/nota.fiscal.obter.link.php', data=payload
        )
        return self._handle_response(response)

    def emit_nf(self, nf_id, *args, **kwargs):
        kwargs.update({'id': nf_id})
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/nota.fiscal.emitir.php', data=payload
        )
        return self._handle_response(response)

    def update_tracking_code(self, nota_fiscal):
        kwargs.update({'notafiscal': nota_fiscal})
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/nota.fiscal.cadastrar.codigo.rastreamento.php', data=payload
        )
        return self._handle_response(response)

    def post_invoice_stock(self, nf_id):
        kwargs.update({'id': nf_id})
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/nota.fiscal.lancar.estoque.php', data=payload
        )
        return self._handle_response(response)

    def post_invoice_accounts(self, nf_id):
        kwargs.update({'id': nf_id})
        payload = self._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.host}/nota.fiscal.lancar.estoque.php', data=payload
        )
        return self._handle_response(response)
    """
    END NOTAS FISCAIS REST API
    """
