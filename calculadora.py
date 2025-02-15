def menu ():
    print("menu da calculadora")
    print("1- soma")
    print("2-subtração")
    print("3- sair")

def soma(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1- n2

def verificaOpcao(opcao):
    if opcao == 1:
        num1 = float(input("Digite o numero 1:"))
        num2 = float(input("Digite o numero 2:"))
        print(soma(num1, num2))
    elif opcao  == 2 :
        num1 = float(input("Digite o numero 1:"))
        num2 = float(input("Digite o numero 2:"))
        print(subtrair(num1, num2))

def calculadora():
    while True:
        menu()
        opcao = int(input("escolha uma opcao"))
        verificaOpcao(opcao)

calculadora ()