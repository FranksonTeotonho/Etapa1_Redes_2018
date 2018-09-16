#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket, select

#Construindo sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8000))
s.listen(1)
#Loop servidor
while True:
	#Aceitando socket do cliente
	cli, addr = s.accept()      
	#Inicializando variavel dados  
	dados = b''
	#recebendo dados até convensão de final de arquivo
	while not b'\n\n\n\n' in dados:
		dados += cli.recv(1000000)
	
	#Tratamento dos dados recebidos
	method, fileName, content = dados.split(b'&', 3)

	#Tratando requisição PUT
	if method == b'PUT':
		#Criação de um novo arquivo
		f = open(fileName, 'wb')
		#Escrita do conteudo no arquivo
		for i in content:
			f.write(i)
		#Fechando arquivo
		f.close()
		#Resposta de sucesso ao servidor
                cli.send(b'OK')
        #Finalizando conexão com cliente
	cli.close()
