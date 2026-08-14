# pipeline de dados ?
 o que é. 
 como funciona

# validação em codigo

# Atividade pratica

# Fontes Heterogeneas em sistemas inteligentes

#

pegar as APIs

criar uma validação  de Dados antes de entrar no PIPELINE.

para verificar os dados.

APIs > VERIFICAÇÂO > PIPELINE > RESPOSTA (sim ou não)

VERIFICAÇÂO = contrato de dados

# estruturação 

os dados vem de varias APIs  com varios tipos de dados diferentes. (JSON, CSV, XML, ETC)
criar uma validação(contrato de dados)
onde vamos definir um padrão de como os dados devem ser tratados e enviado para o *pipeline*
# EX:
{
  "accountId": "conta-cliente-123",
  "description": "Pagamento de Serviço",
  "calendar": {
    "dueDate": "2026-08-20",
    "daysAfterDueDate": 5
  },
  "payer": {
    "cpfCnpj": "12.345.678/0001-90",
    "name": "Nome do Pagador"
  },
  "value": {
    "original": 150.00,
    "fine": {},
    "interest": {},
    "discount": {}
  }
}   

qual quer coisa fora disso teria que transformar e reformular para esse modelo de JSON.

e assim podemos enviar para o PIPELINE.

onde teremos a resposta se é ou Não fraude.


# Principio da reprodutibilidade


