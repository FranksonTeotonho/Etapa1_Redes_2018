#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket

#Criação do socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Conexão com servidor local
s.connect(('127.0.0.1', 8000))

#inicialização dos dados a serem recebidos
dados = b''
#Definição do arquivo a ser recuperado do servidor
fileName = b'teste_cliente.txt'
#Envio do header, content inserido apenas para manter o padrão
s.send(b'GET&'+fileName+b'&content&\n\n\n\n')

#Recebimento dos dados até convensão de final de arquivo
while not b'\n\n\n\n' in dados:
	dados += s.recv(1024)

#Tratamento dos dados recebidos
res, content, endFile = dados.split(b'&', 3)

#Em caso de sucesso, gravar dados recebidos em um novo arquivo
if(res == b'OK'):
	#Criação de um novo arquivo, referente ao fileName requerido
	#Criação de um novo arquivo
	f = open(fileName, 'wb')
	#Escrita do conteudo do arquivo
	for i in content:
		f.write(i)
	#Fechando arquivo
	f.close()
	print('Arquivo recebido com sucesso')

#Em caso de falaha, notificar ao usuario
elif(res == b'FAIL'):
	print("Arquivo não encontrado")

#Finalizar conexão
s.close()
