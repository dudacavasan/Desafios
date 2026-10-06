# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salario_novo = salario + aumento
print(f'O seu salário atual é: {salario: .2f}, com o aumento de: {aumento: .2f}, seu novo salário é: {salario_novo: .2f}')