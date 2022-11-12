def soma_imposto(taxaImposto, custo):
    return (1 + taxaImposto/100) * custo

custo = float(input('Digite o valor de custo: '))
taxa = float(input('Digite a taxa de impostos: '))

print('Valor com imposto:', soma_imposto(taxa,custo))