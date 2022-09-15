d1 = {"mae": "yoko", "pai": "john", "filho": "sean"}


print(d1.get("mae")) #se existe retorna o valor
print(d1.get("primo")) #se nao existe nao da erro, retorna none

for chave in d1: print(chave)
print()

for valor in d1.values(): print(valor)
print()

for chave, valor in d1.items(): print(chave, valor)

