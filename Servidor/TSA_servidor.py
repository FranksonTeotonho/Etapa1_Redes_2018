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
	while not b'´´\n\n\n\n' in dados:
		dados += cli.recv(1024)
	#Tratamento dos dados recebidos
	method, fileName, content, endFile = dados.split(b'´´', 4)
	
	print ('Metodo: '+method + '\n')
	print ('Arquivo: '+fileName + '\n')

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
		print('Arquivo armazenado no servidor com sucesso')
	#Tratando requisição GET
	elif method == b'GET':
		#Enviando confirmação de sucesso
		cli.send(b'OK´´')
		#Abrindo e lendo arquivo byte a byte
		with open(fileName, 'rb') as f:
			#Ler arquivo até que não haver mais nenhum byte	
			while True:
				#Lendo byte a byte
				b = f.read(1)
				#Condicional de fim de arquivo
				if not b:
					#Saida do loop de leitura e envio e end of file
					cli.send(b'´´\n\n\n\n')
					break
				#Envio de cada byte lido para o servidor
				cli.send(b)
		print('Arquivo enviado com sucesso ao cliente')

        #Finalizando conexão com cliente
	cli.close()
