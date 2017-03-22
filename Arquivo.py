#!/usr/bin/python

__author__ = "Vimerson Pereira da Silva"
__copyright__ = ""
__license__ = "LGPLv3"
__version__ = "0.1.0"
__maintainer__ = "Vimerson Pereira da Silva"
__email__ = "vimerson@cemig.com.br"
__status__ = "Testing"

from os import system
from os import remove
from urllib import urlopen
import logging
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/root/bpms_parser.conf")

path = config.get('Path', 'path')
protocolo = config.get('URI', 'protocolo')

logging.basicConfig(filename='/var/log/bpms_parser.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Arquivo():
	def obterJsonUnico(self, instanciaID, servidor, rest_api, usuario, senha):
	#obj = urllib.urlopen('http://' + usuario + ':' + senha +'@pwnap-bhebpm04.cemig.ad.corp/rest/bpm/wle/v1/process/' + instanciaID  + '?parts=executionTree').read()
	
		obj = urlopen(protocolo + '://' + usuario + ':' + senha +'@' + servidor + rest_api + str(instanciaID)).read()
		logging.info ("Obtido JSON " + str(instanciaID) + " do servidor: "  + servidor)
	
		arquivo = Arquivo()
		arquivo.gravarJSON(obj, instanciaID)

	def gravarJSON (self, obj, instanciaID):
		arquivo = open(path + str(instanciaID) + '.json', 'w')
		arquivo.write(obj + " \r\n")
		arquivo.close()
		logging.info ("Gravado JSON em: " + path + str(instanciaID) + ".json")
		
	def apagarArquivo(self, instanciaID, extensao):
		remove(path + str(instanciaID) + '.' + extensao)
		logging.info ("Apagado: " + path + str(instanciaID) + '.' + extensao)