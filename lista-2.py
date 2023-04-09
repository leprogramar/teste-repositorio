'''
#19
n1 = int(input(f'digite um numero\n'))
n2 = int(input(f'digite outro numero\n'))

if n1 > n2:
    print(n1)
else:
    print(n2)
'''

'''
#20
n1 = int(input(f'Digite um numero\n'))

if n1 > 0:
    print(f'valor numerico positivo\n')
else:
    print(f'valor numerico negativo\n')
'''

'''
#21
sexo = input(f'Sexo: F para feminino, M para masculino\n')

if sexo == "F":
    print("F: Feminino")
else: 
    print(f'M: Masculino, Sexo invalido')
'''

'''
#22
letra = input(f'Digite uma letra e descubra se ela e uma vogal ou consoante\n')

if letra == "a" or letra == "i" or letra == "o" or letra == "u":
    print(f'A letra {letra} e uma vogal!')
else:
    print(f'A letra {letra} e uma consoante!')
'''

'''
#23
nota1 = int(input(f'Digite a sua primeira nota.\n'))
nota2 = int(input(f'Digite a sua segunda nota.\n'))

media1 = (nota1 + nota2)/2

if media1 == 10:
    print(f'Aprovado com distincao!')
elif media1 >= 7:
    print(f'Aprovado!')
else:
    print(f'Reprovado')
'''


'''
#24
n1 = int(input(f'Digite um numero \n'))
n2 = int(input(f'Digite outro numero\n'))
n3 = int(input(f'Digite outro numero\n'))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
'''

'''
#25
n1 = int(input(f'Digite um numero \n'))
n2 = int(input(f'Digite outro numero\n'))
n3 = int(input(f'Digite outro numero\n'))

if n1 > n2 and n1 > n3:
    print(f' o maior numero e {n1}\n')
elif n2 > n1 and n2 > n3:
    print(f' o maior numero e {n2}\n')
else:
    print(f' o maior numero e {n3}\n')

if n1 < n2 and n1 < n3:
    print(f' o menor numero e {n1}\n')
elif n2 < n1 and n2 < n3:
    print(f' o menor numero e {n2}\n')
else:
    print(f' o menor numero e {n3}\n')
'''

'''
#26
print(f'### QUAL PRODUT0 COMPRAR? ###')

produto1 = float(input(f'Digite o valor do primeiro produto:\n'))
produto2 = float(input(f'Digite o valor do segundo produto:\n'))
produto3 = float(input(f'Digite o valor do terceiro numero: \n')) 

if produto1 < produto2 and produto1 < produto3:
    print(f'Compre o produto de {produto1}!')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Compre o produto de {produto2}!')
else:
    print(f'Compre o produto de {produto3}!')
'''


'''
#27
n1 = int(input(f'Digite um numero \n'))
n2 = int(input(f'Digite outro numero\n'))
n3 = int(input(f'Digite outro numero\n'))

lista_n = []

lista_n.append(n1)
lista_n.append(n2)
lista_n.append(n3)
lista_n.sort(reverse=True)
print(lista_n)
'''

'''
#28 
turno = input(f'Informe qual o seu turno: M:matiturno, V: vespertino, N: noturno\n')
if turno == "M":
    print(f'Matiturno')
elif turno == "V":
    print(f'Vespertino')
elif turno == "N":
    print(f'Noturno')
elif turno != "M" and turno != "V" and turno != "N":
    print(f'o valor {turno} e invalido')
'''

#29

#30


'''
#31
n1 = int(input(f'Digite um numero de 1 a 7 e descubra o dia da semana \n'))
if n1 == 1:
    print("1-Domingo")
elif n1 == 2:
    print("2-Segunda-feira")
elif n1 == 3:
    print("3-Terca-feira")
elif n1 == 4:
    print("4-Quarta-feira")
elif n1 == 5:
    print("5-Quinta-feira")
elif n1 == 6:
    print("6-Sexta-feira")
elif n1 == 7:
    print("7-Sabado")
'''

#32
# nota1 = float(input(f'Digite a sua primeira nota \n'))
# nota2 = float(input(f'digite a sua segunda nota \n'))
# 
# media = (nota1 + nota2)/2
# 
# if media == 9.0 or media == 10.0:
    # print(f'Nota: A')
# elif media == 7.5 or media == 8.9:
    # print(f'Nota: B')
# elif media == 7.4 or media == 6.0:
    # print(f'Nota: A')
# 
# 

#33




