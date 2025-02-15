#criar novo sistema 
#que calcule o valor de a, valor de B e valor de C
#calcular o bhaskara
#Delta= b² - 4*a*c
#bhaskara

import math

print("Digite um valor:")
a= float(input())

print("Digite o valor de B:")
b= float(input())

print("Digite o valor de c:")
c= float(input())

#calcule o delta
delta= b**2 - 4*a*c 


raiz_delta = math.sqrt(delta)
x1 = (-b + raiz_delta ) / (2 * a)

x2 = (-b - raiz_delta) / (2 * a)

print("seu resultado de x1 é:", x1 , " e o valor de x2 é:", x2)

