traço = '-'*20
print(traço)
print('Calculadora de troco\n')
print(traço)
#desabilitado para maior velocidade de teste
#troco = float(input('Insira o troco '))
troco = 250
n100 = int(troco / 100)
troco = troco - (n100*100)
print('O troco é: \n {} notas de R$100'.format(n100))
#para teste 
n50 = int(troco/50)
troco = troco - (n50*50)
print('O troco é: \n {} notas de R$50'.format(n50))

print(troco)
