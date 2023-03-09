# armazena um núemro pequeno 
maior_numero = -999999

#entra com o primeiro número
number = int(input("Entre com um número ou digite -1 para parar: "))

#Se o número não for igual a -1 cintinua
while number != -1:
    #O número é maior que o maior_numero
    if number > maior_numero:
    #Sim, atualiza maior_numero:
        maior_numero = number
    #Entre com o proxímo número.
    number = int(input("Entre com um número ou digite -1 para parar: "))
    
#Print the largest number
print("O mair número é: ", maior_numero)