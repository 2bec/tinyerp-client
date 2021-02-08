class Note:
    """
    Note Resource
    """

    def __init__(self, client):
        self.client = client

    def search_note(self, *args, **kwargs):
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/notas.fiscais.pesquisa.php', data=payload
        )
        return self.client._handle_response(response)

    def get_note(self, note_id):
        payload = self.client._create_querystring({'id': note_id})
        response = requests.post(
            f'{self.client.host}/nota.fiscal.obter.php', data=payload
        )
        return self.client._handle_response(response)

    def create_note(self, note):
        payload = self.client._create_querystring({'nota': note})
        response = requests.post(
            f'{self.client.host}/nota.fiscal.incluir.php', data=payload
        )
        return self.client._handle_response(response)

    def create_note_consumer(self, note):
        payload = self.client._create_querystring({'nota': note})
        response = requests.post(
            f'{self.client.host}/nota.fiscal.consumidor.incluir.php', data=payload
        )
        return self.client._handle_response(response)

    def get_note_xml(self, note_id):
        payload = self.client._create_querystring({'id': note_id})
        response = requests.post(
            f'{self.client.host}/nota.fiscal.obter.xml.php', data=payload
        )
        return self.client._handle_response(response)

    def get_note_link(self, note_id):
        payload = self.client._create_querystring({'id': note_id})
        response = requests.post(
            f'{self.client.host}/nota.fiscal.obter.link.php', data=payload
        )
        return self.client._handle_response(response)

    def emit_note(self, note_id, *args, **kwargs):
        kwargs.update({'id': note_id})
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/nota.fiscal.emitir.php', data=payload
        )
        return self.client._handle_response(response)

    def update_tracking_code(self, nota_fiscal):
        kwargs.update({'notafiscal': nota_fiscal})
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/nota.fiscal.cadastrar.codigo.rastreamento.php', data=payload
        )
        return self.client._handle_response(response)

    def post_invoice_stock(self, note_id):
        kwargs.update({'id': note_id})
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/nota.fiscal.lancar.estoque.php', data=payload
        )
        return self.client._handle_response(response)

    def post_invoice_accounts(self, note_id):
        kwargs.update({'id': note_id})
        payload = self.client._create_querystring(args, kwargs)
        response = requests.post(
            f'{self.client.host}/nota.fiscal.lancar.estoque.php', data=payload
        )
        return self.client._handle_response(response)
