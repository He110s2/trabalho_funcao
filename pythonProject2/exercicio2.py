def calcular_aumento(salario, percentual):
    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento
    return aumento, novo_salario


salario_atual = float(input("Digite o valor do salário atual: R$ "))
percentual_aumento = float(input("Digite a porcentagem de aumento: "))

aumento, novo_salario = calcular_aumento(salario_atual, percentual_aumento)

print(novo_salario, "valor do aumento")
print(aumento,"novo salario")