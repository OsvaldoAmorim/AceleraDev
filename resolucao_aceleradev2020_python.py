#Codigo para resolução AceleraDev 2020 - Python
#By: Osvaldo Amorim
#---------------------------------------------------------------------------------------------------------------------
#pegando as frase a ser criptografada a partir do meu token

import requests

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=6a496d6df4a249890e13f3cac964ae6b4546eacd'
resp = requests.get(url)
resp

data = resp.json()
data
#--------------------------------------------------------------------------------------------------------------------
#Codigo Criptografia

entrada =data['cifrado']

#Rodar esse codigo para cada entrada uma das entradas abaixo. A decodificacao será a concatenação de seus resultados.
#entrada1: 'jg uif gbdut ep opu gju uif uifpsz'
#entrada2: 'dibohf uif gbdut'
#entrada3: 'bmcfsu fjotufjo'

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
gap = -1

n = len(entrada)   #contador de caracteres da entrada
n2 = len(alfabeto) #numero total do alfabeto

i = 0    # contador para chegar até n
aux = 0  # variavel auxiliar para "fatiar" a entrada
aux2 = 0 # variavel para armazenar o valor dos caracteres da entrada
aux3 = 0 # variavel para armazenar os valores criptografados

for termo in entrada:
  while i <= n-1: #n-1, pois a função [i] começa do zero
    aux = (entrada[i])
    a = int(ord(aux))
    truco = a - 97 + gap
    while (truco) >= 26:
      truco = truco - 26
    if a == 32:
      aux3 = 32
      i += 1
      print (" ", end=" ")
    else:  
      aux2 = truco
      aux3 = alfabeto[aux2]
      i += 1
      print (aux3, end=" ")

#'decifrado': 'if the facts do not fit  the theory, change the facts. albert einstein'
#-------------------------------------------------------------------------------------------------
#Criptografando com sha1 a frase descoberta

import hashlib
hashlib.sha1(b'if the facts do not fit  the theory, change the facts. albert einstein').hexdigest

#------------------------------------------------------------------------------------------------------------------
#Salvei em valores o json que obtive, afim de conseguir editar os campos 'deicfrado' e 'resumo_criptografico'.
#Editei o arquivo answer.json e sobrescrevi-lo com os dados acima

import json
#['numero_casas', 'token', 'cifrado', 'decifrado', 'resumo_criptografico']
valores = {
    
  'numero_casas': 1,
  'token': '6a496d6df4a249890e13f3cac964ae6b4546eacd',
  'cifrado': 'jg uif gbdut ep opu gju uif uifpsz, dibohf uif gbdut. bmcfsu fjotufjo',
 'decifrado': 'if the facts do not fit  the theory, change the facts. albert einstein',
 'resumo_criptografico': 'bcfd599cb9e05203f7ed27db5a78ac17853d83e0'
 
 }
with open('answer.json', 'w+') as json_file:
    json.dump(valores, json_file, indent=5)
    
#-------------------------------------------------------------------------------------------------------------------    
#Enviando o arquivo answer.json via post

import requests

x =requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=6a496d6df4a249890e13f3cac964ae6b4546eacd", files={"answer": open("answer.json", "rb")})
print(x.text)
print(x.status_code)
