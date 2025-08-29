import json

pessoa = {
    "nome": "Murilo",
    "idade": 30,
    "cidade": "Águas de São Pedro"
}

with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")