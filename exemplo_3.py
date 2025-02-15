#verificar se uma palavra é um palindromo 
#caso seja, axiba É palindromo
#a verificação deve ser casa insensitiva

print("Digite uma palvra:")
palavra= str(input()).strip().lower().replace(" ","")

if palavra == palavra[::-1]:
    print("é um palindromo!")
else:
    print("nao é um palindromo")


#strip retira o espaço 
#lower deixa a palavra minuscula
#replace junta a palavra