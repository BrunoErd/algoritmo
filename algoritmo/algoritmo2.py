def calcular_media_notas(n):
    soma_notas = 0.0
    
    for i in range(n):
        nota = float(input(f"Digite a nota {i + 1}: "))
        soma_notas += nota
    
    media = soma_notas / n
    
    return media

n = int(input("Digite o número de notas: "))


media_notas = calcular_media_notas(n)
print(f"A média das {n} notas é: {media_notas}")
