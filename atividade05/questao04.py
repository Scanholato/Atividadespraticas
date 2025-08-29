"""
4 - Crie um programa que calcule a quantos dias um indivíduo está vivo de acordo com a data do dia.
"""

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_atual = datetime.today()

dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")