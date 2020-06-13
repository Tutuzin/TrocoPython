traço = '-'*20
print(traço)
print('Calculadora de troco')
print(traço)
#somente para testes
#troco = 188.9
def calculotroco(troco):
    psv = (100,50,20,10,5,2,1,0.5,0.25,0.1,0.05)
    print('O troco é')
    for vlr in psv:
        #calcula a quantidade de tal moeda
        qntd = int(troco / vlr)
        #atualiza o que falta para ser pago
        troco = troco - qntd*vlr
        #estética do programa
        if qntd != 0:
            meio = 'moeda'
            plural = 's'
            if vlr > 1:
                meio = 'nota'
            if qntd == 1:
                plural = ''
            print(' {} {}{} de R${}'.format(qntd,meio,plural,vlr))
#    print('{:.2f}'.format(troco))
rpt = 'y'
while rpt == 'y':
    troco = float(input('Insira o troco '))
    calculotroco(troco)
    rpt = input('Deseja calcular novamente?(y/n)')
