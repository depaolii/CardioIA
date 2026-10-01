import csv
import unicodedata
import string

#Remover acentos para padronização
def remover_acentos(texto):
    texto_decomposto = unicodedata.normalize('NFD', texto)
    texto_sem_acento = ''.join(c for c in texto_decomposto if unicodedata.category(c) != 'Mn')
    return texto_sem_acento

#Verificar se todas as palavras aparecem na frase (ignorando pontuação)
def todas_palavras_presentes(sintoma, frase):
    tradutor = str.maketrans('', '', string.punctuation)
    palavras_sintoma = remover_acentos(sintoma.lower()).translate(tradutor).split()
    palavras_frase = remover_acentos(frase.lower()).translate(tradutor).split()
    return all(palavra in palavras_frase for palavra in palavras_sintoma)

#Ler arquivo .csv
with open("mapa_conhecimento_sintomas.csv", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    dados_csv = list(leitor)

#Ler arquivo .txt
with open("frases_sintomas_pacientes.txt", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for paciente in linhas:
  for linha in dados_csv:
    if todas_palavras_presentes(linha[0], paciente) or todas_palavras_presentes(linha[1], paciente):
      print(f"Frase do paciente: {paciente} / Doença: {linha[2]}")
