		Transferência simples de arquivos (TSA)

Desenvolvido na linguagem Python (versão 2.7.15rc1)

1 Servidor que recebe requisição PUT e GET
2 Clientes, 1 realizando requisição PUT e 1 realizando requisição GET

Dentro dos scripts dos clientes pode-se especificar um filename no qual se deseja
a adição de arquivos ao servidor ou a recuperação de arquivos a partir do servidor.

Para executar:
-Para requisição PUT
	Na pasta do servidor execute o comando 'python TSA_servidor.py'
	Na paste do cliente execute o comando 'python TSA_cliente_put.py'
-Para requisição GET
	Na pasta do servidor execute o comando 'python TSA_servidor.py'
	Na paste do cliente execute o comando 'python TSA_cliente_get.py'

Observações: Há diversos arquivos de teste, com diversas extensões. Especifique o fileName dentro do script 'TSA_cliente_put.py' ou 'TSA_cliente_get.py'
