#!/usr/bin/python
from os import system
from Arquivo import Arquivo
import logging

usuario = "<<bpms_user>>"
senha = "<<bpms_pass>>"
usuario_es = "elasticsearch_user"
password_es = "<<elasticsearch_pass>>"
#instanciaID = "66992"
servidor = "<<FQDN>>/rest/bpm/wle/v1/process/"
url = "http://<<FQDN>>:9200/index_01/pw04/"
rest_cmd = "-XPUT"

arquivo = Arquivo()

for instanciaID in range(1, 1000):
	#OBTEM do servidor de BPMS o JSON contendo os dados da instancia e GRAVA no disco do servidor
	arquivo.obterJsonUnico(str(instanciaID), servidor, usuario, senha)
	
	#GRAVA no banco NoSQL (elasticsearch v5.2.2) os dados da instancia
	try:
		nosql_gravar = system ("curl -u " + usuario_es + ":" + password_es + " " + rest_cmd + " " + url + str(instanciaID) + " -d @/usr/share/bpms/instancias/" + str(instanciaID) + '.json --max-time 30')
	except Exception (e):
		print (e)
		logging.error("[ERROR]" + e)
	
	#LOGA os resultados
	print ("\n Status " + str(nosql_gravar))
	if (nosql_gravar == 0):
		logging.info("[OK] " + "Gravado JSON " + str(instanciaID) + " em " + url)
		#APAGA arquivo do servidor	
		arquivo.apagarArquivo(str(instanciaID), "json")
	else:
		logging.warn("[WARNING] Falha ao gravar " + str(instanciaID) + " em " + url)