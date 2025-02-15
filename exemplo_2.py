# sistema de descontp de veiculos 
#solicite o nome do veiculo 
#e o preço
#se o preço . 80k -. 60% de desconto 


print("bem vindo")
print("qual o nome do seu veiculo")
veiculo= str(input())

print("qual o preço do seu veiculo:")
preço= float(input())


if preço >= 80000:
    desconto = 0.6
elif preço > 50000:
    desconto = 0.3
else:
    desconto = 0


valor_final= preço*(1-desconto)

print("veiculo: ", veiculo)
print("preço:", preço)
print("seu desconto é de:",desconto * 100, "%" )
print("seu preço final é de R$:", valor_final)