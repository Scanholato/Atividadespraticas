import csv

# Dados
pessoas = [
    {"Nome": "Murilo", "Idade": 30, "Cidade": "Águas de São Pedro"},
    {"Nome": "Carlota", "Idade": 28, "Cidade": "Santos"},
    {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"}
]

# Escrevendo CSV
with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    colunas = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(pessoas)

print("Arquivo CSV criado com sucesso!")