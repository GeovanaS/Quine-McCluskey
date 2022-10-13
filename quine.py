#Exemplo entrada: !A*!B*!C*!D + !A*!B*!C*D + !A*B*!C*D + !A*B*C*!D + !A*B*C*D

import math
from operator import eq
from typing import List,Iterable

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
def listaMintermos(vBin,tam):
    i=0
    for i in range(0,tam):
        bin2dec(aux[i])
    print('Mintermos:',dec)

def montarTabela(mint):
    linha = 0
    col = 0
    tab = [[0,4,12,8],
           [1,5,13,9],
           [3,7,15,11],
           [2,6,14,10]]          

    for linha in range(0,4):
       # print('linha',linha)
        #print('mint',mint)
        #if linha == mint:
           # print('teste')
            #tab[linha]= 1
        print(tab[linha])
   # print('\n',tab)

def agrupaUns(tabela,tam):
    grupo = [[] for i in range(tam+1)]
    for i in tabela:
        grupo[i.count('1')] += [i]
    return grupo

def compara_strings(str1, str2):
	l1 = list(str1); l2 = list(str2)
	cont = 0
	for i in range(len(l1)):
		if l1[i] != l2[i]:
			cont += 1
			l1[i] = '_'
	if cont > 1:
		return -1
	else:
		return("".join(l1))

def verificaPrimosImplicantes(eqBin):
	primo = []
	while 1:
		check1 = ['$']*len(eqBin)
		temp = []
		for i in range(len(eqBin)):
			for j in range(i+1, len(eqBin)):
				k=compara_strings(eqBin[i], eqBin[j])
				if k != -1:
					check1[i] = '*'
					check1[j] = '*'
					temp.append(k)
		for i in range(len(eqBin)):
			if check1[i] == '$':
				primo.append(eqBin[i])
		if len(temp) == 0:
			return primo
		eqBin = list(set(temp))




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
print(bin)
nMint = len(aux)

listaMintermos(bin,nMint)

primo_implicante=verificaPrimosImplicantes(bin[0])
print('primos implicantes:')
print(primo_implicante)
