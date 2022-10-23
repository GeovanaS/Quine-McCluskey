# Trabalho 1 - Ferramenta de CAD 

#Exemplo entrada: !A*!B*!C*!D + !A*!B*!C*D + !A*B*!C*D + !A*B*C*!D + !A*B*C*D


# Lists
vBin = []
vDec = []
tabelaV = []
epi = []

essentialPrimes =[]

#numero de mintermos
nMint = 0

# Converte equacao binaria para decimal
def bin2dec(vBin):
    soma = 0
    n = len(vBin)
    for i,d in enumerate(vBin):
        if d == '1':
            soma += 2 ** (n-i-1)
    vDec.append(soma)
    return soma

# Lista os mintermos da equacao
def listaMintermos(vBin,tam,aux):
    i=0
    mintermo_lista = []
    for i in range(0,tam):
        mintermo_lista.append(bin2dec(aux[i]))
    return mintermo_lista

# Agrupa pelo numero de 1's
def agrupaUns(binario, nVar):
    grupo0 = [] 
    grupo1 = []
    grupo2 = []
    grupo3 = []
    grupo4 = []
    for b in binario:
        cont = 0
        for digito in b:
            if digito == '1':
                cont +=1
        if cont == 0:
            grupo0.append(b)
        if cont == 1:
            grupo1.append(b)
        if cont == 2:
            grupo2.append(b)
        if cont == 3:
            grupo3.append(b)
        if cont == 4:
            grupo4.append(b)

    grupo = {}

    if nVar == 1:
        grupo = {0: grupo0, 1: grupo1}
    if nVar == 2:
        grupo = {0: grupo0, 1: grupo1, 2: grupo2}
    if nVar == 3:
        grupo = {0: grupo0, 1: grupo1, 2: grupo2, 3: grupo3}
    if nVar == 4:
        grupo = {0: grupo0, 1: grupo1, 2: grupo2, 3: grupo3, 4: grupo4}
    return grupo

# Converte entrada no formato de soma de produto para binario
def entradaSOP(entrada):
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
    return aux


# Converte o binario para o formato de soma de produto
def binario_para_equacao(selectedPrimes):
    eq = ''
    if(selectedPrimes[0]=='1'):
        eq += str("A")
    elif(selectedPrimes[0]=='0'):
        eq += str("!A")
    elif(selectedPrimes[0]=='_'):
        eq+=str("")

    if(selectedPrimes[1]=='1'):
        eq+=str("B")
    elif(selectedPrimes[1]=='0'):
        eq+=str("!B")
    elif(selectedPrimes[1]=='_'):
        eq+=str("")

    if(selectedPrimes[2]=='1'):
        eq+=str("C")
    elif(selectedPrimes[2]=='0'):
        eq+=str("!C")
    elif(selectedPrimes[2]=='_'):
        eq+=str("")

    if(selectedPrimes[3]=='1'):
        eq+=str("D")
    elif(selectedPrimes[3]=='0'):
        eq+=str("!D")
    elif(selectedPrimes[3]=='_'):
        eq+=str("")        

    return eq

##############################
#def dec(x):  # bin>>dec converter
#   return int(x, 2)

# Verifica se a diferenca entre as equacoes diferem por um bit    
def isBitShift_1(eq1, eq2):      
    for i in range(len(eq1)):
        if eq1[i] == '_':
            if eq1[i] != eq2[i]:
                return False
    n = eq1.replace('_', '')
    m = eq2.replace('_', '')
    cont = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            cont+=1
    if cont!=1:
        return False
    return True


# Gera os primos implicantes
def PI(eq1,eq2):
    saida = ''
    for i in range(len(eq1)):
        if eq1[i] == eq2[i]:
            saida += eq1[i]
        else:
            saida += '_'
    return saida


# Gera os selected primes    
def selectedPrimes(eq1,eq2):
    global essentialPrimes
    for i in eq1:
        if i not in eq2 and i not in essentialPrimes:
            essentialPrimes.append(i)
#################################

# Função main 
def main():
    op = input("Escolha a opção de entrada\n1-SOP\n2-Tabela Verdade\n3-Sair\n")
    if op == "1":
       print("Digite a equação no formato SOP:")  
       entrada = input()
       aux = entradaSOP(entrada)
       vBin.append(aux)
       print("Equação em binario:",aux)
       nMint = len(aux)
       minterms = listaMintermos(vBin,nMint,aux)
       print("Mintermos:",minterms)
       grupos = agrupaUns(aux,nMint-1)
       print("Agrupamento:",grupos)
       
       n = nMint-1

       group1 = []
       for i in range(n+1):
           group1.append([])

       #minBin = []
       #for i in minterms:
        #   eqBin = bin(i)[2:]
         #  if eqBin == n:
          #    continue
          # else:
           #   while len(eqBin) < n:
            #    eqBin = '0' + eqBin
        
         #  minBin.append(eqBin)

      # print('minbin:',minBin)  
    
       #agrupa pelo numero de 1's
       for i in aux:
           group1[i.count('1')].append(i)  

       print('group1:',group1)    

       minBin = []
       minBin2 = []
       group2 = []
       for i in range(n):
           group2.append([])

       for group in group1[:-1]:
           for i in group:
               if i not in minBin:minBin.append([bin2dec(i),i])
               for j in group1[group1.index(group)+1]:
                   if j not in minBin:minBin.append([bin2dec(j),j])
                   if bin2dec(i) > bin2dec(j):
                      continue
                   elif isBitShift_1(i,j):
                        if i not in minBin2: minBin2.append([bin2dec(i),i])
                        if j not in minBin2: minBin2.append([bin2dec(i),i])
                        group2[group1.index(group)].append([[bin2dec(i), bin2dec(j)], PI(i,j)])
       
       for i in group2:
          if i == []:
            group2.remove([])

       print('Tabela de Cobertura (Mintermos x Primos Implicantes):') 
       for i in group2:
           print(i)

       selectedPrimes(minBin,minBin2)
       #print(essentialPrimes)
       
       while True:
            if len(group2) == 1:
                for i in group2[0]:
                    essentialPrimes.append(i)
                break

            group1 = group2
            group2 = []
            minBin = []
            minBin2 = []
            
            for i in range(len(group1) - 1):
                group2.append([])

            for i in group1[:-1]:
                for j in i:
                    if j[-1] not in minBin: minBin.append(j)
                    for k in group1[group1.index(i) + 1]:
                        if k[-1] not in minBin: minBin.append(k)
                        if isBitShift_1(j[-1], k[-1]):
                            if j[-1] not in minBin2: minBin2.append(j)
                            if k[-1] not in minBin2: minBin2.append(k)
                            group2[group1.index(i)].append([j[0] + k[0], PI(j[-1], k[-1])])

            for i in group2:
                if i == []:
                    group2.remove([])
            
            selectedPrimes(minBin,minBin2)
           # print(essentialPrimes)
            if len(group2) == 0:
                break
            if len(group2[0]) == 0:
                break
            if len(group2[0]) != 0 and len(group2)==1:
                selectedPrimes.append(group2[0][0])
                break
           # print(selectedPrimes)

       filtro = []

       for i in essentialPrimes:
           x = i[0]
           if type(x) is list:
              x.sort()
           y = [x,i[1]]
           if y not in filtro:
              filtro.append(y)

       #print('filtro:',filtro)

       copylist = minterms.copy()
       copy2 = filtro.copy()
       for i in copy2:
           if type(i[0]) is int:
                filtro[copy2.index(i)][0] = [filtro[copy2.index(i)][0]]

       #print(filtro)

       chosen = []

       for i in copylist:
           cont = 0
           eq = []
           for j in filtro:
               if i in j[0]:
                  cont+=1
                  eq.append(j)
           if cont==1:
              if eq[0] not in chosen: chosen.append(eq[0])
              
              for a in eq[0][0]:
                  if a in minterms: minterms.remove(a)
        
       for i in chosen: 
           filtro.remove(i)

       while len(minterms) > 0:
            max = 0
            nextTerm = 0
            for i in filtro:
                cont = 0
                for j in i[0]:
                    if j in minterms:
                        cont += 1
                    if cont > max:
                        max = cont
                        nextTerm = i
            filtro.remove(nextTerm)
            chosen.append(nextTerm)
            for b in nextTerm[0]:
                if b in minterms: minterms.remove(b)
            
       for i in chosen:
           epi.append(i[1])


       #ep = ['0000_','0_01','011_']
       solucao = ""
       solucao += binario_para_equacao(epi[0])
       for x in range(1,len(epi)):
           solucao += " + " + binario_para_equacao(epi[x])
       print(solucao)

    elif op == "2":
       print("Digite a tabela verdade da equação separando cada linha por um espaço:")
       entradaBin = input()
       aux = entradaBin
       for i,b in enumerate(entradaBin):
           if b == ' ':
              aux = entradaBin.split()

       tabelaV.append(aux)
       tam = len(aux)
       minterms =  listaMintermos(tabelaV,tam,aux)
       print("Mintermos:",minterms) 
       grupos = agrupaUns(aux,nMint-1)
       print("Agrupamento:",grupos)

       #ep = ['0000_','0_01','011_']
       solucao = ""
       solucao += binario_para_equacao(epi[0])
       for x in range(1,len(epi)):
           solucao += " + " + binario_para_equacao(epi[x])
       print(solucao)


    elif op == "3":
        return 0
    else:
        print("Opção invalida! Tente Novamente!\n")
        return main()




main()       
