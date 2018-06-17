import random
arq = open("perguntas.txt",'r')
arq2 = open("respostas.txt", 'r')
perg = arq.readline()
resp = arq2.readline()
data_base_p = list()
data_base_r = list()
while perg != "fim\n":
    data_base_p.append(perg)
    data_base_r.append(resp)
    perg = arq.readline()
    resp = arq2.readline()

arq.close()
arq2.close()
prox = input("Digite qualquer coisa para iniciar, e 'sair' quando acabar")
while prox != "sair":
    aleatorio = random.randint(0, len(data_base_p)-1)
    print(data_base_p[aleatorio], end="")
    prox = input()
    print("Resposta:", data_base_r[aleatorio])
