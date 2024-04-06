resul = 0
sair = 1

while  sair == 1:
    calc = int(input("Escolha a opção:\n 1)Soma\n 2)Subtração\n 3)Multiplicação\n 4)Divisão\n 0)Sair\n"))
    if calc == "0":
        print("Encerrando Calculo")
        sair = 0
        continue
    if calc not in [1, 2, 3, 4, 0]:
        print("Número inserido inválido")
        break
    num1 = float(input("Digite um número: "))
    if not num1.is_integer():
        print("Valor inválido. Digite um número inteiro.")
        continue
    num2 = float(input("Digite outro número: "))
    if not num2.is_integer():
        print("Valor inválido. Digite um número inteiro.")
        continue
    if calc == 1:
        resul = num1 + num2
        calc = "+"
    elif calc == 2:
        resul = num1 - num2
        calc = "-"
    elif calc == 3:
        resul = num1 * num2
        calc = "*"
    elif calc == 4:
        if num2 == 0:
            print("Não é possível dividir por zero.")
            continue
        resul = num1 / num2
        calc = "/"
    else:
        print("Opção inválida, digite novamente.")
        continue
    print("-" * 80)
    print(f"A operação foi: {num1} {calc} {num2} = {resul}")

# Add a try-except block to catch ValueError exceptions
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")