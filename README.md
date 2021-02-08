# tinyerp-client

# Resources

- [ ] Account
- [x] Clients and Providers (Contacts)
- [x] Products
- [ ] Orders
- [ ] PDV
- [x] NF
- [ ] Tags group
- [ ] Prices lists
- [ ] Expeditions
- [ ] Sellers
- [ ] CRM
- [ ] NFS
- [ ] Expenses
- [ ] Recipes
- [ ] Webhooks
- [ ] Contracts
- [ ] Linked Tables

# Suggestions for TinyErp to improve its REST API

1. usar cache, se ainda não utilizam. (ainda não fiz requests)
1. padronização dos endpoints
   1. melhorar a camada de diretórios para: `/api/v2`. Assim englobamos todas as versões dentro de um módulo `api`. Podemos padronizar os nomes das versões, exemplo: deve começar com a letra `v` de versão e incluir somente o número `major` (major.patch.minor)
   1. utilizar o nome do serviço (ou recurso) no plural e em inglês `/product`, `/order`, `contacts`, etc.
   1. não utilizar extensão na url, ao invés de `https://api.tiny.com.br/api2/produtos.pesquisa.php` utilizar `https://api.tiny.com.br/api/v2/produtos/search`.
   1. utilizar os métodos HTTP corretos para cada ação, por exemplo: `GET` para buscar informação, `POST` para enviar informação, `PUT` para realizar alterações completas, `PATCH` para alterações parciais e `DELETE` para deletar.
1. criar OpenAPI Documentation (antigo swagger)
1. utilizar authorization HEADER
1. utilizar JSON como padrão (post/get)
