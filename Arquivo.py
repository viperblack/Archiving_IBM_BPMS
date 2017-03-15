#!/usr/bin/python
from os import system
from os import remove
from urllib import urlopen
import logging

path = "/usr/share/bpms/instancias/"
logging.basicConfig(filename='/var/log/bpms_parser.log', format='%(asctime)s:%(message)s', level=logging.INFO)

class Arquivo():
	def obterJsonUnico(self, instanciaID, servidor, usuario, senha):
	#obj = urllib.urlopen('http://' + usuario + ':' + senha +'@pwnap-bhebpm04.cemig.ad.corp/rest/bpm/wle/v1/process/' + instanciaID  + '?parts=executionTree').read()
	
		obj = urlopen('http://' + usuario + ':' + senha +'@' + servidor + instanciaID).read()
		logging.info ("[OK] " + "Obtido JSON " + str(instanciaID) + " do servidor: "  + servidor)
	
		arquivo = Arquivo()
		arquivo.gravarJSON(obj, instanciaID)

	def gravarJSON (self, obj, instanciaID):
		arquivo = open(path + str(instanciaID) + '.json', 'w')
		arquivo.write(obj + " \r\n")
		arquivo.close()
		logging.info ("[OK] " + "Gravado JSON em: " + path + instanciaID + ".json")
		#print ("Gravado JSON em: " + path + instanciaID + ".json")

		#	def obterHash(self, obj, instanciaID):
#		#Obter hash SHA-256
#		
#		sha256_hash = hashlib.sha256()
#		sha256_hash.update(obj)
#		hash_hex = sha256_hash.hexdigest()
#		arquivo = open(path + str(instanciaID) + '.sha256', 'w')
#		arquivo.write(hash_hex)
#		arquivo.close()
#		logging.info ("Obtido hash SHA-256 para: " + str(instanciaID))
	
#	def lerArquivo(self, instanciaID, extensao):
#		arquivo = open(path + str(instanciaID) + '.' + extensao, 'r')
#		saida = arquivo.read()
#		arquivo.close()
#		return saida
	
	def apagarArquivo(self, instanciaID, extensao):
		remove(path + str(instanciaID) + '.' + extensao)
		logging.info ("[OK] " + "Apagado: " + path + str(instanciaID) + '.' + extensao)