import csv

lista1 = []
lista2 = []

with open('lista1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        lista1.append(row[0])

with open('lista2.csv', 'r') as csvfile:
    spamreader2 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader2:
        lista2.append(row[0])

iguais = []
diferentes = []

for element in lista2:
    if element in lista1:
        iguais.append(element)
    else:
        diferentes.append(element)

print('Números presentes nas duas listas:', iguais)
print('Números presentes apenas na lista comparada:', diferentes)

with open("log-diferentes.csv", "w") as text_file:
    for i in diferentes:
        print(i, file=text_file)