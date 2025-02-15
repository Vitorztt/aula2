def verificaridade(idade):
    if idade >= 18:
        return"pode ver o filme"
    else:
        return "não pode ver o filme"

print("Digite sua idade:")
idade= int(input())

resultado = verificaridade(idade)

print(resultado)