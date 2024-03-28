resul = 0
sair = 1

while  sair == 1:
 calc = (input("Escolha a opção:\n 1)Soma\n 2)Subtração\n 3)Multiplicação\n 4)Divisão\n 0)Sair\n"))
 if calc == "0":
    print("Encerrando Calculo")
    sair = 0
    continue
 num1 = float(input("Digite um numero:"))
 num2 = float(input("Digite  outro numero: "))
 if calc == "1":
    resul = num1 + num2
    calc =  "+"
 elif calc == "2":
    resul = num1 - num2
    calc = "-"
 elif calc == "3": 
    resul = num1 * num2
    calc = "*"
 elif calc == "4":
    resul ==  num1 / num2
    calc = "/"
 else:
     print ("Opção Inválida, Digite Novamente")
 print (80*"-")
 print (f"A operação foi: {num1} {calc} {num2} = {resul}")

    
