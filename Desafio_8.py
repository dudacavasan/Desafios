# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

def pode_ver_filme(idade, classificacao):
    if classificacao == 'L':
        idade_minima = 0
    elif classificacao == 'Maior de 12':
        idade_minima = 12
    elif classificacao == 'Maior de 14':
        idade_minima = 14
    elif classificacao == 'Maior de 16':
        idade_minima = 16
    elif classificacao == 'Maior de 18':
        idade_minima = 18

    if idade >= idade_minima:
        resposta = "Pode assistir o filme"
    else:
        resposta = "Não pode assistir o filme"

    print(f'A resposta é: {resposta}')

idade = int(input('Digite a sua idade: '))
classificacao = input('Digite a classificação indicativa do filme (L, Maior de 12, Maior de 14, Maior de 16, Maior de 18): ')

pode_ver_filme(idade, classificacao)
