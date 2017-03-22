#!/usr/bin/python
__author__ = "Vimerson Pereira da Silva"
__license__ = "LGPLv3"
__version__ = "0.1.0"
__maintainer__ = "Vimerson Pereira da Silva"
__email__ = "vimerson@cemig.com.br"
__status__ = "Testing"

from os import system
from Arquivo import Arquivo
import logging
import ConfigParser

#Mapping conf file
config = ConfigParser.ConfigParser()
config.read("/root/bpms_parser.conf")

#Mapping variables
usuario = config.get('Authentication', 'usuario')
senha = config.get('Authentication', 'senha')
usuario_es = config.get('Authentication', 'usuario_es')
password_es = config.get('Authentication', 'password_es')
servidor = config.get('URI', 'servidor')
rest_api = config.get('URI', 'rest_api')
url = config.get('URI', 'url')
rest_cmd = config.get('URI', 'rest_cmd')
faixa_inicio = config.get('Range', 'faixa_inicio')
faixa_fim = config.get('Range', 'faixa_fim')


#Four steps:
# 1. Get data from IBM BPMS
# 2. Save JSON data in filesystem
# 3. Record datas on NoSQL index (similar as database for relational)
# 4. Delete or not JSON on filesystem (sucess or not, respectively)


arquivo = Arquivo()

for instanciaID in range(int(faixa_inicio), int(faixa_fim) + 1):
	
	# 1. Getting data from IBM BPMS (v8.5.5)
	# 2. Saving JSON data in filesystem
	
	arquivo.obterJsonUnico(instanciaID, servidor, rest_api, usuario, senha)
	
	#3. Record data on NoSQL (elasticsearch v5.2.2)
	try:
		nosql_gravar = system ("curl -s -u " + usuario_es + ":" + password_es + " " + rest_cmd + " " + url + str(instanciaID) + " -d @/usr/share/bpms/instancias/" + str(instanciaID) + '.json --max-time 30' + " | grep 'status'")
		
		#Show progress of recording data
		percentual = (float(instanciaID)/float(faixa_fim) * 100)
		percentual_arredondado = format(percentual, '.2f')
		
		print (str(percentual_arredondado) + " % (" + str(instanciaID) + " de " + str(faixa_fim) + ")")
		
	except Exception as e:
		logging.error(str(e))
	
	
	# 4. Deleting JSON on filesystem (in case of sucess)
	if (nosql_gravar == 256):
		logging.info("Gravado JSON " + str(instanciaID) + " em " + url)
		
		arquivo.apagarArquivo(str(instanciaID), "json")
		
	# 4. No delete JSON on filesystem (fault case)
	else:
		logging.warn("Falha ao gravar " + str(instanciaID) + " em " + url)
		logging.warn("Tratar " + str(instanciaID) + ".json manualmente")