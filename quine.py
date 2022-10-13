import math
from operator import eq

def main():
    pass

if __name__ == '__main__':
    main()
  
nMint  = 0 
bin = []
mintermo=[]
dec = []

# Converte equacao binaria para decimal
def bin2dec(vBin):
    sum = 0
    n = len(vBin)
    for i,d in enumerate(vBin):
        if d == '1':
            sum += 2 ** (n-i-1)
    dec.append(sum)
    return sum

# Lista os mintermos da equação
def listaMintermos(vBin):
    bin2dec(aux[0])
    bin2dec(aux[1])
    bin2dec(aux[2])
    bin2dec(aux[3])
    bin2dec(aux[4])
    print('Mintermos:',dec)

entrada = input()
for i in range (0,15):
    aux = entrada
    aux = aux.replace("!A", '0')
    aux = aux.replace("!a", '0')
    aux = aux.replace("!B", '0')
    aux = aux.replace("!b", '0')
    aux = aux.replace("!C", '0')
    aux = aux.replace("!c", '0')
    aux = aux.replace("!D", '0')
    aux = aux.replace("!d", '0')
    aux = aux.replace("A", '1')
    aux = aux.replace("a", '1')
    aux = aux.replace("B", '1')
    aux = aux.replace("b", '1')
    aux = aux.replace("C", '1')
    aux = aux.replace("c", '1')
    aux = aux.replace("D", '1')
    aux = aux.replace("d", '1')
    aux = aux.replace("*",'')
    aux = aux.replace(" ", "")
    nVar = aux.count('+')
    aux = aux.split('+')

bin.append(aux)
#print(bin)

listaMintermos(bin)
