def somar_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento 
    return soma

lista_valores = [10,30,50,90,80]

resultado = somar_lista(lista_valores)

print(f"A soma do vlores da lista é: { resultado}")
