d1 = {"mae": "yoko", "pai": "john", "filho": "sean"}
d2 = {"bateria": "ringo", "baixo": "paul", "guitarra": "george"}

print(d1, d2)

d1.pop("mae")#remove elemento com chave "mae"
print(d1)

d1.update(d2) #atualiza d1 com dados de d2
print(d1)

d1["guitarra2"] = "john" #insere elemento "guitarra2": "john" em d1
print(d1)

d1.pop("pai")
d1.pop("filho")

print("agora temos os beatles: ", d1)