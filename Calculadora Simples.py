resul = 0
sair = True

while  sair == True:
 num1 = float(input("Digite um numero:"))
 calc = int(input("Escolha a opção: 1-soma  2-subtração  3-multiplicação  4-divisão"))
 num2 = float(input("Digite  outro numero: "))
 if calc == "1":
    resul = num1 + num2
 elif calc == "2":
    resul = num1 - num2
 elif calc == "3": 
    resul = num1 * num2
 elif calc == "4":
    resul ==  num1 / num2
 else :
    print ("Opção Inválida")

        
print (f"A operação foi soma: {num1} {calc} {num2} = {resul}")

    
