from dict_1500 import * #eliminado
from dict_1600 import *
#from dict_2100 import *
# Abra o arquivo .txt em modo de leitura
with open('dict_2100.txt', 'r') as file:
    # Crie uma lista para armazenar as palavras
    lista_palavras = []
    
    # Leia cada linha do arquivo
    for linha in file:
        # Remova qualquer espaço em branco à direita (como quebras de linha)
        palavra = linha.rstrip()
        
        # Adicione a palavra à lista
        lista_palavras.append(palavra.lower())

# Exiba a lista de palavras
print(len(lista_palavras))
novas_palavras = lista_palavras
i = 0
print(f"wordleDictionary tem {len(wordleDictionary)}.")
print(f"lista palavras tem {len(lista_palavras)}.")

palavras_repetidas = []

for palavra in wordleDictionaryNoAccents:
    if wordleDictionaryNoAccents.count(palavra) > 1 and palavra not in palavras_repetidas:
        palavras_repetidas.append(palavra)

print("Palavras repetidas na lista:", palavras_repetidas)
    
ver = True
for palavra in wordleDictionaryNoAccents:
    if palavra not in lista_palavras:
        i += 1
        novas_palavras.append(palavra)

print(i)
print(len(novas_palavras))

# Abra um novo arquivo .py em modo de escrita
with open('novo_arquivo.py', 'w') as file:
    # Escreva a lista no arquivo
    file.write("nova_lista = [\n")
    for palavra in novas_palavras:
        file.write(f"    '{palavra}',\n")
    file.write("]")