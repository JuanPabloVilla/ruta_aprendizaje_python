'''
Crea un programa que calcule el impuesto a pagar según estos tramos:

Ingreso anual (€)	Tipo impositivo
0 – 12.450	19%
12.451 – 20.200	24%
20.201 – 35.200	30%
35.201 – 60.000	37%
Más de 60.000	45%
'''

ingreso_anual = int(input("Digite su ingreso anual: \n"))
if ingreso_anual > 0 and ingreso_anual < 12450:
    print(f"Debes pagar 19% de impuesto. tu total es de {ingreso_anual*0.19}")
elif ingreso_anual >12451 and ingreso_anual < 20200:
    print(f"Debes pagar 24% de impuestos. Tu total es de {ingreso_anual*0.24}")
elif ingreso_anual > 20201 and ingreso_anual < 35200:
    print(f"Debes pagar 30% impuestos. Tu total es de {ingreso_anual*0.30}")
elif ingreso_anual >35201 and ingreso_anual < 60000:
    print(f"Debes pagar 37% impuestos. Tu total es de {ingreso_anual*0.37}")
elif ingreso_anual > 60000:
    print(f"Debes pagar 45% impuestos. Tu total es de {ingreso_anual*0.45}")