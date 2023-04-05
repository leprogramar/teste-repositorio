

'''
#ESTRUTURA SEQUENCIA
#1
print("Alo mundo")

#2
n1 = input("digite um numero")
print("o numero que voce digitou foi:" + n1)

3#
n2 = int(input("digite um numero"))
n3 = int(input("digite outro numero"))

soma = (n2 + n3)
print(f'A soma dos seus numeros e:' + str(soma))
print(type(soma))

#4
nota1 = int(input("digite a sua primeira nota"))
nota2 = int(input("digite a sua segunda nota"))
nota3 = int(input("digite a sua terceira nota"))
nota4 = int(input("digite a sua quarta nota"))

media = (nota1+nota2+nota3+nota4/4)
print(f'a media das notas das suas provas foi:' + str(media))

#5
print("###CONVERSOR DE MEDIDAS####")
medida = int(input("digite o numero em metros"))
centimetros = medida*100
print(f'o valor em centimetros e:' + str(centimetros))
'''


#6



'''
#7
print("###CALCULADORA DE AREA DE QUADRADOS###")
q = int(input("digte o valor da aresta da sua figura"))
area = (q**2)
print(f'o valor da area desssa figura e: ' + str(area))
area_dobro = (area*2)
print(f'o dobro dessa area: '+ str(area_dobro))
'''


'''
#8
print("###CALCULADORA DE SALARIO###")
valor_hora = int(input("Digite o valor da hora de trabalho"))
horas_de_trabalho = int(input("Digite o numero de horas trabalhadas por dia"))
salario =  (valor_hora * horas_de_trabalho * 30)
print(f' seu salario por mes e de:' + str(salario))
'''



'''
#9
print(f'### CONVERSORA DE TEMERATURA ###')
f = int(input("DIGITE A TEMPERATURA EM FAHRENHEIT"))
c = (5*((f -32)/9))
print(f'a temperatura em C e igual e:' + str(c))
'''



'''
#10
print(f'###CONVERSOR DE TEMPERATURA###')
c = int(input(f'digite a teperatura em celsius'))
f = (9/5*c+32)
print(f'a tempeteratura em fahrenheit: ' + str(f))
'''


#11



'''
#12
print(f'###CALCULADORA DE PESO IDEIAL###')
altura = float(input(f'informe sua altura atual'))
peso_ideal = ((72.7 * (altura/100.0))- 58.0)
print(f'Com base na sua altura, seu peso ideal e: '+ str(peso_ideal))
print(altura)
'''

'''
#13
print(f'###CALCULADORA DE PESO IDEAL###')
h = float(input(f'informe a sua altura em numeros inteiros e sem virgulas'))
s = input(f'informe o seu sexo: F para feminino e M para masculino')
F = True
M = False
if s == True:
    peso_ideal1 = ((62.1 * (h/100.0)-44.7))
    print(f'Seu peso ideal e: ' + str(peso_ideal1))

else:
    peso_ideal2 = ((72.7 * (h/100.0) - 58))
    print(f'Seu peso ideal e: '+ str(peso_ideal2))
'''



'''
#14
def calcula_excesso(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        return excesso, multa
    return 0, 0
peso = int(input("Digite o peso em Kg"))
print(calcula_excesso(peso))
'''



'''
#15
salario = int(input(f'Digite o valor recebido por hora \n'))
horas = int(input("Digite o numero de horas trabalhadas\n"))

salario_mes = (salario * horas * 30)
salario_imposto = (float(salario_mes) * 0.11)
salario_inss = (float(salario_mes) * 0.08)
salario_sindicato = (float(salario_mes) * 0.05)
salario_liquido = (salario_mes - salario_imposto - salario_inss - salario_sindicato)
salario_final = round(salario_liquido,1)

print(f'Seu salario bruto e: {salario_mes} \n')
print(f'Voce pagou este mes de imposto o valor de: {salario_imposto}\n')
print(f'Voce pagou para o sindicato:{salario_sindicato}\n')
print(f'Seu salario liquido e:{salario_final}')
'''

'''
#16
area_pintada = int(input(f'Digite a medida em metros quadrados que voce vai pintar \n'))
cobertura = int((area_pintada / 3))
numero_latas = int((cobertura/18))
valor_tinta = (numero_latas * 80)

print(f'Voce precisa comprar {numero_latas} latas')
print(f'O valor total e igual a {round(valor_tinta,2)}')
'''

#17


'''
#18
tamanho = int(input(f'Informe o tamano do arquivo para download'))
velociade = int(input(f'Informe a velocidade de download'))
calculo = (tamanho/velociade)
print(f'O tempo estimado para baixar esse arquivo e de: {calculo} minutos!')
'''
 #fim! parabens pra min
