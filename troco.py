traço = '-'*20
print(traço)
print('Calculadora de troco\n')
print(traço)
#somente para testes
#troco = 188.9
def calculotroco(troco):
    psv = (100,50,20,10,5,2,1,0.5,0.25,0.1,0.05)
    print('O troco é')
    for vlr in psv:
        qntd = int(troco / vlr)
        troco = troco - qntd*vlr
        print(' {} notas de R${}'.format(qntd,vlr))
#        print('{:.2f}'.format(troco))
rpt = 'y'
while rpt == 'y':
    troco = float(input('Insira o troco '))
    calculotroco(troco)
    rpt = input('Deseja calcular novamente?(y/n)')
