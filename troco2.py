troco = 188.9
psv = {100:n100,50:n50,20:n20,10:n10,5:n5,2:n2,1:n1,0.5:n05,0.25:n02,0.10:n01,0.5:m05}
print('O troco é')
for vlr, qntd in psv.items():
    qntd = int(troco / vlr)
    troco = troco - qntd*vlr
    print(' {} notas de R${}'.format(qntd,vlr))
print(troco)

