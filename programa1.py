#Capitulo 02 Tipos de Dados

#Python nao exige a declaracao de variaveis antes de seu uso - autor

pi = 3.14159265
raio = 5
altura =10
vol_cil = pi * raio **2 * altura


#Operadores relacionais
idade = 18
idade >= 18
#True
idade < 18
#False
idade == 18
#True
idade != 18
#False

#Quando duas ou mais expressoes precisam ser avaliadas para que o resultado possa ser utilizado na tomada de decisao, devemos nos valer dos operadores logicos - autor 
#Operadores logicos
idade >= 16 and idade <= 21
#True

#Matrizes
dia_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
#Forma dinamica do seu array
quantidade = int(input("Informe a quantidade de valors:"))
valores = [0 for x in range(quantidade)]
valores[4] = 520
print(valores)

#As matrizes (ou listas) em Python sao, na verdade, uma classe para armazenamento de dados. 
#Alguns metodos para insercao e remocao de elementos de uma matriz
valores = [100,320,450,560,680]
valores.insert(3,280)
print(valores)
valores.append(800)
print(valores)

#if 450 in valores: print (True)
450 in valores
#True


tamanho = 5
medicoes = [0 for x in range(tamanho)]
consumo = float(input("Informe a 1a. medição de consumo:"))
total = consumo
consumo = float(input("Informe a 2a. medição de consumo:"))
total+= consumo
consumo = float(input("Informe a 3a. medição de consumo:"))
total+= consumo
consumo = float(input("Informe a 4a. medição de consumo:"))
total+= consumo
consumo = float(input("Informe a 5a. medição de consumo:"))
total+= consumo

media = total / tamanho
<<<<<<< HEAD
print("Média das 5 medições de consumo %8.2f"% media) #8 digitos inteiros e 2 casas decimais

valor = float(input("Digite um valor numerico: "))
if valor <0:
    print("Voce digitou um valor negativo")
else:
    print("Voce digitou um numero positivo")
=======
print("Média das 5 medições de consumo %8.2f"% media) #8 digitos inteiros e 2 casas decimais
>>>>>>> 59983c0b5af92876b48723a0a0c3bca3788a57d7
