resul = 0
sair = 1


def calc_soma(num1,num2):
    return num1+num2

def calc_sub(num1,num2):
    return num1-num2

def calc_div(num1,num2):
    return num1/num2

def calc_multi(num1,num2):
    return num1*num2

def somente_opcao(prompt):  #Para verificar se o usuario digitou uma letra ou um numero fora da lista que possa causar um erro de valor retornando "none"
    while True:
        try:
            calc = int((input(prompt)))
            if calc in [0, 1, 2, 3, 4]:
              return calc
            else:
                print("Opção invalida, tente novamente.")
        except ValueError:
            print("Digito invalido, tente por numeros")

def somente_num(prompt):    #Mesma coisa que o anterior mas somente para letras
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Digito invalido, tente por numeros")

def menu(somente_opcao):
    sair = 1
while  sair == 1:
    calc = somente_opcao("Escolha a opção:\n 1)Soma\n 2)Subtração\n 3)Multiplicação\n 4)Divisão\n 0)Sair\n")
    if calc == 0:
        print("Encerrando Calculo")
        sair = 0
        break
    num1 = somente_num("Digite o Primeiro Numero: ")
    num2 = somente_num("Digite o segundo Numero: ")
    if calc == 1:
        resul = calc_soma(num1,num2)
        calc = "+"
    elif calc == 2:
        resul = calc_sub(num1,num2)
        calc = "-"
    elif calc == 3:
        resul = calc_multi(num1,num2)
        calc = "*"
    elif calc == 4:
        if num2 == 0:
            print("Não é possível dividir por zero.")
            continue
        resul = calc_div(num1,num2)
        calc = "/"
    else:
        print("Opção inválida, digite novamente.")
        continue
    print("-" * 80)
    print(f"A operação foi: {num1} {calc} {num2} = {resul}")
    print("-" * 80)

menu(somente_opcao)