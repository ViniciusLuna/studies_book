import math
coef_a = float(input("Entre com o coeficiente A: "))
coef_b = float(input("Entre com o coeficiente B: "))
termo_c = float(input("Entre com o termo independente C: "))

delta = coef_b**2 -4 * coef_a * termo_c

if delta > 0:
    x1 = (-coef_b + math.sqrt(delta)) / (2 * coef_a)
    x2 = (-coef_b - math.sqrt(delta)) / (2 * coef_a)
    print("Raizes reais e distintas")
    print("x1 = %8.2f" %x1)
    print("x2 = %8.2f" %x2)
elif delta == 0:
    x = -coef_b / (2 * coef_a)
    print("Raizes reais e iguais: x = %8.2f" %x)
else:
    print("Nao existem raizes reais...")