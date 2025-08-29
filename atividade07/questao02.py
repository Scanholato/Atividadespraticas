
import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return (f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        return(f"Erro ao escrever no arquivo: {e}")


dados = [
    ['Murilo', 31, 'Santo André'],
    ['Carolina', 28, 'Santos'],
    ['Thor', 12, 'São Vicente']
]

nome_arquivo = input("Digite o nome do arquivo: ")
print(escrever_csv(nome_arquivo, dados))
