# idade = int(input('Qual é a sua idade? '))

# if idade >= 18:
#     print('Você é maior de idade!!!')
# else:
#     print('Você é menor de idade!!!')

media = float(input('Digite sua média: '))
faltas = float(input('Digite a porcentagem de faltas: '))

# if media >= 6:
#     print('Aprovado(a)')
# elif media >=4:
#     print('Exame')
# else:
#     print('DP')

if media >=6 and faltas <=25:
    print('Aprovado(a)')
    if media == 10:
        print('Parabéns pelo 10zão')
elif media >=4 and faltas <=25:
    print('Exame')
else:
    print('DP') 
 