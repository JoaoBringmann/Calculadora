resul = 0
sair = True
esc = 0

while  sair == True:
 num1 = float(input("Digite um numero:"))
 calc = (input("Escolha a opção: +, -, *  ou /:\n"))
 num2 = float(input("Digite  outro numero: "))
 if calc == "+":
    resul = num1 + num2
 elif calc == "-":
    resul = num1 - num2
 elif calc == "*": 
    resul = num1 * num2
 elif calc == "/":
    resul ==  num1 / num2
 else :
    print("Número ou opção incorretos, Digite novamente")

 esc = int(input("Para finalizar a conta digite 5"))
 if esc == 5:
   sair = False

print (80*"-")
print (f"A operação foi soma: {num1} {calc} {num2} = {resul}")

    
