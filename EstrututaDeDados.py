<<<<<<< HEAD
#conceitos Estrutura de dados

#listas
#contem em lista função in

from statistics import median, median_grouped, median_high, median_low


animals = ['gato', 'cachorro', 'pagagaio']

print('gato' in animals)

#tamanho da lista 

print(len(animals))

#max min e media
list = [10,20,30,40,50,60,70,80,90,100,11,22,33]

print(list)

print(max(list))
print(min(list))
print(median(list))

#adicionar um argumento ao final da lista 

animals.append("leao")

#adicionar varios elementos

animals.extend(["vaca", "cobra", 'rato'])

print(animals)

#contar elementos
print(animals.count('vaca'))

#ordenação de lista
list.sort()
print(list)
animals.sort()
print(animals)

#Tuplas

#Tuplas são imutáveis

tp = ('maça', 'banana', 'melancia')

print(tp)
print(tp[0])
print(tp.count('maça'))
print(tp[0:2])

#Dicionários
# Dicionários são estrutura chave:valor

dic= {"Maça":20, "Banana":10, "Laranja":15, "Uva":5}

print(dic)
print(dic['Maça'])

#Atribuindo valor a uma chave
dic["Maça"]=23
print(dic['Maça'])

#Retornando as chaves 

print(dic.keys())

#Retonndo os valores

print(dic.values())

#Verificar chave existente e caso false inserir
dic.setdefault("Pera",50)
print(dic)
dic.setdefault("Pera",50)
print(dic)






=======
#conceitos Estrutura de dados

#listas
#contem em lista função in

from statistics import median, median_grouped, median_high, median_low


animals = ['gato', 'cachorro', 'pagagaio']

print('gato' in animals)

#tamanho da lista 

print(len(animals))

#max min e media
list = [10,20,30,40,50,60,70,80,90,100,11,22,33]

print(list)

print(max(list))
print(min(list))
print(median(list))

#adicionar um argumento ao final da lista 

animals.append("leao")

#adicionar varios elementos

animals.extend(["vaca", "cobra", 'rato'])

print(animals)

#contar elementos
print(animals.count('vaca'))

#ordenação de lista
list.sort()
print(list)
animals.sort()
print(animals)

#Tuplas

#Tuplas são imutáveis

tp = ('maça', 'banana', 'melancia')

print(tp)
print(tp[0])
print(tp.count('maça'))
print(tp[0:2])

#Dicionários
# Dicionários são estrutura chave:valor

dic= {"Maça":20, "Banana":10, "Laranja":15, "Uva":5}

print(dic)
print(dic['Maça'])

#Atribuindo valor a uma chave
dic["Maça"]=23
print(dic['Maça'])

#Retornando as chaves 

print(dic.keys())

#Retonndo os valores

print(dic.values())

#Verificar chave existente e caso false inserir
dic.setdefault("Pera",50)
print(dic)
dic.setdefault("Pera",50)
print(dic)






>>>>>>> 42bbfde (Commit_1)
