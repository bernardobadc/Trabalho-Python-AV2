def calc_area(base_maior,base_menor,altura):
    return ((base_maior + base_menor) * altura)/2

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite valor da altura: "))

area = calc_area(base_maior, base_menor, altura)

print(area)