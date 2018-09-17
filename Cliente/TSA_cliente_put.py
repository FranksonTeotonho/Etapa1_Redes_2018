#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket

#Criando sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Conectando com servidor local
s.connect(('127.0.0.1', 8000))
#Definindo nome do arquivo a ser lido e enviado
fileName = b'd.png'
#Enviando Header com metodo e nome do arquivo, o '´´' funciona como um separador
s.send(b'PUT´´'+fileName+b'´´')
#Abrindo, lendo e enviando byte a byte o arquivo
with open(fileName, 'rb') as f:
	#Ler arquivo até que não haver mais nenhum byte	
	while True:
		#Lendo byte a byte
		b = f.read(1)
		#Condicional de fim de arquivo e envio da convensão de final de arquivo
		if not b:
			#4 quebras de linha significa fim de arquivo
                        s.send(b'´´\n\n\n\n')
			#Saida do loop de leitura e envio
			break
		#Envio de cada byte lido para o servidor
		s.send(b)
#Recebendo resposta do servidor
res = s.recv(1024)
#Exibindo resposta
print('Resposta do servidor: ' + res)
#Finalizando conexão
s.close()
