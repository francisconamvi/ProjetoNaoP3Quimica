import random
arq = open("perguntas.txt",'r')
perg = arq.readline()
data_base = list()
while perg != "fim\n":
	data_base.append(perg)
	perg = arq.readline()
prox = input("Digite qualquer coisa para iniciar, e 'sair' quando acabar")
while prox != "sair":
	print(data_base[random.randint(0, len(data_base)-1)])
	prox = input()
