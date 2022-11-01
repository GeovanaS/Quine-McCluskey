# Trabalho 1 - Ferramenta de CAD 

# Geovana Silva da Silveira

# Algoritmo de Quine-McCluskey para solucionar mapas de Karnaugh de 4 variaveis

#Exemplos de entradas:
#!A*!B*!C*!D + !A*!B*!C*D + !A*B*!C*D + !A*B*C*!D + !A*B*C*D
#!A*B*!C*D + !A*B*C*!D + !A*B*C*D + A*!B*!C*D + A*!B*C*!D

vBin = []
tabelaV = []
epi = []
selected_primes =[]

#numero de mintermos
nMint = 0
#numero de literais
nLiterais = 0


# Converte equacao binaria para decimal
def bin2dec(vBin):
    soma = 0
    n = len(vBin) 
    for i,d in enumerate(vBin):
        if d == '1':
            soma += 2 ** (n-i-1)
    if n > 4:
        soma = int(soma/2)    
    return soma


# funcao auxiliar para remover elementos duplicados
def remove_duplicates(l):
    return list(set(l))    

# Lista os mintermos da equacao
def listaMintermos(vBin,tam,aux):
    i=0
    mintermo_lista = []
    for i in range(0,tam):
        mintermo_lista.append(bin2dec(aux[i]))
        mintermo_lista=remove_duplicates(mintermo_lista)
    return mintermo_lista

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
    global nLiterais
    eq = ''

    if(selectedPrimes[0]=='1'):
        eq += str("A")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[0]=='0'):
        eq += str("!A")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[0]=='_'):
        eq+=str("")

    if(selectedPrimes[1]=='1'):
        eq+=str("B")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[1]=='0'):
        eq+=str("!B")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[1]=='_'):
        eq+=str("")

    if(selectedPrimes[2]=='1'):
        eq+=str("C")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[2]=='0'):
        eq+=str("!C")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[2]=='_'):
        eq+=str("")

    if(selectedPrimes[3]=='1'):
        eq+=str("D")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[3]=='0'):
        eq+=str("!D")
        nLiterais = nLiterais + 1
    elif(selectedPrimes[3]=='_'):
        eq+=str("")

    return eq


# Funcao auxiliar que compara duas strings    
def compara_strings(str1, str2): 
    for i in range(len(str1)):
        if str1[i] == '_':
            if str1[i] != str2[i]:
                return False
    cont = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cont+=1
    if cont > 1:
        return False
    return True


# Gera os primos implicantes
def geraPrimos(str1,str2):
    saida = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            saida += str1[i]
        else:
            saida += '_'
    return saida


# Gera o conjunto minimo de primos(selected primes)    
def selectedPrimes(str1,str2):
    global selected_primes
    for i in str1:
        if i not in str2 and i not in selected_primes:
            selected_primes.append(i)



# Função main 
def main():
    op = input("Escolha a opção de entrada\n1-SOP\n2-Tabela Verdade\n3-Sair\n")
    if op == "1":
       print("Digite a equação no formato SOP:")  
       entrada = input() #le a entrada do usuario
       aux = entradaSOP(entrada) # armazena a expressao em binario
       binario = remove_duplicates(aux)
       #vBin.append(aux)
       print("Equação em binario:\n",binario)
       nMint = len(aux) #numero de mintermos
       minterms = listaMintermos(vBin,nMint,aux)
       print("Mintermos:\n",minterms)

       mintermos = listaMintermos(vBin,nMint,aux)
       
       n = nMint

       # Cria lista para armazena as expressoes agrupadas pelo numero de 1's
       group1 = []
       for i in range(n+1):
           group1.append([])
       
       for i in aux:
           group1[i.count('1')].append(i)  

       for i in group1:
           if i == []:
              group1.remove(i) # remove o que nao é usado     

       #print('Searching for primes:\n',group1) 
       print('Searching for primes')
       print('Column 0')
       print(group1)
       #print('Group 0:',group1[0])
       #print('Group 1:',group1[1])
       #print('Group 2:',group1[2])
       #print('Group 3:',group1[3])

       ##########################################################################   
       #Covering table
       ##########################################################################
       group2 = [] #armazena primos e mintermos que eles cobrem
       primos = [] #armazena primos implicantes
       minBin = [] #armazena mintermos e sua representação binaria
       minBin2 = [] #armazena mintermos e binario ordenado
       numPrimos = 0

       for i in range(n+1):
           group2.append([])

       for group in group1[:-1]:
           for i in group:
               if i not in minBin:minBin.append([bin2dec(i),i])
               for j in group1[group1.index(group)+1]:
                   if j not in minBin:minBin.append([bin2dec(j),j])
                   if bin2dec(i) > bin2dec(j):
                      continue
                   elif compara_strings(i,j):
                        if i not in minBin2: minBin2.append([bin2dec(i),i])
                        if j not in minBin2: minBin2.append([bin2dec(i),i])
                        primos.append(geraPrimos(i,j))
                        numPrimos+=1
                        group2[group1.index(group)].append([[bin2dec(i), bin2dec(j)], geraPrimos(i,j)])
       
       for i in group2: 
          if i == []:
            group2.remove([])
       
       print('Column 1')
       for i in range(numPrimos):
         print(primos[i])

       print('Covering Table (Prime and the minterms they cover):')
       for i in group2:
         if i != []: 
           print(i)

       ############################################################## 
       # Minimal set of primes (selected primes)
       ##############################################################
       selectedPrimes(minBin,minBin2)
       
       while True:  
            if len(group2) == 1:
                for i in group2[0]:
                    selected_primes.append(i)
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
                        if compara_strings(j[-1], k[-1]):
                            if j[-1] not in minBin2: minBin2.append(j)
                            if k[-1] not in minBin2: minBin2.append(k)
                            group2[group1.index(i)].append([j[0] + k[0], geraPrimos(j[-1], k[-1])])


            for i in group2:
                if i == []:
                    group2.remove([]) #remove o que nao eh usado
            
            selectedPrimes(minBin,minBin2)
            if len(group2) == 0:
                break
            if len(group2[0]) == 0:
                break
            if len(group2[0]) != 0 and len(group2)==1:
                selectedPrimes.append(group2[0][0])
                break

       tabCobertura = []

       for i in selected_primes:
           x = i[0]
           if type(x) is list:
              x.sort() #ordena os mintermos 
           y = [x,i[1]] #armazena a covering table
           if y not in tabCobertura:
              tabCobertura.append(y)
        
       lista1 = minterms.copy() 
       lista2 = tabCobertura.copy()  
       for i in lista2: 
           if type(i[0]) is int:
                tabCobertura[lista2.index(i)][0] = [tabCobertura[lista2.index(i)][0]]

       essentialPrime = []
       for i in lista1:
           cont = 0
           exp = []
           for j in tabCobertura:
               if i in j[0]:
                  cont+=1
                  exp.append(j)
           if cont==1:
              if exp[0] not in essentialPrime: essentialPrime.append(exp[0])
              for a in exp[0][0]:
                  if a in minterms: minterms.remove(a)
       
       for i in essentialPrime: 
           tabCobertura.remove(i)
       
       print('Essential Primes:')
       for i in essentialPrime:
           print(i[1])

       while len(minterms) > 0:
            tam = 0
            proxTermo = 0
            for i in tabCobertura:
                cont = 0
                for j in i[0]:
                    if j in minterms:
                        cont += 1
                if cont > tam:
                    tam = cont
                    proxTermo = i
            tabCobertura.remove(proxTermo)
            essentialPrime.append(proxTermo)
            for b in proxTermo[0]:
                if b in minterms: minterms.remove(b)

       epi=[]
       #print('Essential Prime:',essentialPrime)     
       for i in essentialPrime:
             epi.append(i[1]) #insere na lista os primos necessarios para a simplicacao
       

       print('Essential Prime Implicants:\n',epi)

       setPrimos = []
       for i in epi:
            setPrimos.append(i)     

       solucao = ""
       solucao += binario_para_equacao(setPrimos[0])
       for x in range(1,len(setPrimos)):
           solucao += " + " + binario_para_equacao(setPrimos[x])

       print("Saida: ",solucao," / ", nLiterais,"Literais")

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
       n=tam

       # cria lista group1 para armazenar as expressoes agrupada pelo numero de 1's
       group1 = []
       for i in range(n+1):
           group1.append([])

       for i in aux:
           group1[i.count('1')].append(i) 

       for i in group1:   
           if i == []: 
              group1.remove([]) #remove o que nao é usado

       print('Searching for primes\n',group1)

      ######################################################################
      #Covering table
      ######################################################################
       group2 = [] #armazena primos e mintermos que eles cobrem
       primos = [] #primos implicantes
       minBin = [] #armazena mintermos e sua respectiva representacao binaria
       minBin2 = [] #armazena mintermos e o binario de forma ordenada

       for i in range(n):
           group2.append([])

       for group in group1[:-1]:
            for i in group:
                if i not in minBin: minBin.append([bin2dec(i),i]) #insere na lista mintermo e o binario
                for j in group1[group1.index(group)+1]:
                    if j not in minBin:minBin.append([bin2dec(j),j])
                    if bin2dec(i) > bin2dec(j):
                        continue
                    elif compara_strings(i,j): 
                        if i not in minBin2: minBin2.append([bin2dec(i),i])
                        if j not in minBin2: minBin2.append([bin2dec(j),j])
                        primos.append(geraPrimos(i,j))
                        group2[group1.index(group)].append([[bin2dec(i), bin2dec(j)], geraPrimos(i,j)]) #insere na lista os primos e mintermos que eles cobrem
       
       for i in group2:
          if i == []:
            group2.remove([]) #remove o que nao é usado
       
       print("Covering Table (Prime and the minterms they cover):")
       for i in group2:
           print(i)
       ######################################################################
       # Minimal set of primes (selected primes)
       ######################################################################
       selectedPrimes(minBin,minBin2)

       while True:
          if len(group2) == 1:
            for i in group2[0]:
                selected_primes.append(i)
            break
          
          group1 = group2
          group2 = []
          minBin = []
          minBin2 = []

          for i in range(len(group1)-1):
              group2.append([])
          
          for i in group1[:-1]:
            for j in i:
                if j[-1] not in minBin:minBin.append(j)
                for k in group1[group1.index(i) + 1]:
                    if k[-1] not in minBin:minBin.append(k)
                    if compara_strings(j[-1],k[-1]):
                        if j[-1] not in minBin2:minBin2.append(j)
                        if k[-1] not in minBin2:minBin2.append(k)
                        group2[group1.index(i)].append([j[0] + k[0], geraPrimos(j[-1],k[-1])])
                          
          for i in group2:
            if i == []:
              group2.remove([])

          selectedPrimes(minBin,minBin2)
          if len(group2) == 0:
             break
          if len(group[0]) == 0:
            break
          if len(group2[0]) != 0 and len(group2)==1:
             selectedPrimes.append(group2[0][0])
             break
            
       tabCobertura = []
       for i in selected_primes:
           x = i[0]
           if type(x) is list:
               x.sort()
           y = [x,i[1]] #armazena a covering table 
           if y not in tabCobertura:
              tabCobertura.append(y)  
        
       lista1 = minterms.copy()
       lista2 = tabCobertura.copy()
       for i in lista2:
           if type(i[0]) is int:
              tabCobertura[lista2.index(i)][0] = [tabCobertura[lista2.index(i)][0]]
             
        #print('tab:',tabCobertura)
            
       essentialPrime = []

       for i in lista1:
           cont = 0
           exp = []
           for j in tabCobertura:
              if i in j[0]:
                 cont+=1
                 exp.append(j)
           if cont == 1:
              if exp[0] not in essentialPrime: essentialPrime.append(exp[0])
              for a in exp[0][0]:
                  if a in minterms: minterms.remove(a)

       print('Essential Prime:',essentialPrime) 
       for i in essentialPrime:
          tabCobertura.remove(i)

       while len(minterms) > 0:
            max = 0
            proxTerm = 0
            for i in tabCobertura:
                cont = 0
                for j in i[0]:
                    if j in minterms:
                        cont += 1
                    if cont > max:
                        max = cont
                        proxTerm = i
            tabCobertura.remove(proxTerm)
            essentialPrime.append(proxTerm)
            for b in proxTerm[0]:
                if b in minterms: minterms.remove(b) 

       for i in essentialPrime:
           epi.append(i[1])
          
       solucao = ""
       solucao += binario_para_equacao(epi[0])
       for x in range(1,len(epi)):
           solucao += " + " + binario_para_equacao(epi[x])
       print("Saida: ", solucao, " / ", nLiterais, "Literais")


    elif op == "3":
        return 0
    else:
        print("Opção invalida! Tente Novamente!\n")
        return main()




main()       
