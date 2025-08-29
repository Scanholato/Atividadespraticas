import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            return "CEP não encontrado"
        
        return f"""
                CEP: {dados['cep']}
                Logradouro: {dados['logradouro']}
                Bairro: {dados['bairro']}
                Cidade: {dados['localidade']}
                Estado: {dados['estado']}
                """
    except requests.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"
    


cep = input("Digite o CEP (apenas números): ")
resultado = consultar_cep(cep)
print(resultado)
